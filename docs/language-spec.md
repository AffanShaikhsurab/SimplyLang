# SimplyLang Language Specification

This document is the implementation contract for SimplyLang. It records the
language behavior that tests and future refactors should preserve unless a
change is intentionally designed, documented, and covered by tests.

## Goals

SimplyLang is a beginner-friendly scripting language with natural-language
keywords. The implementation currently uses a Python tree-walk interpreter:

1. Source text is tokenized.
2. Tokens are parsed into an AST.
3. A semantic resolver checks names and calls.
4. The interpreter evaluates the AST with runtime environments and built-ins.

## Kid Core For Ages 7-10

The beginner learning track should use a deliberately small subset. This is the
part of SimplyLang that child-facing lessons, playground missions, and website
examples should teach first.

Core concepts:

- Say something: `show("Hello!")`
- Store a value: `name is "Robo"` or `score is 0`
- Do something more than once: `repeat 4 times`
- Make a choice: `if score > 5 then ... otherwise ... .`
- Count and change numbers: `score is score + 1`
- Create simple custom commands after the basics: `dance does ... .`

Beginner lessons should avoid dictionaries, classes, contracts, nested
functions, `try/oops`, `%`, `^`, and complex comparisons until learners are
comfortable with sequence, repeat, choice, and memory.

The website playground may also offer visual command cards such as `say`,
`move`, `turn`, `wait`, and `color`. Those are child-first learning commands for
the visual world. They should be treated as the next language evolution step and
documented with tests before becoming part of the core interpreter.

## Files

SimplyLang source files use the `.simply` extension. Tooling should treat the
extension case-insensitively for user convenience, but examples should use
lowercase `.simply`.

## Lexical Rules

Whitespace separates tokens. Newlines separate top-level statements. A period
`.` closes block constructs such as functions, loops, conditionals, classes,
contracts, and `try/oops` blocks.

Supported lexical categories:

- Integers: `10`
- Doubles: `10.5`
- Booleans: `true`, `false`
- Identifiers: ASCII letters, digits, `_`, and supported emoji characters
- Strings: text between double quotes, currently tokenized through quote
  delimiters for compatibility
- Operators: `+`, `-`, `*`, `/`, `%`, `^`, `<`, `>`, `equals`, `not equals`
- Delimiters: `(`, `)`, `[`, `]`, `,`, `.`, `:`

Comments use `Note` or `Note:` and continue until a terminating period.

## Keywords

Current reserved words include:

`show`, `is`, `if`, `then`, `otherwise`, `equals`, `till`, `do`, `try`, `oops`,
`get`, `Robo`, `repeat`, `times`, `say`, `create`, `with`, `at`, `arrange`,
`ascending`, `descending`, `length`, `of`, `stop`, `return`, `contract`, `call`.

The docs previously mentioned `and`, `or`, `<=`, and `>=`. Those are future
language features unless tests are added with implementation support.

## Statements

### Assignment

```simply
name is 10
result is name + 5
```

Assignment creates or updates a variable in the current environment.

### Output

```simply
show("value is", result)
```

`show` prints its arguments separated by spaces and appends a newline.

### Arrays

```simply
array is 1 , 2 , 4
element is array[0]
array[1] is 10
sorted is arrange array
descending_sorted is arrange array in descending
length_value is length of array
```

Array indexes are zero-based. Access outside the valid range is a runtime error.

### Dictionaries

```simply
dict is Name Affan , Age 20
name is Name of dict
Name of dict is "John Doe"
```

Dictionary keys are currently parsed from identifier-like tokens.

### Functions

```simply
add takes a , b does
    sum is a + b
    return sum
.

result is add(10 , 20)
show(add(1 , 2))
```

Functions may take parameters and return values. A call with the wrong number of
arguments is a semantic/runtime error.

### Control Flow

```simply
if a equals b then
    show("same")
otherwise
    show("different")
.
```

`if` evaluates the `then` branch when the condition is truthy, otherwise the
optional `otherwise` branch.

```simply
till a < b do
    show(a)
    a is a + 1
.
```

`till` repeats while its condition is truthy.

```simply
repeat 5 times
    show("again")
.
```

`repeat` executes its body a fixed number of times.

### Stop And Error Handling

```simply
stop with "message"
```

`stop` halts the program after printing its message.

```simply
try
    show("work")
oops
    show("fallback")
.
```

`try/oops` is the language error-handling construct. Runtime errors in `try`
execute the `oops` block. Program-level `stop` halts execution.

### Classes And Contracts

Classes and contracts are supported by the current interpreter, but their
surface syntax is still experimental. Existing tests should be expanded before
adding new behavior here.

## Expressions

Expressions support numeric arithmetic, comparison, parentheses, variables,
function calls, array access, dictionary access, and booleans.

Operator precedence currently follows the implementation:

1. Parentheses and primary values
2. Unary `+` and `-`
3. `*` and `/`
4. `+`, `-`, `<`, `>`, `equals`, `not equals`, `%`, `^`

This precedence should be revisited when the parser moves to a Pratt parser.

## Semantic Rules

The semantic resolver is responsible for:

- Duplicate definitions
- Undefined variables/functions/classes/contracts
- Function and contract arity
- Scope boundaries for functions/classes/contracts
- Invalid `return` or control-flow constructs

The legacy parser still performs some of these checks. New checks should be
added to `simplylang.semantic` first, then removed from the parser as part of
the parser refactor.

## Diagnostics

Diagnostics should include:

- Error kind
- Optional stable error code
- Message
- Filename, line, and column
- A code frame with a caret where possible

Runtime code should return diagnostics through the API/CLI, not call `exit()`
or write directly to stderr.

## Compatibility Policy

Current examples and golden tests define shipped behavior. Behavior changes
require updated examples, docs, and tests in the same change.
