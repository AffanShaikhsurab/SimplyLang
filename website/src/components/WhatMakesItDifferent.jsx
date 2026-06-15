import { useState, useEffect, useRef } from "react";
import { Play, Bot } from "lucide-react";
import SectionHeader from "./ui/SectionHeader.jsx";

const WhatMakesItDifferent = () => {
  const [robotPosition, setRobotPosition] = useState({ x: 50, y: 50, direction: "east" });
  const [isAnimating, setIsAnimating] = useState(false);
  const robotRef = useRef(null);

  const codeSnippet = `show("Robo is ready!")
repeat 2 times
    move 1
    turn right
.
`;

  const executeCode = () => {
    if (isAnimating) return;
    setIsAnimating(true);

    const animate = async () => {
      await animateMove({ x: robotPosition.x + 100, y: robotPosition.y }, 1000);
      await animateRotation(90, 500);
      await animateMove({ x: robotPosition.x + 100, y: robotPosition.y + 50 }, 500);
      setIsAnimating(false);
    };

    animate();
  };

  const animateMove = (newPosition, duration) =>
    new Promise((resolve) => {
      setRobotPosition((prev) => ({ ...prev, ...newPosition }));
      setTimeout(resolve, duration);
    });

  const animateRotation = (degrees, duration) =>
    new Promise((resolve) => {
      if (robotRef.current) {
        robotRef.current.style.transform += ` rotate(${degrees}deg)`;
      }
      setTimeout(resolve, duration);
    });

  useEffect(() => {
    if (robotRef.current) {
      robotRef.current.style.transform = `translate(${robotPosition.x}px, ${robotPosition.y}px)`;
    }
  }, [robotPosition]);

  return (
    <section className="section-shell bg-white">
      <div className="section-container">
        <SectionHeader
          eyebrow="Try it yourself"
          title="Code that makes something visible happen"
          description="Children learn best when they can see Robo react. Start with a tiny mission, press Go, and watch the world change."
        />

        <div className="grid grid-cols-1 items-start gap-8 lg:grid-cols-2">
          <div className="code-window">
            <div className="code-window-header">
              <span className="code-dot bg-red-400" />
              <span className="code-dot bg-amber-400" />
              <span className="code-dot bg-emerald-400" />
              <span className="ml-2 font-mono text-xs text-slate-400">robo_mission.simply</span>
            </div>
            <div className="p-6">
              <pre className="font-mono text-sm leading-relaxed text-slate-200">{codeSnippet}</pre>
              <button
                type="button"
                onClick={executeCode}
                disabled={isAnimating}
                className="btn-primary mt-5 !rounded-xl !py-2.5 disabled:opacity-50"
              >
                <Play size={16} />
                {isAnimating ? "Running…" : "Go!"}
              </button>
            </div>
          </div>

          <div className="card-surface !p-0 overflow-hidden">
            <div className="relative h-[400px] bg-brand-50">
              <div
                ref={robotRef}
                className="absolute flex h-12 w-12 items-center justify-center rounded-xl bg-white shadow-card transition-transform duration-1000 ease-in-out"
              >
                <Bot className="h-8 w-8 text-brand-700" />
              </div>
              <div
                className="absolute inset-0"
                style={{
                  backgroundImage:
                    "linear-gradient(#ddd6fe 1px, transparent 1px), linear-gradient(90deg, #ddd6fe 1px, transparent 1px)",
                  backgroundSize: "24px 24px",
                }}
              />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default WhatMakesItDifferent;
