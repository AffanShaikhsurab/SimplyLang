# SimplyLang Children-First Roadmap

This roadmap turns SimplyLang into a first coding language for children ages
7-10. The goal is not to expose every programming feature early. The goal is for
a child to make something visible, playful, and personal within minutes.

## North Star

SimplyLang should feel like a creative coding playground:

- Children use simple words.
- A character, robot, turtle, or story world reacts immediately.
- Lessons are short missions.
- Errors feel like hints from a friendly coach.
- Text coding grows naturally from command cards and guided examples.

## Beginner Track

### Level 1: Words Make Things Happen

Concepts: output, simple commands, sequence.

Projects:

- Make Robo say hello.
- Make a character introduce itself.
- Change a color or background.

### Level 2: Repeats And Patterns

Concepts: `repeat`, counting, visual patterns.

Projects:

- Make Robo dance.
- Draw a square.
- Make a staircase.

### Level 3: Choices

Concepts: `if`, `otherwise`, obstacles, scores.

Projects:

- Guide Robo around a rock.
- Make a quiz answer.
- Change a pet mood.

### Level 4: Memory Boxes

Concepts: variables, score, names, health.

Projects:

- Score counter.
- Pet name badge.
- Tiny quiz game.

### Level 5: My Commands

Concepts: functions as reusable child-created commands.

Projects:

- `dance does ... .`
- `draw_square does ... .`
- `pet_trick does ... .`

## Advanced Track

Advanced features stay available, but should be labeled for older or returning
learners:

- Lists and dictionaries
- Functions with parameters
- Classes and contracts
- Error handling with `try/oops`
- Future bytecode/VM internals

## Website Experience

The website should prioritize:

1. Start Playing: a browser playground above the fold.
2. Learn: guided missions with one concept per mission.
3. Projects: remixable starter projects.
4. Parents: what children learn and how to support them.
5. Teachers: classroom activities and printable mission cards.
6. Docs: reference material for older learners and contributors.
7. Download: optional, after the browser path.

## Playground Requirements

The first browser playground can be a React-only simulator before a full
interpreter integration:

- Command cards append code snippets.
- Text mode lets children edit code.
- Visual world shows a robot/turtle moving on a grid.
- Feedback uses friendly coaching language.
- Missions show one persistent hint near the workspace.

## Child-Friendly Diagnostics

Diagnostics should translate technical errors into one clear next step.

Examples:

- Undefined name: “You used `score`, but we have not made a memory box called
  `score` yet. Try: `score is 0`.”
- Missing punctuation: “This block needs a closing `.` so SimplyLang knows where
  it ends.”
- Unknown command: “I do not know that word yet. Try one of the command cards.”

## Success Metrics

- First program runs in under 60 seconds.
- First mission can be completed without installation.
- Children can explain repeat, choice, and memory in their own words.
- Each lesson has a runnable example and a creative “make it yours” extension.
- Playground usage becomes the primary entry point before download.
