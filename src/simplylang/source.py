from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SourceFile:
    """Source text plus filename metadata used by every language phase."""

    text: str
    filename: str = "<stdin>"

    @classmethod
    def from_path(cls, path: str) -> "SourceFile":
        with open(path, encoding="utf-8") as file:
            return cls(file.read(), path)

    def line_at(self, line: int) -> str:
        lines = self.text.splitlines()
        if 0 <= line < len(lines):
            return lines[line]
        return ""


@dataclass(frozen=True)
class Position:
    index: int
    line: int
    column: int


@dataclass(frozen=True)
class Span:
    source: SourceFile
    start: Position
    end: Position

    @classmethod
    def from_legacy(cls, start, end=None) -> "Span":
        end = end or getattr(start, "end", start)
        source = SourceFile(
            getattr(start, "text", ""), getattr(start, "filename", "<stdin>")
        )
        return cls(
            source=source,
            start=Position(start.index, start.line, start.column),
            end=Position(end.index, end.line, end.column),
        )
