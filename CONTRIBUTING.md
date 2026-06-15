# Contributing to Simple Language

Thank you for your interest in contributing to Simple Language! This document outlines the coding principles, architecture, and guidelines we follow in this project.

## Architecture Overview

Simple Language now follows an explicit language pipeline:

1. **Source and Diagnostics** (`simplylang/source.py`, `simplylang/diagnostics.py`)
2. **Lexical Analysis** (`simplylang/lexer.py`, `simplylang/token.py`)
3. **Parsing and AST** (`simplylang/parser/`, `simplylang/ast.py`)
4. **Semantic Resolution** (`simplylang/semantic/`)
5. **Runtime and Interpretation** (`simplylang/runtime/`, `simplylang/interpreter.py`)
6. **Public API and CLI** (`simplylang/api.py`, `simplylang/cli.py`)

All implementation code lives under `src/simplylang/`. The `src/` directory is
only the package root and should not contain top-level Python modules.

### Design Patterns

1. **Visitor Pattern**

   - Used in the interpreter for traversing the Abstract Syntax Tree (AST)
   - Implementation in `Interpreter` class with `visit_*` methods
2. **Object-Oriented Node Structure**

   - Each language construct is represented by a specific node class
   - Examples: `NumberNode`, `BinaryOperationNode`, `IfNode`, etc.
3. **Result Pattern**

   - Used throughout the codebase (`ParserResult`, `InterpreterResult`)
   - Encapsulates both success and error states

## Coding Principles

### 1. Error Handling

```python
class Error:
    def __init__(self, error_msg, error_type, start, end):
        self.msg = error_msg
        self.type = error_type
        self.start = start
        self.end = end
```

- Use descriptive error messages
- Include position information for error reporting
- Implement specific error types (IllegalCharError, InvalidSyntaxError, etc.)

### 2. Code Organization

- Clear separation of concerns between lexing, parsing, and interpretation
- Each phase has its own dedicated class
- Modular design for easy extension

### 3. Documentation

- Use docstrings for classes and complex methods
- Include parameter descriptions and return value information
- Document error conditions and edge cases

### 4. Naming Conventions

- Use descriptive names for classes and methods
- Follow Python naming conventions:
  - Classes: PascalCase (e.g., `NumberNode`, `Interpreter`)
  - Methods/Functions: snake_case (e.g., `create_number`, `visit_NumberNode`)
  - Constants: UPPER_CASE (e.g., `TT_INT`, `DIGITS`)

## Contributing Guidelines

### 1. Adding New Features

1. Update `docs/language-spec.md` with the intended syntax and semantics.
2. Add or update golden tests in `tests/language/` and focused unit tests in
   `tests/unit/`.
3. Add token changes in `simplylang/token.py` and lexer support in
   `simplylang/lexer.py` or the compatibility lexer.
4. Add AST/parser changes in `simplylang/ast.py` and `simplylang/parser/`.
5. Add name, arity, scope, or control-flow checks in `simplylang/semantic/`.
6. Add runtime values, environments, built-ins, or visitor behavior in
   `simplylang/runtime/` and `simplylang/interpreter.py`.
7. Expose user-facing behavior through `simplylang/api.py` and
   `simplylang/cli.py` when needed.

### 2. Testing

- Write test cases for new features
- Ensure backward compatibility
- Test error conditions and edge cases

### 3. Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Implement changes following the coding principles
4. Add tests and documentation
5. Submit a pull request

### 4. Code Review Criteria

- Adherence to coding principles
- Proper error handling
- Documentation quality
- Test coverage
- Performance considerations

## Development Setup

1. Clone the repository
2. Set up a Python development environment
3. Install any required dependencies
4. Run tests, linting, and formatting checks:
   ```bash
   pytest
   pylint src/simplylang tests
   black --check src tests
   ```
5. Run system tests:
   ```bash
   simplylang tests/system/test.simply
   # Source-tree development without installing:
   PYTHONPATH=src python -m simplylang.cli tests/system/test.simply
   ```

## Questions and Support

If you have questions about contributing, please:

1. Check existing documentation
2. Review open and closed issues
3. Contact the maintainers

## License

By contributing to Simple Language, you agree that your contributions will be licensed under the same license as the project (MIT License).
