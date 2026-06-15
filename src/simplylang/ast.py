"""AST facade for SimplyLang.

The current parser still constructs the legacy node classes from `praser.py`.
This module centralizes that public AST surface so future refactors can replace
the implementation without changing callers.
"""

# pylint: disable=unused-import

from dataclasses import dataclass, field
from typing import Any

from simplylang.parser import (  # noqa: F401
    AccessDictNode,
    ArrayAccessNode,
    ArrayArrangeNode,
    ArrayLengthNode,
    ArrayNode,
    ArrayVariable,
    BinaryOperationNode,
    BoolNode,
    CallContractNode,
    ClassAccessNode,
    ClassAssignNode,
    ClassNode,
    ClassifyNode,
    ContractNode,
    DictNode,
    FunctionCallNode,
    FunctionNode,
    GetPictureNode,
    IfNode,
    NoteNode,
    NumberNode,
    RepeatNode,
    ReturnExprNode,
    ReturnNode,
    ShowMultiNode,
    ShowNode,
    StatementsNode,
    StopNode,
    TillNode,
    TryNode,
    UniaryOperatorNode,
    UpdateDictNode,
    VariableAccessNode,
    VariableClassFunctionNode,
    VariableFunctionNode,
    VariableNode,
)
from simplylang.source import Span


@dataclass(frozen=True)
class AstNode:
    span: Span | None = None


@dataclass(frozen=True)
class Program(AstNode):
    statements: tuple[AstNode, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class Expression(AstNode):
    value: Any = None


@dataclass(frozen=True)
class Statement(AstNode):
    value: Any = None


def iter_child_nodes(node):
    """Yield direct child AST nodes from the legacy AST shape."""

    for attribute in (
        "statements",
        "body",
        "then_expr",
        "otherwise_expr",
        "left",
        "right",
        "condition_expr",
        "value_node",
        "node",
    ):
        value = getattr(node, attribute, None)
        if value is None:
            continue
        if isinstance(value, list):
            yield from (item for item in value if hasattr(item, "pos_start"))
        elif hasattr(value, "pos_start"):
            yield value
