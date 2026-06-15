from __future__ import annotations

# pylint: disable=invalid-name

from dataclasses import dataclass, field

import simplylang.parser as legacy_ast

from simplylang.diagnostics import Diagnostic


@dataclass
class SymbolInfo:
    name: str
    kind: str
    arity: int | None = None


@dataclass
class ResolveResult:
    diagnostics: list[Diagnostic] = field(default_factory=list)
    symbols: dict[str, SymbolInfo] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.diagnostics


class Resolver:
    """Small semantic pass for symbols, arity, and obvious name errors."""

    def __init__(self) -> None:
        self.result = ResolveResult()
        self.scopes: list[set[str]] = [set(["NULL"])]
        self.function_depth = 0

    def resolve(self, node) -> ResolveResult:
        self._declare_top_level(node)
        self._visit(node)
        return self.result

    def _declare(self, name: str, kind: str, arity: int | None = None) -> None:
        if name in self.scopes[-1]:
            self.result.diagnostics.append(
                Diagnostic(
                    message=f"{kind.title()} '{name}' is already defined",
                    code="SL1003",
                )
            )
            return
        self.scopes[-1].add(name)
        self.result.symbols[name] = SymbolInfo(name, kind, arity)

    def _assign(self, name: str) -> None:
        self.scopes[-1].add(name)
        self.result.symbols[name] = SymbolInfo(name, "variable")

    def _is_defined(self, name: str) -> bool:
        return any(name in scope for scope in reversed(self.scopes))

    def _diagnose(self, _node, message: str, code: str) -> None:
        self.result.diagnostics.append(Diagnostic(message=message, code=code))

    def _declare_top_level(self, node) -> None:
        statements = getattr(node, "statements", [])
        for statement in statements:
            if isinstance(statement, legacy_ast.FunctionNode):
                arity = len(statement.variables or [])
                self._declare(statement.function_name.value, "function", arity)
            elif isinstance(statement, legacy_ast.ClassNode):
                self._declare(
                    statement.class_name, "class", len(statement.variable or [])
                )
            elif isinstance(statement, legacy_ast.ContractNode):
                self._declare(
                    statement.contract_name.value,
                    "contract",
                    len(statement.variables or []),
                )

    def _visit(self, node) -> None:
        if not hasattr(node, "__dict__"):
            return
        method = getattr(self, f"_visit_{type(node).__name__}", self._visit_children)
        method(node)

    def _visit_children(self, node) -> None:
        for value in vars(node).values():
            if isinstance(value, list):
                for item in value:
                    if hasattr(item, "__dict__"):
                        self._visit(item)
            elif hasattr(value, "__dict__"):
                self._visit(value)

    def _visit_StatementsNode(self, node: legacy_ast.StatementsNode) -> None:
        for statement in node.statements:
            self._visit(statement)

    def _visit_VariableNode(self, node: legacy_ast.VariableNode) -> None:
        self._visit(node.value_node)
        self._assign(node.variable_name.value)

    def _visit_ArrayNode(self, node: legacy_ast.ArrayNode) -> None:
        self._assign(node.variable_name.value)

    def _visit_DictNode(self, node: legacy_ast.DictNode) -> None:
        self._assign(node.variable_name.value)

    def _visit_AccessDictNode(self, node: legacy_ast.AccessDictNode) -> None:
        if not self._is_defined(node.dict.value):
            self._diagnose(node, f"'{node.dict.value}' is not defined", "SL1001")
        self._assign(node.variable.value)

    def _visit_UpdateDictNode(self, node: legacy_ast.UpdateDictNode) -> None:
        if not self._is_defined(node.dict):
            self._diagnose(node, f"'{node.dict}' is not defined", "SL1001")
        self._visit(node.expression)

    def _visit_ArrayAccessNode(self, node: legacy_ast.ArrayAccessNode) -> None:
        if not self._is_defined(node.access_variable):
            self._diagnose(node, f"'{node.access_variable}' is not defined", "SL1001")
        self._assign(node.variable_name.value)

    def _visit_ArrayLengthNode(self, node: legacy_ast.ArrayLengthNode) -> None:
        if not self._is_defined(node.expression.value):
            self._diagnose(node, f"'{node.expression.value}' is not defined", "SL1001")
        self._assign(node.variable.value)

    def _visit_ArrayArrangeNode(self, node: legacy_ast.ArrayArrangeNode) -> None:
        if not self._is_defined(node.array.value):
            self._diagnose(node, f"'{node.array.value}' is not defined", "SL1001")
        self._assign(node.variable_name.value)

    def _visit_VariableFunctionNode(
        self, node: legacy_ast.VariableFunctionNode
    ) -> None:
        self._visit(node.value_node)
        self._assign(node.variable_name.value)

    def _visit_VariableAccessNode(self, node: legacy_ast.VariableAccessNode) -> None:
        name = node.variable_name.value
        if not self._is_defined(name):
            self._diagnose(node, f"'{name}' is not defined", "SL1001")

    def _visit_FunctionNode(self, node: legacy_ast.FunctionNode) -> None:
        self.function_depth += 1
        self.scopes.append(set(node.variables or []))
        for statement in node.body:
            self._visit(statement)
        self.scopes.pop()
        self.function_depth -= 1

    def _visit_FunctionCallNode(self, node: legacy_ast.FunctionCallNode) -> None:
        symbol = self.result.symbols.get(node.function_name)
        if not symbol:
            self._diagnose(
                node,
                f"Function '{node.function_name}' is not defined",
                "SL1001",
            )
        if symbol and symbol.arity is not None and symbol.arity != len(node.parameters):
            self._diagnose(
                node,
                f"Function '{node.function_name}' expects {symbol.arity} arguments",
                "SL1002",
            )
        for parameter in node.parameters:
            if (
                isinstance(parameter, str)
                and parameter.isidentifier()
                and not self._is_defined(parameter)
            ):
                # Numeric literals arrive as raw ints/floats, while identifier arguments
                # are strings in the current AST.
                self._diagnose(node, f"'{parameter}' is not defined", "SL1001")

    def _visit_ReturnNode(self, node: legacy_ast.ReturnNode) -> None:
        if self.function_depth == 0:
            self._diagnose(node, "`return` is only valid inside a function", "SL1004")
        token = node.token
        if getattr(token, "type", None) == "IDENTIFIER" and not self._is_defined(
            token.value
        ):
            self._diagnose(node, f"'{token.value}' is not defined", "SL1001")

    def _visit_ReturnExprNode(self, node: legacy_ast.ReturnExprNode) -> None:
        if self.function_depth == 0:
            self._diagnose(node, "`return` is only valid inside a function", "SL1004")
        self._visit(node.token)


def resolve(node) -> ResolveResult:
    return Resolver().resolve(node)
