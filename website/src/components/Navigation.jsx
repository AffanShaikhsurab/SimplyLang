/* eslint-disable react/prop-types */
import { useState } from "react";
import { Bot, Menu, X } from "lucide-react";

const Navigation = ({ showDocs, setShowDocs }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const homeLinks = [
    { label: "Play", href: "#play" },
    { label: "Missions", href: "#learn" },
    { label: "Projects", href: "#projects" },
    { label: "Families", href: "#parents" },
    { label: "Download", href: "#download" },
  ];

  const goHome = () => {
    setShowDocs(true);
    setIsMenuOpen(false);
  };

  const goDocs = () => {
    setShowDocs(false);
    setIsMenuOpen(false);
  };

  const linkClass = (active) =>
    `block rounded-lg px-4 py-2.5 text-sm font-semibold transition md:px-3 md:py-2 ${
      active
        ? "bg-brand-100 text-brand-800"
        : "text-ink-muted hover:bg-brand-50 hover:text-brand-800"
    }`;

  return (
    <nav className="sticky top-0 z-50 border-b border-brand-100 bg-white/90 backdrop-blur-md">
      <div className="section-container flex items-center justify-between gap-4 py-3">
        <button
          type="button"
          onClick={goHome}
          className="flex items-center gap-2 rounded-lg px-1 py-1 text-left transition hover:opacity-90"
        >
          <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-brand-700 text-white">
            <Bot className="h-5 w-5" />
          </span>
          <span className="font-display text-lg font-bold text-ink">SimplyLang</span>
        </button>

        <div className="hidden items-center gap-1 md:flex">
          <button type="button" onClick={goHome} className={linkClass(showDocs)}>
            Home
          </button>
          {showDocs &&
            homeLinks.map((link) => (
              <a key={link.href} href={link.href} className={linkClass(false)}>
                {link.label}
              </a>
            ))}
          <button type="button" onClick={goDocs} className={linkClass(!showDocs)}>
            Learn
          </button>
          {showDocs ? (
            <a href="#play" className="btn-primary ml-2 !px-5 !py-2 text-xs">
              Start playing
            </a>
          ) : null}
        </div>

        <button
          type="button"
          className="rounded-lg p-2 text-ink md:hidden"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
          aria-label="Toggle menu"
        >
          {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
        </button>
      </div>

      {isMenuOpen ? (
        <div className="border-t border-brand-100 bg-white px-6 py-4 md:hidden">
          <div className="flex flex-col gap-1">
            <button type="button" onClick={goHome} className={linkClass(showDocs)}>
              Home
            </button>
            {showDocs &&
              homeLinks.map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className={linkClass(false)}
                  onClick={() => setIsMenuOpen(false)}
                >
                  {link.label}
                </a>
              ))}
            <button type="button" onClick={goDocs} className={linkClass(!showDocs)}>
              Learn
            </button>
            {showDocs ? (
              <a href="#play" className="btn-primary mt-2 text-center" onClick={() => setIsMenuOpen(false)}>
                Start playing
              </a>
            ) : null}
          </div>
        </div>
      ) : null}
    </nav>
  );
};

export default Navigation;
