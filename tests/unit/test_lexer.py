from simplylang import lexer


def token_values(source: str):
    tokens, error = lexer.Lex(source, "<test>").create_token()
    assert error is None
    return [(token.type, token.value) for token in tokens]


def test_lexes_numbers_identifiers_keywords_and_newlines():
    assert token_values("a is 10\nshow(a)") == [
        (lexer.TT_IDENTIFIER, "a"),
        (lexer.TT_KEYWORD, "is"),
        (lexer.TT_INT, 10),
        (lexer.TT_NEWLINE, lexer.TT_NEWLINE),
        (lexer.TT_KEYWORD, "show"),
        (lexer.TT_LP, "("),
        (lexer.TT_IDENTIFIER, "a"),
        (lexer.TT_RP, ")"),
        (lexer.TT_EOF, lexer.TT_EOF),
    ]


def test_lexes_string_delimiters_for_current_parser_contract():
    assert token_values('show("hello")') == [
        (lexer.TT_KEYWORD, "show"),
        (lexer.TT_LP, "("),
        (lexer.TT_STRING, "'"),
        (lexer.TT_IDENTIFIER, "hello"),
        (lexer.TT_STRING, "'"),
        (lexer.TT_RP, ")"),
        (lexer.TT_EOF, lexer.TT_EOF),
    ]


def test_reports_illegal_character_with_position():
    tokens, error = lexer.Lex("@", "<test>").create_token()

    assert tokens == []
    assert isinstance(error, lexer.IllegalCharError)
    assert error.start.line == 0
    assert error.start.column == 1
