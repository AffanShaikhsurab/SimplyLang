# Future Bytecode/VM Evaluation

SimplyLang should keep the tree-walk interpreter as the production execution
model until the language spec, semantic resolver, tests, and runtime boundaries
are stable.

## Why Defer The VM

CPython, V8, SpiderMonkey, and TypeScript all benefit from intermediate
representations because their language semantics and test suites are mature.
SimplyLang is still stabilizing syntax, diagnostics, scope rules, classes,
contracts, and built-ins. Adding bytecode too early would duplicate unclear
semantics.

## Entry Criteria

Start VM implementation only when:

- Golden language tests cover all public syntax.
- Parser checks are mostly moved into `simplylang.semantic`.
- Runtime values and environments no longer depend on global mutable state.
- Developer commands can dump tokens, AST, semantic diagnostics, and runtime
  traces.
- Performance or tooling needs require a lower-level representation.

## Proposed First VM Shape

The first VM should be a small stack bytecode interpreter:

- `Chunk`: instructions plus constants table.
- `Instruction`: opcode, operand, and source line.
- `OpCode`: minimal instructions such as `CONSTANT`, `LOAD_NAME`, `STORE_NAME`,
  `CALL`, `RETURN`, and `POP`.
- `Compiler`: AST to bytecode lowering.
- `VM`: stack, frames, globals, built-ins, and diagnostics.
- `disassemble`: developer tool for bytecode debugging.

## Non-Goals

- No JIT.
- No optimizer tiers.
- No native code generation.
- No replacement of the current interpreter until behavior parity is proven by
  the same language test suite.
