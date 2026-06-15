import { ArrowRight, Play } from "lucide-react";
import { Typewriter } from "react-simple-typewriter";

const HeroSection = () => (
  <div className="relative overflow-hidden dot-grid-bg">
    <div className="pointer-events-none absolute inset-0 -z-10">
      <div className="absolute left-1/2 top-0 h-72 w-72 -translate-x-1/2 rounded-full bg-brand-200/40 blur-3xl" />
      <div className="absolute bottom-0 right-0 h-64 w-64 rounded-full bg-amber-100/60 blur-3xl" />
    </div>

    <div className="section-container grid items-center gap-12 pb-16 pt-12 lg:grid-cols-2 lg:pb-24 lg:pt-20">
      <div className="max-w-xl">
        <p className="section-eyebrow">Coding for ages 7–10</p>
        <h1 className="mt-4 text-4xl font-bold leading-tight text-ink lg:text-5xl xl:text-6xl">
          <Typewriter
            words={["Play", "Build", "Imagine"]}
            loop
            cursor
            cursorStyle="_"
            typeSpeed={80}
            deleteSpeed={60}
            delaySpeed={1200}
          />
          <br />
          with <span className="text-brand-700">simple words</span>
        </h1>
        <p className="mt-6 text-lg leading-relaxed text-ink-muted">
          Make Robo speak, move, turn, and solve tiny missions. SimplyLang is a gentle bridge from
          playful command cards to real text coding.
        </p>
        <div className="mt-8 flex flex-col gap-3 sm:flex-row sm:items-center">
          <a href="#play" className="btn-primary">
            Start playing
            <ArrowRight size={16} />
          </a>
          <a href="#learn" className="btn-secondary">
            <Play size={18} />
            See missions
          </a>
        </div>
      </div>

      <div className="relative mx-auto w-full max-w-md lg:max-w-none">
        <div className="code-window">
          <div className="code-window-header">
            <span className="code-dot bg-red-400" />
            <span className="code-dot bg-amber-400" />
            <span className="code-dot bg-emerald-400" />
            <span className="ml-2 font-mono text-xs text-slate-400">robo_starter.simply</span>
          </div>
          <pre className="overflow-x-auto p-6 font-mono text-xs leading-relaxed text-emerald-100 md:text-sm">
            {`show("Hi, I am Robo!")

repeat 4 times
    move 1
    turn right
.

score is 0
score is score + 1
show("Score:", score)`}
          </pre>
        </div>
      </div>
    </div>
  </div>
);

export default HeroSection;
