import { Gamepad2, MessageCircle, Music, Paintbrush, PawPrint, Route } from "lucide-react";
import SectionHeader from "./ui/SectionHeader.jsx";

const projects = [
  {
    icon: MessageCircle,
    title: "Talking Robo",
    type: "Story",
    level: "Starter",
    concepts: ["show", "sequence"],
  },
  {
    icon: Paintbrush,
    title: "Shape Garden",
    type: "Art",
    level: "Starter",
    concepts: ["repeat", "color"],
  },
  {
    icon: Route,
    title: "Star Maze",
    type: "Robot",
    level: "Builder",
    concepts: ["move", "turn"],
  },
  {
    icon: PawPrint,
    title: "Mood Pet",
    type: "Story",
    level: "Builder",
    concepts: ["if", "memory"],
  },
  {
    icon: Gamepad2,
    title: "Score Catcher",
    type: "Game",
    level: "Explorer",
    concepts: ["score", "repeat"],
  },
  {
    icon: Music,
    title: "Loop Beat",
    type: "Music",
    level: "Explorer",
    concepts: ["repeat", "sound"],
  },
];

const ProjectGallery = () => (
  <section id="projects" className="section-shell dot-grid-bg">
    <div className="section-container">
      <SectionHeader
        eyebrow="Make it yours"
        title="Remixable starter projects"
        description="Kids can make stories, games, art, music, and robot adventures with the same friendly language."
      />

      <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-3">
        {projects.map((project) => (
          <article key={project.title} className="card-surface !p-0 overflow-hidden">
            <div className="flex h-36 items-center justify-center bg-gradient-to-br from-brand-100 to-amber-50">
              <project.icon className="h-14 w-14 text-brand-700" />
            </div>
            <div className="p-6">
              <div className="flex flex-wrap gap-2">
                <span className="badge-sky">{project.type}</span>
                <span className="badge-warm">{project.level}</span>
              </div>
              <h3 className="mt-4 text-xl font-bold text-ink">{project.title}</h3>
              <div className="mt-3 flex flex-wrap gap-2">
                {project.concepts.map((concept) => (
                  <span key={concept} className="rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-600">
                    {concept}
                  </span>
                ))}
              </div>
              <button type="button" className="btn-primary mt-5 w-full !rounded-xl !py-3">
                Open starter
              </button>
            </div>
          </article>
        ))}
      </div>
    </div>
  </section>
);

export default ProjectGallery;
