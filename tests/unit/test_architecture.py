import ast
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PACKAGE_ROOT = ROOT / "src" / "simplylang"
LEGACY_MODULES = {"lexer", "praser", "parser", "interpreter"}
ALLOWED_SRC_FILES = set()


def imported_roots(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    imports: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".", maxsplit=1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".", maxsplit=1)[0])
    return imports


def test_package_modules_do_not_import_legacy_top_level_modules():
    offenders = {}
    for path in PACKAGE_ROOT.rglob("*.py"):
        legacy_imports = imported_roots(path) & LEGACY_MODULES
        if legacy_imports:
            offenders[str(path.relative_to(ROOT))] = sorted(legacy_imports)

    assert offenders == {}


def test_src_root_contains_no_top_level_python_modules():
    top_level_modules = {
        path.name
        for path in (ROOT / "src").glob("*.py")
        if path.name not in ALLOWED_SRC_FILES
    }

    assert top_level_modules == set()
