import { BookOpen, Code, Share, ArrowRight } from "lucide-react";
import SectionHeader from "./ui/SectionHeader.jsx";

const JourneySection = () => {
  const steps = [
    {
      icon: BookOpen,
      number: "01",
      title: "Play",
      description: "Click command cards and watch Robo speak, move, and turn right away",
    },
    {
      icon: Code,
      number: "02",
      title: "Build",
      description: "Finish short missions and remix them into stories, art, mazes, and games",
    },
    {
      icon: Share,
      number: "03",
      title: "Grow",
      description: "Move from cards to readable text, then bridge toward Python or JavaScript later",
    },
  ];

  return (
    <section id="policy" className="section-shell dot-grid-bg">
      <div className="section-container">
        <SectionHeader
          eyebrow="Your journey"
          title="Play, build, grow with SimplyLang"
          description="Three simple stages help children move from playful commands to confident text coding."
        />

        <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
          {steps.map((step, index) => (
            <article key={step.title} className="card-surface relative">
              <div className="mb-5 flex items-center justify-between">
                <div className="card-icon">
                  <step.icon className="h-6 w-6" />
                </div>
                <span className="text-4xl font-bold text-brand-200">{step.number}</span>
              </div>
              <h3 className="text-xl font-bold text-ink">{step.title}</h3>
              <p className="mt-3 text-ink-muted">{step.description}</p>
              {index < steps.length - 1 ? (
                <ArrowRight className="absolute -right-3 top-1/2 hidden h-6 w-6 -translate-y-1/2 text-brand-200 md:block" />
              ) : null}
            </article>
          ))}
        </div>
      </div>
    </section>
  );
};

export default JourneySection;
