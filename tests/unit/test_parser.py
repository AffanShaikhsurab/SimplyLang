from simplylang import lexer, parser


def parse_source(source: str):
    tokens, lex_error = lexer.Lex(source, "<test>").create_token()
    assert lex_error is None
    result = parser.Parser(tokens).parse()
    assert result.error is None
    return result.node


def test_parses_variable_assignment_expression():
    ast = parse_source("answer is 40 + 2")

    assert isinstance(ast, parser.StatementsNode)
    assert len(ast.statements) == 1
    assignment = ast.statements[0]
    assert isinstance(assignment, parser.VariableNode)
    assert assignment.variable_name.value == "answer"
    assert isinstance(assignment.value_node, parser.BinaryOperationNode)


def test_parses_function_definition_and_call_assignment():
    ast = parse_source(
        "add takes a , b does\n"
        "sum is a + b\n"
        "return sum\n"
        ".\n"
        "result is add(1 , 2)"
    )

    assert isinstance(ast.statements[0], parser.FunctionNode)
    assert ast.statements[0].function_name.value == "add"
    assert ast.statements[0].variables == ["a", "b"]
    assert isinstance(ast.statements[1], parser.VariableFunctionNode)


def test_parser_rejects_missing_assignment_keyword():
    tokens, lex_error = lexer.Lex("answer 42", "<test>").create_token()
    assert lex_error is None

    result = parser.Parser(tokens).parse()

    assert isinstance(result.error, lexer.InvalidSyntaxError)
    assert "Expected 'is'" in result.error.msg
