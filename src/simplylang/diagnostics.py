from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from simplylang.source import Span


@dataclass(frozen=True)
class Diagnostic:
    """Structured error/warning that can be rendered by the CLI or tests."""

    message: str
    kind: str = "error"
    code: Optional[str] = None
    span: Optional[Span] = None

    def render(self) -> str:
        prefix = self.kind
        if self.code:
            prefix = f"{prefix}[{self.code}]"
        result = f"{prefix}: {self.message}"
        if not self.span:
            return result

        line = self.span.source.line_at(self.span.start.line)
        caret = " " * max(self.span.start.column, 0) + "^"
        location = (
            f"File {self.span.source.filename}, line {self.span.start.line + 1}, "
            f"column {self.span.start.column + 1}"
        )
        return f"{result}\n{location}\n{line}\n{caret}"


def from_legacy_error(error) -> Diagnostic:
    """Adapt existing lexer/parser/runtime errors into the new diagnostics shape."""

    span = None
    start = getattr(error, "start", None)
    if start is not None:
        span = Span.from_legacy(start, getattr(error, "end", None))
    return Diagnostic(
        message=getattr(error, "msg", str(error)),
        kind=getattr(error, "type", "error"),
        span=span,
    )
