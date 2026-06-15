import { Zap, Brain, Users, Share2 } from "lucide-react";
import SectionHeader from "./ui/SectionHeader.jsx";

const WhySimpleLang = () => {
  const features = [
    {
      icon: Zap,
      title: "Easy words",
      description: "Natural syntax that feels like writing in plain English",
    },
    {
      icon: Brain,
      title: "See it work",
      description: "Watch Robo react immediately when you press Run",
    },
    {
      icon: Users,
      title: "Like a game",
      description: "Short missions, command cards, and playful challenges",
    },
    {
      icon: Share2,
      title: "Level up",
      description: "Grow from cards to readable text, then into bigger projects",
    },
  ];

  return (
    <section className="section-shell bg-gradient-to-b from-white to-brand-50/40">
      <div className="section-container">
        <SectionHeader
          eyebrow="Why SimplyLang"
          title="Built for curious young coders"
          description="SimplyLang keeps the first steps small, visual, and fun — so children build confidence before they meet harder programming ideas."
        />

        <div className="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-4">
          {features.map((feature) => (
            <article key={feature.title} className="card-surface">
              <div className="card-icon mb-5">
                <feature.icon className="h-6 w-6" />
              </div>
              <h3 className="text-xl font-bold text-ink">{feature.title}</h3>
              <p className="mt-3 text-ink-muted">{feature.description}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
};

export default WhySimpleLang;
