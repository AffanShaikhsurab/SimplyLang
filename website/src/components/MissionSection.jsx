import { Bot, Flag, Palette, Repeat, Star, Trophy } from "lucide-react";
import SectionHeader from "./ui/SectionHeader.jsx";

const missions = [
  {
    icon: Bot,
    title: "Robo says hello",
    concept: "Sequence",
    prompt: 'Use show("Hi!") to make Robo speak.',
  },
  {
    icon: Flag,
    title: "Reach the star",
    concept: "Commands",
    prompt: "Move and turn until Robo reaches the star.",
  },
  {
    icon: Repeat,
    title: "Dance loop",
    concept: "Repeat",
    prompt: "Use repeat to make a tiny dance pattern.",
  },
  {
    icon: Palette,
    title: "Pattern art",
    concept: "Creative coding",
    prompt: "Change colors and repeat moves to make a picture.",
  },
  {
    icon: Star,
    title: "Score box",
    concept: "Variables",
    prompt: "Use a memory box called score and make it grow.",
  },
  {
    icon: Trophy,
    title: "My command",
    concept: "Functions",
    prompt: "Create your own command and use it again.",
  },
];

const MissionSection = () => (
  <section id="learn" className="section-shell bg-white">
    <div className="section-container">
      <SectionHeader
        eyebrow="Guided missions"
        title="One tiny coding idea at a time"
        description="Each mission teaches one concept with a short goal, a visible result, and a playful challenge to make it your own."
      />

      <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">
        {missions.map((mission, index) => (
          <article key={mission.title} className="card-surface">
            <div className="mb-4 flex items-center justify-between">
              <div className="card-icon">
                <mission.icon className="h-6 w-6" />
              </div>
              <span className="text-sm font-bold text-brand-300">0{index + 1}</span>
            </div>
            <span className="badge-brand">{mission.concept}</span>
            <h3 className="mt-3 text-xl font-bold text-ink">Mission {index + 1}: {mission.title}</h3>
            <p className="mt-3 text-ink-muted">{mission.prompt}</p>
          </article>
        ))}
      </div>
    </div>
  </section>
);

export default MissionSection;
