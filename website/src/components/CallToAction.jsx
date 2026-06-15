import { ArrowRight } from "lucide-react";
import SectionHeader from "./ui/SectionHeader.jsx";

const CallToAction = () => (
  <section id="contact-us" className="section-shell bg-brand-700 text-white">
    <div className="section-container text-center">
      <SectionHeader
        eyebrow="Get started"
        title="Ready to make Robo move?"
        description="Start in the browser with a tiny mission, then grow into readable text coding when the child is ready."
        centered
        light
      />
      <div className="flex flex-col items-center justify-center gap-3 sm:flex-row">
        <a
          href="#play"
          className="inline-flex items-center gap-2 rounded-full bg-white px-8 py-3.5 text-sm font-bold text-brand-800 transition hover:bg-brand-50"
        >
          Start playing
          <ArrowRight size={16} />
        </a>
        <a
          href="#parents"
          className="inline-flex items-center gap-2 rounded-full border-2 border-white/40 px-8 py-3.5 text-sm font-semibold text-white transition hover:bg-white/10"
        >
          Parents & teachers
        </a>
      </div>
    </div>
  </section>
);

export default CallToAction;
