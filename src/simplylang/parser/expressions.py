"""Expression parsing boundary.

The implementation delegates to the compatibility parser today. Keeping this
module separate gives operator parsing a focused home for the planned Pratt
parser migration.
"""

from simplylang.parser import Parser


def parse_expression(parser: Parser, seen: bool = True):
    return parser.expr(seen)
