import { useMemo, useState } from "react";
import { Bot, Play, RotateCw, Sparkles, Wand2 } from "lucide-react";
import SectionHeader from "./ui/SectionHeader.jsx";

const starterCode = `show("Hi, I am Robo!")
repeat 4 times
    move 1
    turn right
.`;

const commandCards = [
  { label: "Say hello", code: 'show("Hello, friends!")' },
  { label: "Move", code: "move 1" },
  { label: "Turn right", code: "turn right" },
  { label: "Repeat", code: "repeat 4 times\n    move 1\n    turn right\n." },
  { label: "Change color", code: "color purple" },
];

const directions = ["east", "south", "west", "north"];
const colorMap = {
  purple: "text-brand-700",
  blue: "text-blue-600",
  green: "text-emerald-600",
  pink: "text-pink-600",
  orange: "text-orange-500",
};

const clamp = (value) => Math.max(0, Math.min(4, value));

const cleanMessage = (line) => {
  const quoted = line.match(/["']([^"']*)["']/);
  if (quoted) return quoted[1];
  return line.replace(/^say\s+/i, "").trim();
};

const runLine = (line, state) => {
  const trimmed = line.trim();
  if (!trimmed || trimmed === ".") return state;

  if (trimmed.startsWith("show(") || trimmed.startsWith("say ")) {
    return {
      ...state,
      messages: [...state.messages, cleanMessage(trimmed)],
      trace: [...state.trace, "Robo said something out loud."],
    };
  }

  if (trimmed.startsWith("move")) {
    const amount = Number(trimmed.split(/\s+/)[1] || 1);
    const next = { ...state.position };
    if (state.direction === "east") next.x = clamp(next.x + amount);
    if (state.direction === "west") next.x = clamp(next.x - amount);
    if (state.direction === "south") next.y = clamp(next.y + amount);
    if (state.direction === "north") next.y = clamp(next.y - amount);
    return {
      ...state,
      position: next,
      trace: [...state.trace, `Robo moved ${amount} step${amount === 1 ? "" : "s"}.`],
    };
  }

  if (trimmed === "turn right" || trimmed === "turn left") {
    const currentIndex = directions.indexOf(state.direction);
    const offset = trimmed.endsWith("right") ? 1 : -1;
    const direction = directions[(currentIndex + offset + directions.length) % directions.length];
    return {
      ...state,
      direction,
      trace: [...state.trace, `Robo turned ${trimmed.endsWith("right") ? "right" : "left"}.`],
    };
  }

  if (trimmed.startsWith("color")) {
    const color = trimmed.split(/\s+/)[1] || "purple";
    return {
      ...state,
      color: colorMap[color] ? color : "purple",
      trace: [...state.trace, `Robo changed color to ${color}.`],
    };
  }

  return {
    ...state,
    hints: [
      ...state.hints,
      `I do not know "${trimmed}" yet. Try a command card like move, turn, or show.`,
    ],
  };
};

const runProgram = (code) => {
  const lines = code.split("\n");
  let state = {
    position: { x: 1, y: 1 },
    direction: "east",
    color: "purple",
    messages: [],
    trace: [],
    hints: [],
  };

  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index].trim();
    const repeatMatch = line.match(/^repeat\s+(\d+)\s+times$/i);

    if (repeatMatch) {
      const repeatLines = [];
      index += 1;
      while (index < lines.length && lines[index].trim() !== ".") {
        repeatLines.push(lines[index]);
        index += 1;
      }

      for (let count = 0; count < Number(repeatMatch[1]); count += 1) {
        repeatLines.forEach((repeatLine) => {
          state = runLine(repeatLine, state);
        });
      }
      state = {
        ...state,
        trace: [...state.trace, `The repeat block ran ${repeatMatch[1]} times.`],
      };
      continue;
    }

    state = runLine(line, state);
  }

  if (!state.messages.length && !state.trace.length) {
    state.hints.push("Try adding a command card, then press Run.");
  }

  return state;
};

const Playground = () => {
  const [code, setCode] = useState(starterCode);
  const [result, setResult] = useState(() => runProgram(starterCode));
  const rotation = useMemo(
    () => directions.indexOf(result.direction) * 90,
    [result.direction]
  );

  const appendCommand = (snippet) => {
    setCode((current) => `${current.trim()}\n${snippet}`);
  };

  return (
    <section id="play" className="section-shell bg-brand-50/60">
      <div className="section-container">
        <SectionHeader
          eyebrow="Start playing"
          title="Make Robo move with simple words"
          description="Pick a command card, press Run, and watch the little world change. This is the first step from playful commands to real text coding."
        />

        <div className="grid gap-6 lg:grid-cols-[220px_1fr_1fr]">
          <div className="card-surface !p-5">
            <div className="mb-4 flex items-center gap-2 font-bold text-ink">
              <Wand2 className="h-5 w-5 text-brand-700" />
              Command cards
            </div>
            <div className="space-y-2">
              {commandCards.map((card) => (
                <button
                  key={card.label}
                  type="button"
                  onClick={() => appendCommand(card.code)}
                  className="w-full rounded-xl bg-brand-100 px-4 py-3 text-left text-sm font-semibold text-brand-950 transition hover:bg-brand-200"
                >
                  {card.label}
                </button>
              ))}
            </div>
            <p className="mt-5 rounded-xl bg-amber-50 p-4 text-sm font-medium text-amber-950 ring-1 ring-amber-100">
              Mission hint: make Robo say hello, move, and turn in a pattern.
            </p>
          </div>

          <div className="code-window !border-slate-800 p-5">
            <div className="mb-3 flex items-center justify-between text-white">
              <span className="font-bold">Text mode</span>
              <button
                type="button"
                onClick={() => setResult(runProgram(code))}
                className="inline-flex items-center gap-2 rounded-full bg-emerald-400 px-5 py-2 text-sm font-bold text-emerald-950 transition hover:bg-emerald-300"
              >
                <Play className="h-4 w-4" />
                Run
              </button>
            </div>
            <textarea
              value={code}
              onChange={(event) => setCode(event.target.value)}
              className="h-80 w-full resize-none rounded-xl bg-slate-950 p-4 font-mono text-sm leading-6 text-emerald-100 outline-none ring-1 ring-white/10 focus:ring-2 focus:ring-emerald-400"
              spellCheck="false"
            />
          </div>

          <div className="card-surface">
            <div className="mb-4 flex items-center justify-between">
              <div className="flex items-center gap-2 font-bold text-ink">
                <Bot className="h-5 w-5 text-brand-700" />
                Robo world
              </div>
              <span className="badge-brand flex items-center gap-1">
                <RotateCw className="h-3 w-3" />
                {result.direction}
              </span>
            </div>

            <div className="relative h-80 overflow-hidden rounded-xl border border-brand-100 bg-[linear-gradient(#ede9fe_1px,transparent_1px),linear-gradient(90deg,#ede9fe_1px,transparent_1px)] bg-[size:20%_20%]">
              <div
                className={`absolute flex h-14 w-14 items-center justify-center rounded-xl bg-white shadow-card transition-all duration-500 ${colorMap[result.color]}`}
                style={{
                  left: `${result.position.x * 20 + 4}%`,
                  top: `${result.position.y * 20 + 4}%`,
                  transform: `rotate(${rotation}deg)`,
                }}
              >
                <Bot className="h-8 w-8" />
              </div>
              <div className="absolute bottom-4 right-4 rounded-full bg-amber-200 px-4 py-2 text-sm font-bold text-amber-900">
                Star
              </div>
            </div>

            <div className="mt-4 space-y-2">
              {result.messages.map((message, index) => (
                <div
                  key={`${message}-${index}`}
                  className="rounded-xl bg-sky-50 p-3 text-sm font-semibold text-sky-950 ring-1 ring-sky-100"
                >
                  Robo says: {message}
                </div>
              ))}
              {result.hints.map((hint) => (
                <div
                  key={hint}
                  className="rounded-xl bg-amber-50 p-3 text-sm font-semibold text-amber-950 ring-1 ring-amber-100"
                >
                  {hint}
                </div>
              ))}
              <div className="rounded-xl bg-slate-50 p-3 text-sm text-ink-muted ring-1 ring-slate-100">
                <div className="mb-1 flex items-center gap-2 font-bold text-ink">
                  <Sparkles className="h-4 w-4 text-brand-700" />
                  What happened?
                </div>
                {result.trace.length ? result.trace.join(" ") : "Press Run to see Robo wake up."}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Playground;
