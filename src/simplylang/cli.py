from __future__ import annotations

# pylint: disable=too-many-return-statements

import argparse
import sys
from pathlib import Path

from simplylang.api import lex_source, parse_source, run_file
from simplylang.parser import Parser, print_ast


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a SimplyLang file.")
    parser.add_argument("filename", help="The .simply file to run")
    parser.add_argument("--tokens", action="store_true", help="Print tokens and exit")
    parser.add_argument(
        "--ast", action="store_true", help="Print the parsed AST and exit"
    )
    parser.add_argument(
        "--trace",
        action="store_true",
        help="Reserved for future runtime tracing",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    filename = args.filename

    if not filename.lower().endswith(".simply"):
        print("Invalid file format, should be in .simply format", file=sys.stderr)
        return 2

    path = Path(filename)
    if not path.exists():
        print(f"File not found: {filename}", file=sys.stderr)
        return 2

    source = path.read_text(encoding="utf-8")

    if args.tokens:
        result = lex_source(source, filename)
        if result.diagnostic:
            print(result.diagnostic.render(), file=sys.stderr)
            return 1
        for token in result.tokens:
            print(token)
        return 0

    if args.ast:
        result = parse_source(source, filename)
        if result.diagnostic:
            print(result.diagnostic.render(), file=sys.stderr)
            return 1
        print_ast(result.node)
        return 0

    result = run_file(filename)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result.exit_code


__all__ = ["Parser", "main"]


if __name__ == "__main__":
    raise SystemExit(main())
