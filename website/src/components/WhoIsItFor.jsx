import { Palette, GraduationCap, Baby, Compass } from "lucide-react";
import SectionHeader from "./ui/SectionHeader.jsx";

const WhoIsItFor = () => {
  const audiences = [
    {
      icon: Baby,
      title: "Kids ages 7–10",
      description: "A playful first coding space with short missions, visible results, and friendly hints",
    },
    {
      icon: Palette,
      title: "Creative builders",
      description: "Make stories, robot mazes, art, music, quizzes, and tiny games with simple words",
    },
    {
      icon: GraduationCap,
      title: "Teachers",
      description: "Teach sequence, loops, choices, variables, and debugging through guided missions",
    },
    {
      icon: Compass,
      title: "Parents",
      description: "Support co-play at home without needing installs, accounts, or terminal setup first",
    },
  ];

  return (
    <section className="section-shell bg-white">
      <div className="section-container">
        <SectionHeader
          eyebrow="Who it's for"
          title="Kids lead. Grown-ups support."
          description="SimplyLang is designed for young learners first, with clear support for families and classrooms."
        />

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-4">
          {audiences.map((audience) => (
            <article key={audience.title} className="card-surface">
              <div className="card-icon mb-5">
                <audience.icon className="h-6 w-6" />
              </div>
              <h3 className="text-xl font-bold text-ink">{audience.title}</h3>
              <p className="mt-3 text-ink-muted">{audience.description}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
};

export default WhoIsItFor;
