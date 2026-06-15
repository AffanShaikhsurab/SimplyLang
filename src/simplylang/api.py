from __future__ import annotations

import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from simplylang.diagnostics import Diagnostic
from simplylang.interpreter import interpret_file
from simplylang.lexer import LexResult, lex_source as _lex_source
from simplylang.parser import ParseResult, parse_source as _parse_source
from simplylang.semantic import ResolveResult, resolve


@dataclass(frozen=True)
class RunResult:
    value: Any = None
    stdout: str = ""
    stderr: str = ""
    diagnostic: Optional[Diagnostic] = None
    exit_code: int = 0
    semantic: Optional[ResolveResult] = None

    @property
    def ok(self) -> bool:
        return self.exit_code == 0 and self.diagnostic is None


def lex_source(source: str, filename: str = "<stdin>") -> LexResult:
    return _lex_source(source, filename)


def parse_source(source: str, filename: str = "<stdin>") -> ParseResult:
    return _parse_source(source, filename)


def run_source(source: str, filename: str = "<stdin>") -> RunResult:
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", suffix=".simply", delete=False
    ) as file:
        file.write(source)
        temp_path = file.name

    try:
        return run_file(temp_path, display_filename=filename)
    finally:
        Path(temp_path).unlink(missing_ok=True)


def run_file(path: str, display_filename: str | None = None) -> RunResult:
    source = Path(path).read_text(encoding="utf-8")
    parse_result = parse_source(source, display_filename or path)
    semantic_result = None
    if parse_result.node is not None:
        semantic_result = resolve(parse_result.node)

    # Preserve current interpreter behavior while exposing semantic diagnostics
    # for tests/tools. The legacy parser still owns some validation today.
    interpreted = interpret_file(path)
    if interpreted.diagnostic:
        rendered = interpreted.diagnostic.render()
        return RunResult(
            value=interpreted.value,
            stdout=interpreted.stdout,
            stderr=rendered,
            diagnostic=interpreted.diagnostic,
            exit_code=1,
            semantic=semantic_result,
        )

    return RunResult(
        value=interpreted.value,
        stdout=interpreted.stdout,
        semantic=semantic_result,
    )
