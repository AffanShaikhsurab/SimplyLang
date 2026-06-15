from simplylang.api import parse_source
from simplylang.semantic import resolve


def semantic_for(source: str):
    parsed = parse_source(source)
    assert parsed.diagnostic is None
    return resolve(parsed.node)


def test_resolver_accepts_defined_variables_and_functions():
    result = semantic_for(
        "a is 1\n"
        "add takes x , y does\n"
        "sum is x + y\n"
        "return sum\n"
        ".\n"
        "total is add(a , 2)"
    )

    assert result.ok
    assert result.symbols["add"].arity == 2


def test_resolver_reports_wrong_function_arity():
    result = semantic_for("add takes x , y does\n" "return x\n" ".\n" "total is add(1)")

    assert not result.ok
    assert result.diagnostics[0].code == "SL1002"


def test_resolver_reports_return_outside_function():
    result = semantic_for("return 1")

    assert not result.ok
    assert result.diagnostics[0].code == "SL1004"
