"""Statement parsing boundary for the compatibility parser."""

from simplylang.parser import Parser


def parse_statement(parser: Parser):
    return parser.expr()
