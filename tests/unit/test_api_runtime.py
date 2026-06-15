from pathlib import Path

from simplylang.api import parse_source, run_file, run_source
from simplylang.semantic import resolve


ROOT = Path(__file__).resolve().parents[2]


def test_run_source_captures_stdout():
    result = run_source('show("hello")')

    assert result.exit_code == 0
    assert result.stdout.strip() == "hello"
    assert result.stderr == ""


def test_runs_do_not_leak_global_variables_between_calls():
    first = run_source("a is 1\nshow(a)")
    second = run_source("show(a)")

    assert first.exit_code == 0
    assert first.stdout.strip() == "1"
    assert second.exit_code == 1
    assert "'a' is not defined" in second.stderr


def test_semantic_resolver_reports_undefined_variable():
    parse_result = parse_source("show(missing)")
    semantic = resolve(parse_result.node)

    assert not semantic.ok
    assert semantic.diagnostics[0].code == "SL1001"


def test_run_file_exposes_semantic_result():
    result = run_file(str(ROOT / "tests" / "system" / "test.simply"))

    assert result.semantic is not None
    assert result.semantic.ok
