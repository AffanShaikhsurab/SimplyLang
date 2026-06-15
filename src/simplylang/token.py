from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional

import simplylang.lexer as legacy_lexer

from simplylang.source import Span


class TokenType(str, Enum):
    INT = legacy_lexer.TT_INT
    DOUBLE = legacy_lexer.TT_DOUBLE
    ADD = legacy_lexer.TT_ADD
    MUL = legacy_lexer.TT_MUL
    DIV = legacy_lexer.TT_DIV
    BOOL = legacy_lexer.TT_BOOL
    MINUS = legacy_lexer.TT_MINUS
    LP = legacy_lexer.TT_LP
    RP = legacy_lexer.TT_RP
    STOP = legacy_lexer.TT_STOP
    EOF = legacy_lexer.TT_EOF
    POW = legacy_lexer.TT_POW
    MOD = legacy_lexer.TT_MOD
    LT = legacy_lexer.TT_LT
    GT = legacy_lexer.TT_GT
    COLON = legacy_lexer.TT_COLON
    STRING = legacy_lexer.TT_STRING
    NOT_EQUAL = legacy_lexer.TT_NOT_EQUAL
    LBRACKET = legacy_lexer.TT_LBRACKET
    RBRACKET = legacy_lexer.TT_RBRACKET
    NEWLINE = legacy_lexer.TT_NEWLINE
    IDENTIFIER = legacy_lexer.TT_IDENTIFIER
    EQ = legacy_lexer.TT_EQ
    KEYWORD = legacy_lexer.TT_KEYWORD
    EQUAL = legacy_lexer.TT_EQUAL
    COMMA = legacy_lexer.TT_COMMA


KEYWORDS = dict(legacy_lexer.KEYWORDS)


@dataclass(frozen=True)
class Token:
    type: TokenType | str
    lexeme: str
    literal: Any = None
    span: Optional[Span] = None

    @classmethod
    def from_legacy(cls, token: legacy_lexer.Token) -> "Token":
        try:
            token_type = TokenType(token.type)
        except ValueError:
            token_type = token.type
        value = token.value
        return cls(
            type=token_type,
            lexeme=str(value),
            literal=value,
            span=(
                Span.from_legacy(token.start, token.end)
                if hasattr(token, "start")
                else None
            ),
        )

    def to_legacy(self) -> legacy_lexer.Token:
        token_type = self.type.value if isinstance(self.type, TokenType) else self.type
        if self.span:
            start = legacy_lexer.Position(
                self.span.start.index,
                self.span.start.line,
                self.span.start.column,
                self.span.source.filename,
                self.span.source.text,
            )
            end = legacy_lexer.Position(
                self.span.end.index,
                self.span.end.line,
                self.span.end.column,
                self.span.source.filename,
                self.span.source.text,
            )
            return legacy_lexer.Token(token_type, self.literal, start, end)
        return legacy_lexer.Token(token_type, self.literal)
