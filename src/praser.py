from typing import Any
import lexer


class StatementsNode:
    def __init__(self, statements):
        self.statements = statements

        if self.statements:
            self.pos_start = self.statements[0].pos_start
            self.pos_end = self.statements[-1].pos_end
        else:
            self.pos_start = None
            self.pos_end = None


class BinaryOperationNode:
    def __init__(self, left, op, right):

        self.left = left
        self.token = op
        self.right = right
        self.pos_start = self.left.pos_start
        self.pos_end = self.right.pos_end

    def __repr__(self) -> str:
        return f"({self.left} {self.token.value} {self.right})"


class CallContractNode:
    def __init__(self, name, parameters):
        self.contract_name = name
        self.parameters = parameters
        self.pos_start = name.start
        self.pos_end = name.end

    def __repr__(self):
        return f"(call {self.contract_name})"


class ContractNode:
    def __init__(self, name, body, variables=None):
        self.contract_name = name
        self.body = body
        self.variables = variables
        if len(body) > 0:
            self.pos_start = body[0].pos_start
            self.pos_end = body[len(body) - 1].pos_end
        else:
            self.pos_start = name.start
            self.pos_end = name.end

    def __repr__(self):
        return f"(contract {self.contract_name} : {self.body})"


class GetPictureNode:
    def __init__(self, variable):
        self.varibale = variable
        self.pos_start = variable.pos_start
        self.pos_end = variable.pos_end

    def __repr__(self) -> str:
        return f"({self.varibale_name})"


class IfNode:
    def __init__(self, condition_expr, then_expr, otherwise_expr=None):
        self.condition_expr = condition_expr
        self.then_expr = then_expr
        self.otherwise_expr = otherwise_expr
        self.pos_start = self.condition_expr.pos_start
        self.pos_end = (self.otherwise_expr[len(self.otherwise_expr) - 1]).pos_end

    def __repr__(self) -> str:
        if self.otherwise_expr:
            return f"(if {self.condition_expr} then {self.then_expr} otherwise {self.otherwise_expr})"
        return f"(if {self.condition_expr} then {self.then_expr})"


class TryNode:
    def __init__(self, then_expr, otherwise_expr=None):
        self.then_expr = then_expr
        self.otherwise_expr = otherwise_expr
        self.pos_end = (self.otherwise_expr[len(self.otherwise_expr) - 1]).pos_end

    def __repr__(self) -> str:
        if self.otherwise_expr:
            return f"{self.then_expr} otherwise {self.otherwise_expr})"
        return f"(try {self.then_expr})"


class FunctionNode:
    def __init__(self, name, body, variables=None) -> Any:
        self.function_name = name
        self.body = body
        self.variables = variables
        self.pos_start = self.body[0].pos_start
        self.pos_end = self.body[len(self.body) - 1].pos_end

    def __repr__(self) -> str:
        return f"({self.body})"


class FunctionCallNode:
    def __init__(self, function_name, function, parameters) -> Any:
        self.function_name = function_name
        self.parameters = parameters
        self.pos_start = function.start
        self.pos_end = function.end

    def __repr__(self) -> str:
        return f"({self.function_name})"


class ClassNode:
    def __init__(self, name, body, variable) -> Any:
        self.class_name = name
        self.variable = variable
        self.body = body
        self.pos_start = self.body[0].pos_start
        self.pos_end = self.body[len(self.body) - 1].pos_end

    def __repr__(self) -> str:
        return f"({self.body})"


class ClassifyNode:
    def __init__(self, variable):
        self.variable_name = variable.value
        self.pos_start = variable.start
        self.pos_end = variable.end

    def __repr__(self) -> str:
        return f"({self.variable_name})"


class TillNode:
    def __init__(self, condition_expr, body):
        self.condition_expr = condition_expr
        self.body = body
        self.pos_start = self.condition_expr.pos_start
        self.pos_end = self.body[len(self.body) - 1].pos_end

    def __repr__(self) -> str:
        return f"(till {self.condition_expr} do {self.body})"


class ShowNode:
    def __init__(self, body, position_var):
        self.body = body
        self.pos_start = position_var.start
        self.pos_end = position_var.end


class VariableAccessNode:
    def __init__(self, varible_name_token):
        self.variable_name = varible_name_token
        self.pos_start = self.variable_name.start
        self.pos_end = self.variable_name.end


class ArrayVariable:
    def __init__(self, variable, index, expression):
        self.variable = variable
        self.index = index
        self.expression = expression

        self.pos_start = self.variable.start
        self.pos_end = self.variable.end


class ClassAccessNode:
    def __init__(self, class_name, access_node):
        self.class_name = class_name
        self.access_node = access_node
        self.pos_start = self.class_name.start
        self.pos_end = class_name.end

    def __repr__(self) -> str:
        return f"({self.class_name} {self.access_node})"


class NoteNode:
    def __init__(self, note):
        self.note = note

        self.pos_start = note[0].start
        self.pos_end = note[-1].end

    def __repr__(self) -> str:
        return f"({self.note})"


class VariableNode:
    def __init__(self, varible_name, value_node):
        self.variable_name = varible_name
        self.value_node = value_node

        self.pos_start = self.variable_name.start
        self.pos_end = self.variable_name.end


class VariableFunctionNode:
    def __init__(self, varible_name, value_node):
        self.variable_name = varible_name
        self.value_node = value_node

        self.pos_start = self.variable_name.start
        self.pos_end = self.variable_name.end


class VariableClassFunctionNode:
    def __init__(self, varible_name, class_name, function):
        self.variable_name = varible_name
        self.class_name = class_name
        self.function = function

        self.pos_start = self.variable_name.start
        self.pos_end = self.variable_name.end


class ArrayNode:
    def __init__(self, varible_name, value_node):
        self.variable_name = varible_name
        self.value_node = value_node

        self.pos_start = self.variable_name.start
        self.pos_end = self.variable_name.end


class DictNode:
    def __init__(self, varible_name, dictronary):
        self.variable_name = varible_name
        self.dictronary = dictronary

        self.pos_start = self.variable_name.start
        self.pos_end = self.variable_name.end


class ArrayAccessNode:
    def __init__(self, varible_name, value_node, access_variable):
        self.variable_name = varible_name
        self.value_node = value_node
        self.access_variable = access_variable

        self.pos_start = self.variable_name.start
        self.pos_end = self.variable_name.end


class ArrayArrangeNode:
    def __init__(self, varible_name, array, type):
        self.variable_name = varible_name
        self.array = array
        self.type = type
        self.pos_start = self.variable_name.start
        self.pos_end = self.variable_name.end


class ClassAssignNode:
    def __init__(self, class_name, value_node, variables):
        self.class_name = class_name.value
        self.value_node = value_node.value
        self.variables = variables
        self.pos_start = value_node.start
        self.pos_end = value_node.end

    def __repr__(self) -> str:
        return f"({self.class_name} {self.value_node})"


class RepeatNode:
    def __init__(self, variable, body):
        self.range = variable.value
        self.body = body
        self.pos_start = variable.start
        self.pos_end = self.body[len(self.body) - 1].pos_end


class ReturnNode:
    def __init__(self, token):
        self.token = token
        self.pos_start = self.token.start
        self.pos_end = self.token.end


class ReturnExprNode:
    def __init__(self, token, pos_token):
        self.token = token
        self.pos_start = pos_token.start
        self.pos_end = pos_token.end


class UpdateDictNode:
    def __init__(self, key, dict, expression):
        self.key = key
        self.dict = dict
        self.expression = expression
        self.pos_start = key.start
        self.pos_end = key.end


class NumberNode:
    def __init__(self, token):
        self.token = token
        self.pos_start = self.token.start
        self.pos_end = self.token.end

    def __repr__(self) -> str:
        return f"{self.token}"


class StopNode:
    def __init__(self, token, string=""):
        self.token = token
        self.string = string
        self.pos_start = self.token.start
        self.pos_end = self.token.end


class BoolNode:
    def __init__(self, token):
        self.token = token
        self.pos_start = self.token.start
        self.pos_end = self.token.end

    def __repr__(self) -> str:
        return f"{self.token}"


class AccessDictNode:
    def __init__(self, variable, key, dict):
        self.variable = variable
        self.key = key
        self.dict = dict

        self.pos_start = variable.start
        self.pos_end = key.end


class ArrayLengthNode:
    def __init__(self, variable, expression):
        self.variable = variable
        self.expression = expression

        self.pos_start = self.variable.start
        self.pos_end = self.variable.end


class ShowMultiNode:
    def __init__(self, string, lb, variable):
        self.string = string
        self.variable = variable

        self.pos_start = lb.start
        self.pos_end = lb.end


class UniaryOperatorNode:
    def __init__(self, op_token, node):
        self.token = op_token
        self.node = node
        self.pos_start = op_token.start
        self.pos_end = node.pos_end

    def __repr__(self) -> str:
        return f"({self.token} {self.node})"


class ParserResult:
    def __init__(self):
        self.error = None
        self.node = None
        self.advance_count = 0

    def register_advance(self):
        self.advance_count += 1

    def register(self, res):
        if res != None:
            try:
                self.advance_count += res.advance_count
                if res.error:
                    self.error = res.error
                return res.node
            except:
                return res

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        if not self.error or self.advance_count == 0:
            self.error = error
            return self


class Praser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.variables = []
        self.functionNames = []
        self.is_class = False
        self.classNames = []
        self.classFunctionNames = []
        self.advance()

    def advance(self):
        self.index += 1
        self.current_token = (
            self.tokens[self.index] if self.index < len(self.tokens) else None
        )

    def parse(self):
        res = ParserResult()
        statements = []

        while self.current_token != None and self.current_token.type != lexer.TT_EOF:
            if self.current_token.type == lexer.TT_NEWLINE:
                res.register_advance()
                self.advance()
                continue

            stmt = res.register(self.expr())
            if res.error:
                return res
            statements.append(stmt)

            if self.current_token != None and self.current_token.type not in (
                lexer.TT_NEWLINE,
                lexer.TT_EOF,
            ):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected newline or end of input",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )

        return res.success(StatementsNode(statements))

    def factor(self):
        result = ParserResult()
        token = self.current_token
        if token != None:
            if token.type in (lexer.TT_ADD, lexer.TT_MINUS):
                result.register_advance()
                self.advance()
                factor = result.register(self.factor())
                if result.error:
                    return result
                return result.success(UniaryOperatorNode(token, factor))

            elif token.type in (lexer.TT_GT, lexer.TT_LT):

                result.register_advance()
                self.advance()
                factor = result.register(self.factor())
                if result.error:
                    return result
                return result.success(UniaryOperatorNode(token, factor))

            elif token.type == lexer.TT_POW:
                result.register_advance()
                self.advance()
                factor = result.register(self.factor())
                if result.error:
                    return result
                return result.success(UniaryOperatorNode(token, factor))
            elif token.type == lexer.TT_MOD:
                result.register_advance()
                self.advance()
                factor = result.register(self.factor())
                if result.error:
                    return result
                return result.success(UniaryOperatorNode(token, factor))

            elif token.type == lexer.TT_EQUAL:
                result.register_advance()
                self.advance()
                factor = result.register(self.factor())
                if result.error:
                    return result
                return result.success(UniaryOperatorNode(token, factor))

            elif token.type == lexer.TT_NOT_EQUAL:
                result.register_advance()
                self.advance()
                factor = result.register(self.factor())
                if result.error:
                    return result
                return result.success(UniaryOperatorNode(token, factor))

            elif token.type in (lexer.TT_INT, lexer.TT_DOUBLE):
                result.register_advance()
                self.advance()
                return result.success(NumberNode(token))

            elif token.type == lexer.TT_BOOL:
                result.register_advance()
                self.advance()
                return result.success(BoolNode(token))

            elif token.type == lexer.TT_IDENTIFIER:
                result.register_advance()
                self.advance()
                return result.success(VariableAccessNode(token))
            # else:
            #     return result.failure(lexer.InvalidSyntaxError( "Expected int or double" , token.start , token.end ))
            elif token.type in (lexer.TT_LP):
                result.register_advance()
                self.advance()
                expr = result.register(self.expr())
                if result.error:
                    return result
                if self.current_token.type == lexer.TT_RP:
                    result.register_advance()
                    self.advance()
                    return result.success(expr)
                else:
                    return result.failure(
                        lexer.InvalidSyntaxError(
                            "Expected ')' ",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )

    def bin_operation(self, function, ops):
        res = ParserResult()
        left = res.register(function())
        if res.error:
            return res
        while self.current_token is not None and self.current_token.type in ops:
            token = self.current_token
            res.register_advance()
            self.advance()
            right = res.register(function())
            if res.error:
                return res
            left = BinaryOperationNode(left, token, right)
        return res.success(left)

    def term(self):
        return self.bin_operation(self.factor, (lexer.TT_MUL, lexer.TT_DIV))

    def expr(self, seen=False):
        res = ParserResult()
        temp = self.current_token
        self.skip_newlines(res)

        if temp.type == lexer.TT_KEYWORD and temp.value == "stop":
            if self.tokens[self.index + 1].value == "with":
                self.advance()
                self.advance()

                if self.current_token.type != lexer.TT_STRING:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            'Expected "',
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )
                self.advance()
                string = ""
                while self.current_token.type != lexer.TT_STRING:
                    if self.current_token.type in (lexer.TT_NEWLINE, lexer.TT_EOF):
                        return res.failure(
                            lexer.InvalidSyntaxError(
                                'Expected "',
                                self.current_token.start,
                                self.current_token.end,
                            )
                        )
                    string += " " + self.current_token.value
                    self.advance()
                self.advance()
                return res.success(StopNode(temp, string))
            res.register_advance()
            self.advance()
            return res.success(StopNode(temp))

        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "return"
        ):
            self.advance()
            if self.current_token.type not in (
                lexer.TT_IDENTIFIER,
                lexer.TT_BOOL,
                lexer.TT_INT,
                lexer.TT_DOUBLE,
                lexer.TT_STRING,
            ):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Unexpected Identifier",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            pos_token = self.current_token
            if self.tokens[self.index + 1].type == lexer.TT_NEWLINE:
                value = self.current_token
                res.register_advance()
                self.advance()
                return res.success(ReturnNode(value))
            else:
                value = res.register(self.expr())
                if res.error:
                    return res
                res.register_advance()
                self.advance()
                return res.success(ReturnExprNode(value, pos_token))

        if not seen and self.current_token.type == lexer.TT_IDENTIFIER:
            res.register_advance()
            self.advance()

            if self.current_token.type == lexer.TT_LP:

                parameters = []
                if temp.value not in self.functionNames:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            f"Function Name {temp.value} not defined",
                            temp.start,
                            temp.end,
                        )
                    )
                self.advance()
                while self.current_token.type != lexer.TT_RP:
                    if self.current_token.type == lexer.TT_NEWLINE:
                        res.failure(
                            lexer.InvalidSyntaxError("Expected )", temp.start, temp.end)
                        )
                    if self.current_token.type == lexer.TT_IDENTIFIER:
                        if self.current_token.value not in self.variables:
                            return res.failure(
                                lexer.InvalidSyntaxError(
                                    f"Variable  Name {temp.value} not defined",
                                    temp.start,
                                    temp.end,
                                )
                            )

                    parameters.append(self.current_token.value)

                    self.advance()

                    self.skip_commas(res)

                self.advance()
                res.register_advance()

                return res.success(FunctionCallNode(temp.value, temp, parameters))

            if self.current_token.value == "of":
                self.advance()

                if self.current_token.type != lexer.TT_IDENTIFIER:
                    return res.failure(
                        SyntaxError(
                            f"Expected Identifier {temp.value} not defined",
                            temp.start,
                            temp.end,
                        )
                    )

                dict_name = self.current_token.value

                self.advance()
                if self.current_token.value != "is":
                    return res.failure(
                        SyntaxError(
                            f"Expected keyword 'is'",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )

                self.advance()
                expr = None

                # Check if the current token is a string
                if self.current_token.type == lexer.TT_STRING:
                    expr = ""
                    self.advance()  # Advance past the opening quote

                    while self.current_token.type != lexer.TT_STRING:
                        # Handle unexpected end of file or new line within a string
                        if self.current_token.type in (lexer.TT_EOF, lexer.TT_NEWLINE):
                            return res.failure(
                                lexer.InvalidSyntaxError(
                                    "Expected closing quote for string",
                                    self.current_token.start,
                                    self.current_token.end,
                                )
                            )
                        # Append current token value to the string expression
                        expr += " " + str(self.current_token.value)
                        self.advance()

                    self.advance()  # Advance past the closing quote
                else:
                    # Handle other expressions
                    expr = res.register(self.expr(True))
                    if res.error:
                        return res

                return res.success(UpdateDictNode(temp, dict_name, expr))

            if self.current_token.type == lexer.TT_STOP:
                self.advance()
                if self.current_token.type == lexer.TT_IDENTIFIER:
                    self.is_class = True
                    identifier = res.register(self.expr(True))
                    if res.error:
                        return res
                    return ClassAccessNode(temp, identifier)

            if self.current_token.value == "takes":
                self.advance()
                variables = []

                while self.current_token.value != "does":
                    if self.current_token.type != lexer.TT_IDENTIFIER:
                        return res.failure(
                            lexer.InvalidSyntaxError(
                                f"Expected Identifier not {self.current_token.type} "
                            )
                        )
                    variable = self.current_token.value
                    variables.append(variable)
                    self.variables.append(variable)

                    self.advance()

                    if self.current_token.type == lexer.TT_COMMA:
                        self.advance()

                if self.current_token.value == "does":
                    if temp.value in self.functionNames:
                        return res.failure(
                            lexer.InvalidSyntaxError(
                                f"Function Name {temp.value} already defined",
                                self.current_token.start,
                                self.current_token.end,
                            )
                        )
                    name = temp
                    res.register_advance()
                    self.advance()
                    then_expr = []
                    while self.current_token.type != lexer.TT_STOP:
                        self.skip_newlines(res)
                        expr = res.register(self.expr())
                        if res.error:
                            return res
                        then_expr.append(expr)
                        self.skip_newlines(res)
                    res.register_advance()  # Consume the STOP token
                    self.advance()
                    if self.is_class:
                        self.classFunctionNames.append(name.value)
                    else:
                        self.functionNames.append(name.value)
                    return res.success(FunctionNode(name, then_expr, variables))

            if self.current_token.value == "does":
                if temp.value in self.functionNames:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            f"Function Name {temp.value} already defined",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )
                name = temp
                res.register_advance()
                self.advance()
                then_expr = []
                while self.current_token.type != lexer.TT_STOP:
                    self.skip_newlines(res)
                    expr = res.register(self.expr())
                    if res.error:
                        return res
                    then_expr.append(expr)
                    self.skip_newlines(res)
                res.register_advance()  # Consume the STOP token
                self.advance()
                if self.is_class:
                    self.classFunctionNames.append(name.value)
                else:
                    self.functionNames.append(name.value)
                return res.success(FunctionNode(name, then_expr))

            if (
                self.current_token.type == lexer.TT_KEYWORD
                and self.current_token.value == "at"
            ):
                self.advance()

                if self.current_token.type != lexer.TT_INT:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected int",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )

                index = self.current_token
                res.register_advance()
                self.advance()

                if not self.current_token.matches(lexer.TT_KEYWORD, "is"):
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected 'is'",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )
                self.advance()

                expression = res.register(self.expr(True))
                self.advance()
                return res.success(ArrayVariable(temp, index, expression))

            if self.current_token.type == lexer.TT_LBRACKET:
                self.advance()

                if self.current_token.type != lexer.TT_INT:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected int",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )

                index = self.current_token
                res.register_advance()
                self.advance()

                if self.current_token.type != lexer.TT_RBRACKET:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected ']'",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )

                res.register_advance()
                self.advance()
                if not self.current_token.matches(lexer.TT_KEYWORD, "is"):
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected 'is'",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )
                self.advance()
                expression = res.register(self.expr(True))
                self.advance()
                return res.success(ArrayVariable(temp, index, expression))

            if not self.current_token.matches(lexer.TT_KEYWORD, "is"):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected 'is'",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )

            variable = temp

            res.register_advance()
            self.advance()

            if self.current_token.type == lexer.TT_IDENTIFIER:
                function_name = self.current_token
                if self.tokens[self.index + 1].type == lexer.TT_LP:
                    self.advance()
                    parameters = []
                    if function_name.value not in self.functionNames:
                        return res.failure(
                            lexer.InvalidSyntaxError(
                                f"Function Name {function_name.value} not defined",
                                function_name.start,
                                function_name.end,
                            )
                        )
                    self.advance()
                    while self.current_token.type != lexer.TT_RP:
                        if self.current_token.type == lexer.TT_NEWLINE:
                            res.failure(
                                lexer.InvalidSyntaxError(
                                    "Expected )", function_name.start, function_name.end
                                )
                            )
                        if self.current_token.type == lexer.TT_IDENTIFIER:
                            if self.current_token.value not in self.variables:
                                return res.failure(
                                    lexer.InvalidSyntaxError(
                                        f"Variable  Name {self.current_token.value} not defined",
                                        self.current_token.start,
                                        self.current_token.end,
                                    )
                                )

                        parameters.append(self.current_token.value)

                        self.advance()

                        self.skip_commas(res)

                    self.advance()
                    res.register_advance()
                    self.variables.append(variable.value)
                    return res.success(
                        VariableFunctionNode(
                            variable,
                            FunctionCallNode(
                                function_name.value, function_name, parameters
                            ),
                        )
                    )

                if self.tokens[self.index + 1].type == lexer.TT_STOP:
                    variable = temp
                    class_name = self.current_token.value
                    if self.current_token.value not in self.variables:
                        return res.failure(
                            lexer.InvalidSyntaxError(
                                f"Variable name {self.current_token.value} not defined",
                                self.current_token.start,
                                self.current_token.end,
                            )
                        )
                    self.advance()
                    self.advance()
                    if self.current_token.type == lexer.TT_IDENTIFIER:
                        self.is_class = True
                        function = res.register(self.expr(True))
                        self.advance()
                        return VariableClassFunctionNode(variable, class_name, function)

            if (
                self.current_token.type == lexer.TT_KEYWORD
                and self.current_token.value == "arrange"
            ):
                self.advance()

                expression = res.register(self.expr(True))
                if res.error:
                    return res
                self.variables.append(variable.value)
                arrange_ascending = True
                if (
                    self.current_token.type == lexer.TT_KEYWORD
                    and self.current_token.value == "in"
                ):
                    self.advance()
                    if (
                        self.current_token.type == lexer.TT_KEYWORD
                        and self.current_token.value == "descending"
                    ):
                        arrange_ascending = False
                        self.advance()
                    else:
                        return res.failure(
                            lexer.InvalidSyntaxError(
                                "Expected 'descending'",
                                self.current_token.start,
                                self.current_token.end,
                            )
                        )
                return res.success(
                    ArrayArrangeNode(
                        variable, expression.variable_name, arrange_ascending
                    )
                )

            if self.current_token.type in (
                lexer.TT_STRING,
                lexer.TT_INT,
                lexer.TT_DOUBLE,
                lexer.TT_BOOL,
                lexer.TT_IDENTIFIER,
            ):
                if self.tokens[self.index + 1].type in (
                    lexer.TT_STRING,
                    lexer.TT_INT,
                    lexer.TT_DOUBLE,
                    lexer.TT_BOOL,
                    lexer.TT_IDENTIFIER,
                ):
                    dictorary = {}

                    while self.current_token.type != lexer.TT_NEWLINE:
                        key = self.current_token
                        self.advance()
                        value = self.current_token
                        self.advance()
                        self.skip_commas(res)
                        if key in dictorary:
                            return res.failure(
                                lexer.InvalidSyntaxError(
                                    "Duplicated key", key.start, key.end
                                )
                            )
                        dictorary[key.value] = value.value

                    self.variables.append(variable.value)
                    self.advance()
                    return res.success(DictNode(variable, dictorary))
                pass

            # accessing dict
            if self.current_token.type == lexer.TT_IDENTIFIER:
                key = self.current_token
                if (
                    self.tokens[self.index + 1].type == lexer.TT_KEYWORD
                    and self.tokens[self.index + 1].value == "of"
                ):
                    self.advance()
                    self.advance()
                    expression = res.register(self.expr(True))
                    if res.error:
                        return res

                    self.advance()
                    self.variables.append(variable.value)

                    return res.success(
                        AccessDictNode(variable, key, expression.variable_name)
                    )

            if (
                self.current_token.type == lexer.TT_KEYWORD
                and self.current_token.value == "length"
            ):
                self.advance()
                if (
                    self.current_token.type != lexer.TT_KEYWORD
                    and self.current_token.value != "of"
                ):
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected 'of'",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )
                self.advance()

                expression = res.register(self.expr(True))

                if res.error:
                    return res

                self.variables.append(variable.value)
                return res.success(ArrayLengthNode(variable, expression.variable_name))

            if self.current_token.type == lexer.TT_IDENTIFIER:
                identifier = self.current_token
                if identifier.value in self.classNames:
                    self.advance()
                    variables = []
                    if self.current_token.value == "with":
                        self.advance()
                        while self.current_token.type != lexer.TT_NEWLINE:
                            if (
                                self.current_token.type == lexer.TT_COMMA
                                or self.current_token.type == lexer.TT_STRING
                            ):
                                self.advance()
                            variables.append(self.current_token)
                            self.advance()
                    self.variables.append(variable.value)
                    return res.success(ClassAssignNode(variable, identifier, variables))

            expression = res.register(self.expr(True))

            if (
                self.current_token.type == lexer.TT_KEYWORD
                and self.current_token.value == "at"
            ):
                self.advance()
                if self.current_token.type != lexer.TT_INT:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected index",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )
                index = self.current_token
                self.advance()
                self.variables.append(variable.value)
                return res.success(
                    ArrayAccessNode(variable, index, expression.variable_name.value)
                )

            if self.current_token.type == lexer.TT_LBRACKET:
                self.advance()
                if self.current_token.type != lexer.TT_INT:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected index",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )
                index = self.current_token
                self.advance()

                if self.current_token.type != lexer.TT_RBRACKET:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected ']'",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )

                self.advance()
                self.variables.append(variable.value)
                return res.success(
                    ArrayAccessNode(variable, index, expression.variable_name.value)
                )

            if self.tokens[self.index].type == lexer.TT_COMMA:
                array = []
                self.advance()
                array.append(expression.token.value)
                while (
                    self.current_token.type != lexer.TT_EOF
                    and self.current_token.type != lexer.TT_NEWLINE
                ):
                    if self.current_token.type == lexer.TT_COMMA:
                        self.advance()
                        continue
                    array.append(self.current_token.value)
                    self.advance()
                self.variables.append(variable.value)
                return res.success(ArrayNode(variable, array))
            if res.error:
                return res
            self.variables.append(variable.value)
            return res.success(VariableNode(variable, expression))

        # if self.current_token.type == lexer.TT_STOP:
        #     self.advance()
        #     if self.current_token.type == lexer.TT_IDENTIFIER:
        #         identifier = res.register(self.expr(True))
        #         if res.error : return res
        #         self.advance()
        #         return ClassAccessNode(temp , identifier.variable_name)

        if self.current_token.type == lexer.TT_IDENTIFIER:
            variable = temp
            function_name = self.current_token
            if self.tokens[self.index + 1].type == lexer.TT_LP:
                self.advance()
                parameters = []
                if self.is_class:
                    if function_name.value not in self.classFunctionNames:
                        return res.failure(
                            lexer.InvalidSyntaxError(
                                f"-- Function Name {function_name.value} not defined",
                                function_name.start,
                                function_name.end,
                            )
                        )
                else:
                    if function_name.value not in self.functionNames:
                        return res.failure(
                            lexer.InvalidSyntaxError(
                                f"-- Function Name {function_name.value} not defined",
                                function_name.start,
                                function_name.end,
                            )
                        )
                self.advance()
                while self.current_token.type != lexer.TT_RP:
                    if self.current_token.type == lexer.TT_NEWLINE:
                        res.failure(
                            lexer.InvalidSyntaxError(
                                "Expected )", function_name.start, function_name.end
                            )
                        )

                    if self.current_token.type == lexer.TT_IDENTIFIER:
                        if self.current_token.value not in self.variables:
                            return res.failure(
                                lexer.InvalidSyntaxError(
                                    f"Variable Name {function_name.value} not defined",
                                    function_name.start,
                                    function_name.end,
                                )
                            )

                    parameters.append(self.current_token.value)

                    self.advance()

                    self.skip_commas(res)

                self.advance()
                res.register_advance()

                self.variables.append(variable.value)
                if self.is_class == True:
                    self.is_class = False
                    return res.success(
                        FunctionCallNode(function_name.value, function_name, parameters)
                    )
                else:
                    return res.success(
                        VariableFunctionNode(
                            variable,
                            FunctionCallNode(
                                function_name.value, function_name, parameters
                            ),
                        )
                    )
            if self.tokens[self.index + 1].type == lexer.TT_STOP:
                class_name = self.current_token
                if self.current_token.value not in self.variables:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            f"Variable name {self.current_token.value} not defined",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )
                self.advance()
                self.advance()
                if self.current_token.type == lexer.TT_IDENTIFIER:
                    self.is_class = True
                    function = res.register(self.expr(True))
                    return ClassAccessNode(class_name, function)

        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "if"
        ):
            res.register_advance()
            self.advance()

            condition_expression = res.register(self.expr(True))
            if res.error:
                return res

            if not self.current_token.matches(lexer.TT_KEYWORD, "then"):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected 'then'",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )

            res.register_advance()
            self.advance()

            self.skip_newlines(res)

            then_expr = []
            while self.current_token.type != lexer.TT_EOF:
                if (
                    self.current_token.type == lexer.TT_KEYWORD
                    and self.current_token.value in ["otherwise", "."]
                ):
                    break

                stmt = res.register(self.expr())
                if res.error:
                    return res
                then_expr.append(stmt)

                self.skip_newlines(res)

            if (
                self.current_token.type == lexer.TT_KEYWORD
                and self.current_token.value == "otherwise"
            ):
                res.register_advance()
                self.advance()

                self.skip_newlines(res)

                else_expr = []
                while self.current_token.type != lexer.TT_EOF:
                    if (
                        self.current_token.type == lexer.TT_STOP
                        and self.current_token.value == "."
                    ):
                        break

                    stmt = res.register(self.expr())
                    if res.error:
                        return res
                    else_expr.append(stmt)

                    self.skip_newlines(res)
                if (
                    self.current_token.type != lexer.TT_STOP
                    or self.current_token.value != "."
                ):
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected '.'",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )

                res.register_advance()
                self.advance()

                return res.success(IfNode(condition_expression, then_expr, else_expr))
            else:
                else_expr = None
        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "try"
        ):
            res.register_advance()
            self.advance()

            self.skip_newlines(res)

            then_expr = []
            while self.current_token.type != lexer.TT_EOF:
                if (
                    self.current_token.type == lexer.TT_KEYWORD
                    and self.current_token.value in ["oops", "."]
                ):
                    break

                stmt = res.register(self.expr())
                if res.error:
                    return res
                then_expr.append(stmt)

                self.skip_newlines(res)

            if (
                self.current_token.type == lexer.TT_KEYWORD
                and self.current_token.value == "oops"
            ):
                res.register_advance()
                self.advance()

                self.skip_newlines(res)

                else_expr = []
                while self.current_token.type != lexer.TT_EOF:
                    if (
                        self.current_token.type == lexer.TT_STOP
                        and self.current_token.value == "."
                    ):
                        break

                    stmt = res.register(self.expr())
                    if res.error:
                        return res
                    else_expr.append(stmt)

                    self.skip_newlines(res)
                if (
                    self.current_token.type != lexer.TT_STOP
                    or self.current_token.value != "."
                ):
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected '.'",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )

                res.register_advance()
                self.advance()

                return res.success(TryNode(then_expr, else_expr))
            else:
                else_expr = None

            if (
                self.current_token.type == lexer.TT_KEYWORD
                and self.current_token.value == "call"
            ):
                res.register_advance()
                self.advance()

                contract_name = self.current_token

                if contract_name not in self.variables:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected contract name to be defined ",
                            contract_name.start,
                            contract_name.end,
                        )
                    )
                res.register_advance()
                self.advance()
                parameters = []

                if self.current_token.type == lexer.TT_LP:

                    self.advance()
                    while self.current_token.type != lexer.TT_RP:
                        if self.current_token.type == lexer.TT_NEWLINE:
                            res.failure(
                                lexer.InvalidSyntaxError(
                                    "Expected )", contract_name.start, contract_name.end
                                )
                            )
                        if self.current_token.type == lexer.TT_IDENTIFIER:
                            if self.current_token.value not in self.variables:
                                return res.failure(
                                    lexer.InvalidSyntaxError(
                                        f"Variable  Name {contract_name.value} not defined",
                                        contract_name.start,
                                        contract_name.end,
                                    )
                                )
                        parameters.append(self.current_token.value)

                        self.advance()

                        self.skip_commas(res)

                    self.advance()
                    res.register_advance()
                return res.success(CallContractNode(contract_name, parameters))
        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "contract"
        ):
            res.register_advance()
            self.advance()
            name = self.current_token

            res.register_advance()
            self.advance()
            variables = []

            if self.current_token.value == "with":
                self.advance()
                while self.current_token.value != "does":
                    if self.current_token.type != lexer.TT_IDENTIFIER:
                        return res.failure(
                            lexer.InvalidSyntaxError(
                                f"Expected Identifier not {self.current_token.type} "
                            )
                        )
                    variable = self.current_token.value
                    variables.append(variable)
                    self.variables.append(variable)

                    self.advance()

                    if self.current_token.type == lexer.TT_COMMA:
                        self.advance()
            if self.current_token.value == "does":
                res.register_advance()
                self.advance()
                contract_body = []

                while self.current_token.type != lexer.TT_STOP:
                    self.skip_newlines(res)
                    expr = res.register(self.expr())
                    if res.error:
                        return res
                    contract_body.append(expr)
                    self.skip_newlines(res)
                res.register_advance()  # Consume the STOP token
                self.advance()
                return res.success(ContractNode(name, contract_body, variables))
            return res.success(ContractNode(name, [], variables))

        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "create"
        ):
            res.register_advance()
            self.advance()

            class_name = self.current_token.value

            res.register_advance()
            self.advance()
            variable = []
            if (
                self.current_token.type == lexer.TT_KEYWORD
                and self.current_token.value == "with"
            ):
                self.advance()
                while self.current_token.type != lexer.TT_NEWLINE:
                    if self.current_token.type == lexer.TT_COMMA:
                        self.advance()
                    variable.append(self.current_token.value)
                    self.advance()

            self.skip_newlines(res)
            class_body = []
            self.is_class = True
            while (
                self.current_token.type != lexer.TT_EOF
                and self.current_token.type != lexer.TT_STOP
            ):
                self.skip_newlines(res)
                expr = res.register(self.expr())
                if res.error:
                    return res
                if expr != None:
                    class_body.append(expr)
            self.advance()
            self.classNames.append(class_name)
            self.is_class = False
            return res.success(ClassNode(class_name, class_body, variable))

        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "till"
        ):
            res.register_advance()
            self.advance()

            condition_expression = res.register(self.expr(True))
            if res.error:
                return res

            if not self.current_token.matches(lexer.TT_KEYWORD, "do"):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected 'do'",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )

            res.register_advance()
            self.advance()

            self.skip_newlines(res)

            then_expr = []
            while self.current_token.type != lexer.TT_EOF:
                if self.current_token.value == ".":
                    break

                stmt = res.register(self.expr())
                if res.error:
                    return res
                then_expr.append(stmt)

                self.skip_newlines(res)

            if (
                self.current_token.type != lexer.TT_STOP
                or self.current_token.value != "."
            ):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected '.'", self.current_token.start, self.current_token.end
                    )
                )

            res.register_advance()
            self.advance()

            return res.success(TillNode(condition_expression, then_expr))

        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "repeat"
        ):
            res.register_advance()
            self.advance()

            variable = self.current_token
            res.register_advance()
            self.advance()

            if not self.current_token.matches(lexer.TT_KEYWORD, "times"):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected 'times'",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )

            res.register_advance()
            self.advance()

            self.skip_newlines(res)

            then_expr = []
            while self.current_token.type != lexer.TT_EOF:
                if self.current_token.value == ".":
                    break

                stmt = res.register(self.expr())
                if res.error:
                    return res
                then_expr.append(stmt)

                self.skip_newlines(res)

            if (
                self.current_token.type != lexer.TT_STOP
                or self.current_token.value != "."
            ):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected '.'", self.current_token.start, self.current_token.end
                    )
                )

            res.register_advance()
            self.advance()

            return res.success(RepeatNode(variable, then_expr))

        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "Note"
        ):
            res.register_advance()
            self.advance()
            note = []
            while self.current_token.type != lexer.TT_STOP:
                self.advance()
                if self.current_token.type == lexer.TT_NEWLINE:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected '.' ",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )
                note.append(self.current_token)
            self.advance()
            return res.success(NoteNode(note))

        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "show"
        ):
            position_var = self.current_token

            res.register_advance()
            self.advance()
            if self.current_token.type != lexer.TT_LP:
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected '('", self.current_token.start, self.current_token.end
                    )
                )
            res.register_advance()
            self.advance()

            body = []

            while self.current_token.type != lexer.TT_RP:

                data = None
                if self.current_token.type == lexer.TT_STRING:
                    res.register_advance()
                    self.advance()
                    is_string = False
                    if self.current_token.type != lexer.TT_IDENTIFIER:
                        return res.failure(
                            lexer.InvalidSyntaxError(
                                "Expected identifier",
                                self.current_token.start,
                                self.current_token.end,
                            )
                        )
                    variable = ""
                    while self.current_token.type != lexer.TT_STRING:

                        variable += " " + str(self.current_token.value)
                        self.advance()
                    self.advance()
                    data = variable
                    body.append(data)

                if self.current_token.type == lexer.TT_IDENTIFIER:
                    expr = res.register(self.expr(True))
                    if res.error:
                        return res.error
                    # variable = self.current_token
                    # if variable.value not in self.variables:
                    #     return res.failure(lexer.InvalidSyntaxError(f"Variable not defined {variable}" , self.current_token.start, self.current_token.end))
                    data = expr
                    body.append(data)

                if (
                    self.current_token.type != lexer.TT_RP
                    and self.current_token.type != lexer.TT_COMMA
                ):
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected , ",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )

                if self.current_token.type != lexer.TT_RP:
                    self.advance()

                if self.current_token.type == lexer.TT_NEWLINE:
                    return res.failure(
                        lexer.InvalidSyntaxError(
                            "Expected ')'",
                            self.current_token.start,
                            self.current_token.end,
                        )
                    )
            res.register_advance()
            self.advance()
            return res.success(ShowNode(body, position_var))

            # if (self.current_token.type != lexer.TT_IDENTIFIER) and (self.current_token.type not in (lexer.TT_INT, lexer.TT_DOUBLE)):
            #     return res.failure(lexer.InvalidSyntaxError("Expected identifier", self.current_token.start, self.current_token.end))
            # variable = self.current_token
            # self.advance()

            # if self.current_token.type != lexer.TT_RP:
            #     return res.failure(lexer.InvalidSyntaxError("Expected ')'", self.current_token.start, self.current_token.end))

            # res.register_advance()
            # self.advance()
            # return res.success(ShowNode(variable, show_token, False))
        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "say"
        ):
            res.register_advance()
            self.advance()

            if self.current_token.type != lexer.TT_IDENTIFIER:
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected identifier ",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            variable = self.current_token
            self.advance()

            return res.success(ShowNode(variable))
        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "get"
        ):
            res.register_advance()
            self.advance()

            if (
                self.current_token.type != lexer.TT_KEYWORD
                and self.current_token.value != "picture"
            ):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected 'picture' ",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            res.register_advance()
            self.advance()

            if (
                self.current_token.type != lexer.TT_KEYWORD
                and self.current_token.value != "for"
            ):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected 'for' ",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            res.register_advance()
            self.advance()

            if self.current_token.type != lexer.TT_IDENTIFIER:
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected identifier ",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            variable = self.current_token
            if self.is_variable_defined():
                res.failure(
                    lexer.InvalidSyntaxError(
                        "Variable already defined ",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            res.register_advance()
            self.advance()

            return res.success(GetPictureNode(VariableNode(variable, None)))

        if (
            self.current_token.type == lexer.TT_KEYWORD
            and self.current_token.value == "Robo"
        ):
            res.register_advance()
            self.advance()

            if (
                self.current_token.type != lexer.TT_KEYWORD
                and self.current_token.value != "what"
            ):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected 'tell' ",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            res.register_advance()
            self.advance()

            if (
                self.current_token.type != lexer.TT_KEYWORD
                and self.current_token.value != "do"
            ):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected 'what' ",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            res.register_advance()
            self.advance()

            if (
                self.current_token.type != lexer.TT_KEYWORD
                and self.current_token.value != "you"
            ):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected 'is' ",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            res.register_advance()
            self.advance()
            if (
                self.current_token.type != lexer.TT_KEYWORD
                and self.current_token.value != "see"
            ):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected 'see' ",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            res.register_advance()
            self.advance()
            if (
                self.current_token.type != lexer.TT_KEYWORD
                and self.current_token.value != "in"
            ):
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected 'in' ",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            res.register_advance()
            self.advance()
            if self.current_token.type != lexer.TT_IDENTIFIER:
                return res.failure(
                    lexer.InvalidSyntaxError(
                        "Expected identifier ",
                        self.current_token.start,
                        self.current_token.end,
                    )
                )
            variable = self.current_token
            res.register_advance()
            self.advance()

            return res.success(ClassifyNode(variable=variable))
        if self.current_token.type == lexer.TT_KEYWORD:
            return self.current_token.value
        return self.bin_operation(
            self.term,
            (
                lexer.TT_ADD,
                lexer.TT_MINUS,
                lexer.TT_LT,
                lexer.TT_GT,
                lexer.TT_EQUAL,
                lexer.TT_NOT_EQUAL,
                lexer.TT_MOD,
                lexer.TT_POW,
            ),
        )

    def skip_newlines(self, res):
        while self.current_token.type == lexer.TT_NEWLINE:
            res.register_advance()
            self.advance()

    def skip_commas(self, res):
        while self.current_token.type == lexer.TT_COMMA:
            res.register_advance()
            self.advance()

    def is_variable_defined(self):
        if self.current_token.type == lexer.TT_IDENTIFIER:
            for i in self.variables:
                if i.value == self.current_token.value:
                    return True
            return False

    def isFunction(self):
        if self.tokens[self.index].type == lexer.TT_LP:
            if self.tokens[self.index + 1].type == lexer.TT_RP:
                self.advance()
                self.advance()
                self.advance()

                return True
            else:
                return False
        else:
            return False


def print_ast(node, indent=""):
    """
    Recursively print the AST in a hierarchical, readable format.

    Args:
    node: The current AST node
    indent: The current indentation level (string of spaces)
    """
    # Print the current node's type and any relevant attributes
    node_type = type(node).__name__
    print(f"{indent}{node_type}", end="")

    if hasattr(node, "value"):
        print(f": {node.value}", end="")
    elif hasattr(node, "token"):
        print(f": {node.token.type} '{node.token.value}'", end="")
    elif hasattr(node, "variable_name"):
        print(f": {node.variable_name}", end="")
    elif hasattr(node, "function_name"):
        print(f": {node.function_name}", end="")
    elif hasattr(node, "class_name"):
        print(f": {node.class_name}", end="")

    print()  # New line

    # Recursively print child nodes
    new_indent = indent + "  "
    if hasattr(node, "statements"):
        for stmt in node.statements:
            print_ast(stmt, new_indent)
    elif hasattr(node, "body"):
        for item in node.body:
            print_ast(item, new_indent)
    elif hasattr(node, "left"):
        print_ast(node.left, new_indent)
        print_ast(node.right, new_indent)
    elif hasattr(node, "condition_expr"):
        print(f"{new_indent}Condition:")
        print_ast(node.condition_expr, new_indent + "  ")
        print(f"{new_indent}Then:")
        for stmt in node.then_expr:
            print_ast(stmt, new_indent + "  ")
        if hasattr(node, "otherwise_expr") and node.otherwise_expr:
            print(f"{new_indent}Otherwise:")
            for stmt in node.otherwise_expr:
                print_ast(stmt, new_indent + "  ")
    elif hasattr(node, "value_node"):
        print_ast(node.value_node, new_indent)


def run(filename):

    tokens, error = lexer.generate(filename)
    if error == None:
        praser = Praser(tokens)
        ast = praser.parse()
        return ast.node, ast.error
    else:
        return None, error.print()
