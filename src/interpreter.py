import os
from typing import List

import lexer as Lex
import praser as Pr


class InterpreterResult:
    def __init__(self):
        self.value = None
        self.error = None

    def register(self, res):
        if res.error:
            self.error = res.error
        return res.value

    def success(self, value):
        self.value = value
        return self

    def failure(self, error):
        self.error = error
        return self


class SymbolTable:
    def __init__(self):
        self.symbols = {}
        self.parent = None

    def get(self, name):
        value = self.symbols.get(name)
        if value == None and self.parent:
            return self.parent.get(name)
        return value

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]


class Context:
    def __init__(self, display_name, parent=None, parent_entry_pos=None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table: List[SymbolTable]


class Number:
    def __init__(self, value):
        self.value = value
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    def add(self, other):
        if isinstance(other, Number):
            return (
                Number(self.value + other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end),
                None,
            )

    def minus(self, other):
        if isinstance(other, Number):
            return (
                Number(self.value - other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end),
                None,
            )

    def isLT(self, other):
        if isinstance(other, Number):
            return (
                Number(self.value < other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end),
                None,
            )

    def isEquall(self, other):
        if isinstance(other, Number):
            return (
                Number(self.value == other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end),
                None,
            )
        else:
            return None, Lex.IllegalOperationError(
                f" Cant compare Number with {type(other).__name__} ",
                self.pos_start,
                self.pos_end,
                self.context,
            )

    def isNotEquall(self, other):
        if isinstance(other, Number):
            return (
                Number(self.value != other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end),
                None,
            )

    def isGT(self, other):
        """
        This function is used to evaluate if the value of the current Number
        instance is greater than the value of the other Number instance.

        Parameters
        ----------
        other : Number
            The other Number instance to compare with.

        Returns
        -------
        Number, Error
            A Number instance with the result of the comparison and an Error
            instance if an error occurred during the comparison.

        """
        if isinstance(other, Number):
            # Create a new Number instance with the result of the comparison.
            # The value of the new Number instance is a boolean indicating if
            # the value of the current Number instance is greater than the value
            # of the other Number instance.
            comparison_result = Number(self.value > other.value)

            # Set the context of the new Number instance to the same context as
            # the current Number instance.
            comparison_result.set_context(self.context)

            # Set the position of the new Number instance to be the same as the
            # position of the current Number instance.
            comparison_result.set_pos(self.pos_start, other.pos_end)

            # Return the new Number instance and None (no error occurred).
            return comparison_result, None

    def mul(self, other):
        if isinstance(other, Number):
            return (
                Number(self.value * other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end),
                None,
            )

    def div(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, Lex.IllegalOperationError(
                    "Divide by zero", self.pos_start, other.pos_end, self.context
                )
            return (
                Number(self.value / other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end),
                None,
            )

    def mod(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, Lex.IllegalOperationError(
                    "Modulo by zero", self.pos_start, other.pos_end, self.context
                )
            return (
                Number(self.value % other.value)
                .set_context(self.context)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end)
            )
        else:
            print("the instance is not number", type(other))
            return None

    def pow(self, other):
        if isinstance(other, Number):
            return (
                Number(self.value**other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end)
            )
        else:
            print("the instance is not number", type(other))
            return None

    def floor_div(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None
            return (
                Number(self.value // other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end)
            )
        else:
            return None

    def copy(self):
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __repr__(self) -> str:
        return str(self.value)


class Bool:
    def __init__(self, value):
        self.value = value
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    def isEquall(self, other):
        if isinstance(other, Bool):
            return (
                Bool(self.value == other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end),
                None,
            )
        else:
            return None, Lex.IllegalOperationError(
                f"Can't compare bool with {type(other).__name__}",
                self.pos_start,
                self.pos_end,
                self.context,
            )

    def isNotEquall(self, other):
        if isinstance(other, Bool):
            return (
                Bool(self.value != other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end),
                None,
            )
        else:
            return None, Lex.IllegalOperationError(
                f"Can't compare bool with {type(other).__name__}",
                self.pos_start,
                self.pos_end,
                self.context,
            )

    def and_with(self, other):
        if isinstance(other, Bool):
            return (
                Bool(self.value and other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end),
                None,
            )
        else:
            return None, Lex.IllegalOperationError(
                f"Can't perform AND with {type(other).__name__}",
                self.pos_start,
                self.pos_end,
                self.context,
            )

    def or_with(self, other):
        if isinstance(other, Bool):
            return (
                Bool(self.value or other.value)
                .set_context(self.context)
                .set_pos(self.pos_start, other.pos_end),
                None,
            )
        else:
            return None, Lex.IllegalOperationError(
                f"Can't perform OR with {type(other).__name__}",
                self.pos_start,
                self.pos_end,
                self.context,
            )


class Interpreter:
    def __init__(self):
        self.function_list = []

    def visit(self, node, context, symbol_table: List[SymbolTable]):
        method_name = f"visit_{type(node).__name__}"
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context, symbol_table)

    def no_visit_method(self, node, context, symbol_table: List[SymbolTable]):
        raise Exception(f"No visit_{type(node).__name__} method defined")

    def visit_BoolNode(self, node, context, symbol_table: List[SymbolTable]):
        return InterpreterResult().success(
            Bool(node.token.value)
            .set_context(context)
            .set_pos(node.pos_start, node.pos_end)
        )

    def visit_NumberNode(self, node, context, symbol_table: List[SymbolTable]):
        return InterpreterResult().success(
            Number(node.token.value)
            .set_context(context)
            .set_pos(node.pos_start, node.pos_end)
        )

    def visit_UniaryOperatorNode(self, node, context, symbol_table: List[SymbolTable]):
        res = InterpreterResult()
        number = res.register(self.visit(node.node, context, symbol_table))
        if res.error:
            return res
        error = None
        if node.token.type == Lex.TT_MINUS:
            number, error = number.mul(Number(-1))
        if error:
            return res.failure(error)
        return res.success(number.set_pos(node.pos_start, node.pos_end))

    def visit_VariableAccessNode(
        self,
        node,
        context,
        symbol_table: List[SymbolTable],
    ):
        variable_name = node.variable_name.value
        value = self.getVariable(variable_name, symbol_table)

        if not value:
            return InterpreterResult().failure(
                Lex.InvalidSyntaxError(
                    f"'{variable_name}' is not defined", node.pos_start, node.pos_end
                )
            )
        try:
            value = value.copy().set_pos(node.pos_start, node.pos_end)
        except:
            value = value
        return InterpreterResult().success(value)

    def visit_VariableNode(
        self, node: Pr.VariableNode, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()
        var_name = node.variable_name.value
        value = res.register(self.visit(node.value_node, context, symbol_table))
        if res.error:
            return res
        self.setVariable(var_name, value, symbol_table)
        return res.success(value)

    def visit_VariableFunctionNode(
        self, node: Pr.VariableFunctionNode, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()
        var_name = node.variable_name.value
        if isinstance(node.value_node, Pr.FunctionCallNode):
            value = res.register(
                self.visit_FunctionCallNode(node.value_node, context, symbol_table)
            )
            if res.error:
                return res
            self.setVariable(var_name, value, symbol_table)
            return res.success(value)

    def visit_VariableClassFunctionNode(
        self,
        node: Pr.VariableClassFunctionNode,
        context,
        symbol_table: List[SymbolTable],
    ):
        res = InterpreterResult()
        var_name = node.variable_name.value
        class_name = node.class_name
        access_node = node.function

        isClass = self.getVariable(class_name, symbol_table)
        if isClass == None:
            return InterpreterResult().failure(
                Lex.InvalidSyntaxError(
                    f"'Class {class_name.value}' is not defined",
                    node.pos_start,
                    node.pos_end,
                )
            )

        class_symbol_table = SymbolTable()
        class_symbol_table.set("NULL", Number(0))
        for i in range(len(isClass[1])):
            key = class_name + "_" + isClass[1][i]
            value = self.getVariable(key, symbol_table)
            class_symbol_table.set(isClass[1][i], value)

        if class_symbol_table != None:
            symbol_tables = symbol_table + [class_symbol_table]
        for i in isClass[0]:
            if isinstance(access_node, Pr.FunctionCallNode):
                if i.function_name.value == access_node.function_name:
                    value = self.visit_FunctionClassNode(
                        access_node, i, context, symbol_tables
                    )
                    self.setVariable(var_name, value.value, symbol_table)

            elif isinstance(i, Pr.FunctionNode):
                if i.function_name.value == access_node.variable_name.value:
                    value = self.visit_FunctionClassNode(
                        access_node, i, context, symbol_tables
                    )
                    self.setVariable(var_name, value.value, symbol_table)

        # for i in isClass[0]:
        #     if isinstance(i , Pr.FunctionNode):
        #         if i.function_name.value == function_name:
        #             value = self.visit_FunctionClassNode( i , node.function , context , symbol_tables)
        return res.success(value)

    def setVariable(self, variable, value, symbol_table):
        # print(f"setting variable {variable} with value {value} in symbol table {symbol_table[-1]}")
        symbol_table[-1].set(variable, value)

    def visit_ArrayLengthNode(
        self, node: Pr.ArrayLengthNode, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()

        variable = node.variable.value
        array_var = node.expression.value

        array = self.getVariable(array_var, symbol_table)
        if not array:
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"'{array_var}' is not defined", node.pos_start, node.pos_end
                )
            )
        if not isinstance(array, list):
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"'{array_var}' is not an array", node.pos_start, node.pos_end
                )
            )

        length = len(array)
        self.setVariable(variable, length, symbol_table)

        return res.success(length)

    def visit_StopNode(
        self, node: Pr.StopNode, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()
        if node.string:
            print(node.string.strip())
        exit()
        return res.success(None)

    def visit_ArrayArrangeNode(
        self, node: Pr.ArrayArrangeNode, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()
        var_name = node.variable_name.value
        array_var = node.array.value
        is_ascending = node.type

        array = self.getVariable(array_var, symbol_table)

        if not array:
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"'{array_var}' is not defined", node.pos_start, node.pos_end
                )
            )
        if not isinstance(array, list):
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"'{array_var}' is not an array", node.pos_start, node.pos_end
                )
            )
        if is_ascending:
            array.sort()
        else:
            array.sort(reverse=True)
        self.setVariable(var_name, array, symbol_table)
        return res.success(array)

    def visit_ArrayVariable(
        self, node: Pr.ArrayVariable, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()
        array_var_name = node.variable.value
        index = node.index.value

        expression_value = None
        if type(node.expression) == Pr.NumberNode:
            expression_value = node.expression.token.value
        else:
            expression_value = res.register(
                self.visit(node.expression.variable_name, context, symbol_table)
            )
            if res.error:
                return res

        value = self.getVariable(array_var_name, symbol_table)
        if not value:
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"'{array_var_name}' is not defined", node.pos_start, node.pos_end
                )
            )
        if not isinstance(value, list):
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"'{array_var_name}' is not an array", node.pos_start, node.pos_end
                )
            )
        if index < 0 or index >= len(value):
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"Index out of range", node.pos_start, node.pos_end
                )
            )

        value[index] = expression_value
        self.setVariable(array_var_name, value, symbol_table)

        return res.success(value)

    def visit_ArrayNode(self, node, context, symbol_table: List[SymbolTable]):
        res = InterpreterResult()
        var_name = node.variable_name.value
        value = node.value_node
        if res.error:
            return res
        self.setVariable(var_name, value, symbol_table)
        return res.success(value)

    def visit_ArrayAccessNode(
        self, node: Pr.ArrayAccessNode, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()

        array_name = node.access_variable
        target_var = node.variable_name.value
        index = node.value_node.value

        array = self.getVariable(array_name, symbol_table)
        if not array:
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"'{array_name}' is not defined", node.pos_start, node.pos_end
                )
            )

        if not isinstance(array, list):
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"'{array_name}' is not an array", node.pos_start, node.pos_end
                )
            )

        if index < 0 or index >= len(array):
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"Index {index} out of bounds for array '{array_name}'",
                    node.pos_start,
                    node.pos_end,
                )
            )

        value = array[index]

        # Store in target variable
        self.setVariable(target_var, Number(value), symbol_table)

        return res.success(Number(value))

    def visit_ShowNode(self, node, context, symbol_table: List[SymbolTable]):
        for statement in node.body:
            # Directly print supported data types
            if isinstance(statement, (int, str, bool, float)):
                print(str(statement).strip(), end=" ")
            elif isinstance(statement, Pr.VariableAccessNode):
                # Retrieve variable value
                value = self.getVariable(statement.variable_name.value, symbol_table)
                if value is None:  # Check for undefined variable
                    return InterpreterResult().failure(
                        Lex.InvalidSyntaxError(
                            f"'{statement.variable_name.value}' is not defined",
                            node.pos_start,
                            node.pos_end,
                        )
                    )
                # Print list values
                if isinstance(value, list):
                    print(" ".join(map(str, value)), end=" ")
                else:
                    print(value, end=" ")
            else:
                # Visit the statement and handle result
                result = self.visit(statement, context, symbol_table)
                if result and result.value is not None:  # Avoid printing None
                    if isinstance(result.value, Bool):
                        print(str(result.value.value).strip(), end=" ")
                    else:
                        print(result.value, end=" ")
        print()  # Ensure newline after printing all statements
        return InterpreterResult().success("success")

    def visit_AccessDictNode(
        self, node: Pr.AccessDictNode, context, symbol_table: List[SymbolTable]
    ):

        res = InterpreterResult()

        variable = node.variable.value
        key = node.key.value
        dict_name = node.dict.value

        dict = self.getVariable(dict_name, symbol_table)

        if dict == None:
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"'{dict_name}' is not defined", node.pos_start, node.pos_end
                )
            )
        elif key not in dict:
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"' No key {key} present in dictonary {dict_name} ' ",
                    node.pos_start,
                    node.pos_end,
                )
            )

        self.setVariable(variable, dict[key], symbol_table)

        return res.success(dict[key])

    def visit_ContractNode(self, node: Pr.ContractNode, context, symbol_table):
        res = InterpreterResult()
        self.setVariable(
            node.contract_name.value, [node.body, node.variables], symbol_table
        )
        return res.success(None)

    def visit_CallContractNode(self, node: Pr.CallContractNode, context, symbol_table):
        res = InterpreterResult()
        contract = self.getVariable(node.contract_name.value, symbol_table)
        if not contract:
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"'Contract {node.contract_name.value}' is not defined",
                    node.pos_start,
                    node.pos_end,
                )
            )

        contract_symbol_table = SymbolTable()
        contract_symbol_table.set("NULL", Number(0))
        if len(contract[1]) != len(node.parameters):
            return res.failure(
                Lex.InvalidSyntaxError(
                    f"Invalid number of parameters in Contract {node.contract_name}'",
                    node.pos_start,
                    node.pos_end,
                )
            )
        for i in range(len(contract[1])):
            value = self.getVariable(node.parameters[i], symbol_table)
            if value:
                contract_symbol_table.set(contract[1][i], value)
            else:
                contract_symbol_table.set(contract[1][i], node.parameters[i])
        if contract_symbol_table != None:
            symbol_tables = symbol_table + [contract_symbol_table]
        for i in contract[0]:
            value = res.register(self.visit(i, context, symbol_tables))
            if res.error:
                return res
        return res.success(value)

    def visit_UpdateDictNode(self, node: Pr.UpdateDictNode, context, symbol_table):
        res = InterpreterResult()
        key = node.key.value
        dict_name = node.dict
        value = node.expression
        if type(value) == Pr.VariableAccessNode:
            var_value = self.getVariable(value.variable_name.value, symbol_table)
            if var_value == None:
                return res.failure(
                    Lex.InvalidSyntaxError(
                        f"'{value.variable_name.value}' is not defined",
                        node.pos_start,
                        node.pos_end,
                    )
                )

            dict_value = symbol_table[-1].get(dict_name)
            dict_value[key] = var_value

            self.setVariable(dict_name, dict_value, symbol_table)

            return res.success(dict_name)
        elif type(value) == Pr.NumberNode:
            dict_value = symbol_table[-1].get(dict_name)
            dict_value[key] = value.token.value

            self.setVariable(dict_name, dict_value, symbol_table)

            return res.success(dict_name)
        elif type(value) == str:
            dict_value = symbol_table[-1].get(dict_name)
            dict_value[key] = value

            self.setVariable(dict_name, dict_value, symbol_table)
            return res.success(dict_name)

        return res.failure(
            Lex.InvalidSyntaxError(f"'Invalid Error'", node.pos_start, node.pos_end)
        )

    def visit_DictNode(
        self, node: Pr.DictNode, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()
        dict_name = node.variable_name.value
        dict_body = node.dictronary
        self.setVariable(dict_name, dict_body, symbol_table)

        return res.success(dict_body)

    def visit_ClassNode(self, node, context, symbol_table: List[SymbolTable]):
        res = InterpreterResult()
        class_name = node.class_name
        class_body = node.body
        class_variables = node.variable

        if res.error:
            return res
        self.setVariable(class_name, [class_body, class_variables], symbol_table)

        for b in class_body:
            if b == Pr.FunctionNode:
                value = res.success(self.visit(b, context, symbol_table))
        return res.success(class_body)

    def visit_ClassAssignNode(
        self, node: Pr.ClassAssignNode, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()
        class_value = self.getVariable(node.value_node, symbol_table)
        if node.variables:
            if not class_value[1]:
                res.failure(
                    Lex.InvalidSyntaxError(
                        f"'paramters are not defined in '{node.class_name}'",
                        node.pos_start,
                        node.pos_end,
                    )
                )
            for i in range(len(class_value[1])):
                key = node.class_name + "_" + class_value[1][i]
                if node.variables[i].type in (
                    Lex.TT_INT,
                    Lex.TT_DOUBLE,
                    Lex.TT_BOOL,
                    Lex.TT_STRING,
                ):
                    self.setVariable(key, node.variables[i].value, symbol_table)
                else:
                    value = self.getVariable(node.variables[i].value, symbol_table)
                    if value == None:
                        return res.failure(
                            Lex.InvalidSyntaxError(
                                f"'{node.variables[i].value}' is not defined",
                                node.pos_start,
                                node.pos_end,
                            )
                        )

                    self.setVariable(key, value, symbol_table)

        self.setVariable(node.class_name, class_value, symbol_table)
        return res.success(None)

    def visit_ClassAccessNode(
        self, node: Pr.ClassAccessNode, context, symbol_table: List[any]
    ):
        res = InterpreterResult()
        class_name = node.class_name
        access_node = node.access_node
        isClass = self.getVariable(class_name.value, symbol_table)
        if isClass == None:
            return InterpreterResult().failure(
                Lex.InvalidSyntaxError(
                    f"'Class {class_name.value}' is not defined",
                    node.pos_start,
                    node.pos_end,
                )
            )

        class_symbol_table = SymbolTable()
        class_symbol_table.set("NULL", Number(0))

        for i in range(len(isClass[1])):
            key = class_name.value + "_" + isClass[1][i]
            value = self.getVariable(key, symbol_table)
            class_symbol_table.set(isClass[1][i], value)

        if class_symbol_table != None:
            symbol_tables = symbol_table + [class_symbol_table]
        for i in isClass[0]:
            if isinstance(access_node, Pr.FunctionCallNode):
                if i.function_name.value == access_node.function_name:
                    value = self.visit_FunctionClassNode(
                        access_node, i, context, symbol_tables
                    )
            elif isinstance(i, Pr.FunctionNode):
                if i.function_name.value == access_node.variable_name.value:
                    value = self.visit_FunctionClassNode(
                        access_node, i, context, symbol_tables
                    )

        return res.success(value.value)

    def visit_StatementsNode(self, node, context, symbol_table: List[SymbolTable]):
        res = InterpreterResult()
        for statement in node.statements:
            value = res.register(self.visit(statement, context, [context.symbol_table]))
            if res.error:
                return res
        return res.success(value)

        # res = InterpreterResult()
        # value = self.getVariable(node.variable_name)
        # if not value:
        #     return InterpreterResult().failure( Lex.InvalidSyntaxError(f"'{node.variable_name}' is not defined" , node.pos_start , node.pos_end ) )
        # processed_image = self.load_and_preprocess_image(value)
        # predictions = self.predict_image(processed_image)
        # print(predictions[0])
        # return InterpreterResult().success( predictions )

    def visit_NoteNode(self, node, context, symbol_table: List[SymbolTable]):
        return InterpreterResult().success(node.note)

    def visit_IfNode(self, node, context, symbol_table: List[SymbolTable]):
        res = InterpreterResult()

        condition = res.register(self.visit(node.condition_expr, context, symbol_table))
        if res.error:
            return res

        if condition.value != 0:  # Assuming 0 is false, any other value is true
            expressions = node.then_expr
            for expr in expressions:
                value = res.register(self.visit(expr, context, symbol_table))
            if res.error:
                return res
        elif node.otherwise_expr:
            for expr in node.otherwise_expr:
                value = res.register(self.visit(expr, context, symbol_table))
                if res.error:
                    return res
        else:
            value = Number(0)  # Return a default value if there's no otherwise branch

        return res.success(value)

    def visit_TryNode(self, node, context, symbol_table: List[SymbolTable]):
        res = InterpreterResult()

        try:
            for expr in node.then_expr:
                value = self.visit(expr, context, symbol_table)
                if isinstance(value, InterpreterResult) and value.error:
                    raise Exception(value.error)
        except Exception as e:
            # If an error occurs in the try block, execute the catch block
            for expr in node.otherwise_expr:
                value = res.register(self.visit(expr, context, symbol_table))
                if res.error:
                    return res
        else:
            # If no exception occurred, the value from the try block is used
            res.value = value

        return res.success(res.value)

    def visit_TillNode(self, node, context, symbol_table: List[SymbolTable]):
        res = InterpreterResult()
        condition = res.register(self.visit(node.condition_expr, context, symbol_table))
        if res.error:
            return res
        while condition.value != 0:  # Assuming 0 is false, any other value is true
            for expr in node.body:
                value = res.register(self.visit(expr, context, symbol_table))
                if res.error:
                    return res
            condition = res.register(
                self.visit(node.condition_expr, context, symbol_table)
            )
        value = None
        return res.success(value)

    def visit_RepeatNode(self, node, context, symbol_table=None):
        res = InterpreterResult()
        for i in range(node.range):
            for expr in node.body:
                value = res.register(self.visit(expr, context, symbol_table))
                if res.error:
                    return res
        return res.success(value)

    def visit_FunctionNode(self, node, context, symbol_table: List[SymbolTable]):
        res = InterpreterResult()
        self.function_list.append(node)
        return res.success(None)

    def visit_ReturnNode(
        self, node: Pr.ReturnNode, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()
        token = node.token

        if token.type == Lex.TT_IDENTIFIER:
            value = self.getVariable(token.value, symbol_table)
            if value == None:
                return InterpreterResult().failure(
                    Lex.InvalidSyntaxError(
                        f"'{token.value}' is not defined", node.pos_start, node.pos_end
                    )
                )
            return res.success(value)
        else:
            return res.success(token)

    def visit_ReturnExprNode(
        self, node: Pr.ReturnExprNode, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()
        token = node.token

        value = res.register(self.visit(token, context, symbol_table))
        if res.error:
            return res
        else:
            if value == None:
                return InterpreterResult().failure(
                    Lex.InvalidSyntaxError(
                        f"'{token.value}' is not defined", node.pos_start, node.pos_end
                    )
                )
            return res.success(value)

    def getVariable(self, variable, symbol_tables: List[SymbolTable]):
        if symbol_tables != None:
            local_table = symbol_tables[::-1]
            for symbol_table in local_table:
                value = symbol_table.get(variable)
                if value:
                    return value

        return None

    def visit_FunctionCallNode(
        self, node: Pr.FunctionCallNode, context, symbol_table: List[SymbolTable]
    ):
        res = InterpreterResult()
        function = []
        function_symbol_table = SymbolTable()
        function_symbol_table.set("NULL", Number(0))
        for func in self.function_list:
            if func.function_name.value == node.function_name:
                function = func.body
                if func.variables != None:
                    if len(node.parameters) != len(func.variables):
                        return InterpreterResult().failure(
                            Lex.InvalidSyntaxError(
                                f"'Invalid number of parameters are passed in function {node.function_name}'",
                                node.pos_start,
                                node.pos_end,
                            )
                        )
                    for i in range(len(node.parameters)):
                        value = self.getVariable(node.parameters[i], symbol_table)
                        if value:
                            function_symbol_table.set(func.variables[i], value)
                        else:
                            function_symbol_table.set(
                                func.variables[i], node.parameters[i]
                            )

        has_return = False
        return_value = None

        for expr in function:
            value = res.register(
                self.visit(expr, context, symbol_table + [function_symbol_table])
            )
            if res.error:
                return res

            # Check if this is a return statement
            if isinstance(expr, (Pr.ReturnNode, Pr.ReturnExprNode)):
                has_return = True
                return_value = value
                break

        # If no return statement was found, return None
        if not has_return:
            return res.success(None)

        # If we had a return statement, return its value
        result = return_value
        if type(result) not in (int, str, bool, float):
            result = return_value.value
        return res.success(result)

    def visit_FunctionClassNode(
        self,
        node: Pr.FunctionCallNode,
        function: Pr.FunctionNode,
        context,
        symbol_table: List[SymbolTable],
    ):
        res = InterpreterResult()

        function_symbol_table = SymbolTable()
        function_symbol_table.set("NULL", Number(0))
        body = function.body

        if node.parameters != [] and function.variables != None:
            if len(node.parameters) != len(function.variables):
                return InterpreterResult().failure(
                    Lex.InvalidSyntaxError(
                        f"'Invalid number of parameters are passed in function {node.function_name}'",
                        node.pos_start,
                        node.pos_end,
                    )
                )
            for i in range(len(node.parameters)):
                value = self.getVariable(node.parameters[i], symbol_table)
                if value:
                    function_symbol_table.set(function.variables[i], value)
                else:
                    function_symbol_table.set(function.variables[i], node.parameters[i])

        has_return = False
        return_value = None

        for expr in body:
            value = res.register(
                self.visit(expr, context, symbol_table + [function_symbol_table])
            )
            if res.error:
                return res

            # Check if this is a return statement
            if isinstance(expr, (Pr.ReturnNode, Pr.ReturnExprNode)):
                has_return = True
                return_value = value
                break

        # If no return statement was found, return None
        if not has_return:
            return res.success(None)

        # Return the explicit return value if we had one
        return res.success(return_value)

    def visit_BinaryOperationNode(self, node, context, symbol_table):
        res = InterpreterResult()
        left = res.register(self.visit(node.left, context, symbol_table))
        if res.error:
            return res
        right = res.register(self.visit(node.right, context, symbol_table))
        if res.error:
            return res

        result = None
        error = None

        if isinstance(left, Bool) or isinstance(right, Bool):
            # Convert both operands to Bool if needed
            if not isinstance(left, Bool):
                left = Bool(bool(left.value if isinstance(left, Number) else left))
            if not isinstance(right, Bool):
                right = Bool(bool(right.value if isinstance(right, Number) else right))

            if node.token.type == Lex.TT_EQUAL:
                result, error = left.isEquall(right)
            elif node.token.type == Lex.TT_NOT_EQUAL:
                result, error = left.isNotEquall(right)
            else:
                return res.failure(
                    Lex.InvalidSyntaxError(
                        f"Invalid operator '{node.token.value}' for boolean values",
                        node.token.start,
                        node.token.end,
                    )
                )
        else:
            if not isinstance(left, Number):
                left = Number(left)
            if not isinstance(right, Number):
                right = Number(right)

            if node.token.type == Lex.TT_ADD:
                result, error = left.add(right)
            elif node.token.type == Lex.TT_MINUS:
                result, error = left.minus(right)
            elif node.token.type == Lex.TT_MUL:
                result, error = left.mul(right)
            elif node.token.type == Lex.TT_DIV:
                result, error = left.div(right)
            elif node.token.type == Lex.TT_LT:
                result, error = left.isLT(right)
            elif node.token.type == Lex.TT_POW:
                result, error = left.pow(right)
            elif node.token.type == Lex.TT_MOD:
                result, error == left.mod(right)
            elif node.token.type == Lex.TT_GT:
                result, error = left.isGT(right)
            elif node.token.type == Lex.TT_EQUAL:
                result, error = left.isEquall(right)
            elif node.token.type == Lex.TT_NOT_EQUAL:
                result, error = left.isNotEquall(right)
            else:
                return res.failure(
                    Lex.InvalidSyntaxError(
                        f"Invalid operator '{node.token.value}'",
                        node.token.start,
                        node.token.end,
                    )
                )

        if error:
            return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))


global_symbol_table = SymbolTable()

global_symbol_table.set("NULL", Number(0))


def run(filename):
    """
    Runs the interpreter on a given filename, returning the result value and any errors that occurred.

    Parameters:
        filename (str): The name of the file to run.

    Returns:
        tuple: A tuple containing the result value and any error that occurred.
    """
    context = Context("<program>")
    ast, error = Pr.run(filename)
    if error:
        return None, error
    interpreter = Interpreter()
    context.symbol_table = global_symbol_table
    if isinstance(ast, Pr.StatementsNode):
        result = interpreter.visit_StatementsNode(ast, context, [context.symbol_table])
    else:
        result = interpreter.visit(ast, context, [context.symbol_table])
    return result.value, result.error
