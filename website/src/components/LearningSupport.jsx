import { HeartHandshake, Lightbulb, ShieldCheck, UsersRound } from "lucide-react";
import SectionHeader from "./ui/SectionHeader.jsx";

const supports = [
  {
    icon: Lightbulb,
    title: "Friendly hints",
    text: "Errors become one clear next step, like: make a memory box called score first.",
  },
  {
    icon: UsersRound,
    title: "Teacher-ready missions",
    text: "Short activities introduce sequence, repeat, choice, memory, and debugging.",
  },
  {
    icon: HeartHandshake,
    title: "Parent co-play",
    text: "Adults can ask children to explain what Robo will do before pressing Run.",
  },
  {
    icon: ShieldCheck,
    title: "Safe first steps",
    text: "The browser-first path avoids accounts, installs, and terminal setup for early lessons.",
  },
];

const LearningSupport = () => (
  <section id="parents" className="section-shell bg-gradient-to-b from-white to-brand-50/50">
    <div className="section-container">
      <div className="grid gap-10 lg:grid-cols-[0.9fr_1.1fr] lg:items-start">
        <div>
          <SectionHeader
            eyebrow="Parents and teachers"
            title="Learning support around every mission"
            description="SimplyLang helps children build confidence, not just finish exercises. The experience focuses on creativity, debugging, and explaining ideas in their own words."
          />
          <div className="rounded-card bg-emerald-50 p-5 ring-1 ring-emerald-100">
            <div className="font-bold text-emerald-950">Success goal</div>
            <p className="mt-2 text-emerald-900">
              A child should run a first program in under 60 seconds and finish the first mission
              without installing anything.
            </p>
          </div>
        </div>

        <div className="grid gap-4 sm:grid-cols-2">
          {supports.map((support) => (
            <article key={support.title} className="card-surface">
              <div className="card-icon mb-4">
                <support.icon className="h-5 w-5" />
              </div>
              <h3 className="text-lg font-bold text-ink">{support.title}</h3>
              <p className="mt-2 text-ink-muted">{support.text}</p>
            </article>
          ))}
        </div>
      </div>
    </div>
  </section>
);

export default LearningSupport;
