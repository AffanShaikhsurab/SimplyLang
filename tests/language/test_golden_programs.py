import subprocess
import sys
from pathlib import Path
import os


ROOT = Path(__file__).resolve().parents[2]


def normalize_output(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.strip().splitlines())


def run_simply(path: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src")
    return subprocess.run(
        [sys.executable, "-m", "simplylang.cli", str(path)],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def test_system_program_matches_golden_output():
    result = run_simply(ROOT / "tests" / "system" / "test.simply")
    expected = (ROOT / "tests" / "language" / "system.expected.stdout").read_text()

    assert result.returncode == 0
    assert result.stderr == ""
    assert normalize_output(result.stdout) == normalize_output(expected)


def test_example_program_matches_system_program():
    system_result = run_simply(ROOT / "tests" / "system" / "test.simply")
    example_result = run_simply(ROOT / "example" / "example.simply")

    assert example_result.returncode == 0
    assert example_result.stderr == ""
    assert normalize_output(example_result.stdout) == normalize_output(
        system_result.stdout
    )
