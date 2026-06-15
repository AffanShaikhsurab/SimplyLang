# Visual World Runtime Plan

SimplyLang's current interpreter is text-first. For ages 7-10, the next major
language addition should be a small visual world runtime that can run in the
browser first and later in the CLI.

## First Runtime: Robo Grid

Start with a deterministic grid world:

- Fixed-size grid.
- One robot with position and direction.
- Optional star, wall, and goal tiles.
- Text output bubble for `show(...)` or future `say`.
- Step-by-step execution trace for teaching debugging.

## Beginner Commands

These commands should become the official visual beginner API:

```simply
say "Hello!"
move 1
turn right
turn left
wait 1
color purple
clear
```

Next commands after the basics:

```simply
when game starts
when clicked
background is "space"
add character "cat"
play sound "pop"
touching "star"
key pressed "space"
```

## Integration Approach

1. Prototype in the React playground with a tiny command interpreter.
2. Add parser tests for command-style syntax once the command set stabilizes.
3. Implement built-in runtime commands in `src/simplylang/runtime/`.
4. Route visual commands through a runtime interface instead of printing only to
   stdout.
5. Keep advanced features available, but avoid teaching them in early missions.

## Diagnostics

Visual runtime errors should be translated into coaching hints:

- Unknown command: “I do not know that word yet. Try a command card.”
- Missing number: “Move needs a number, like `move 1`.”
- Block not closed: “This repeat needs a closing `.`.”
- Out of bounds: “Robo reached the edge. Try turning first.”
