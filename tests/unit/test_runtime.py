from simplylang.runtime import Environment, FunctionValue, NumberValue


def test_environment_reads_parent_scope_and_keeps_zero_values():
    parent = Environment()
    parent.set("zero", NumberValue(0))
    child = Environment(parent=parent)

    assert child.get("zero") == NumberValue(0)
    assert child.get("missing") is None


def test_function_value_records_runtime_callable_shape():
    function = FunctionValue("add", ("a", "b"), ())

    assert function.name == "add"
    assert function.parameters == ("a", "b")
