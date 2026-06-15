import { useState } from "react";
import { FaGithub, FaTwitter, FaEnvelope, FaLinkedin, FaInstagram } from "react-icons/fa";

const Footer = () => {
  const [showTerms, setShowTerms] = useState(false);
  const [showPrivacy, setShowPrivacy] = useState(false);

  const scrollToSection = (id) => {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: "smooth" });
  };

  const linkClass =
    "text-sm font-medium text-slate-400 transition hover:text-white";

  return (
    <footer className="border-t border-slate-800 bg-slate-900 py-10 text-white">
      <div className="section-container text-center">
        <div className="mb-6 flex flex-wrap justify-center gap-x-6 gap-y-3">
          <button type="button" onClick={() => scrollToSection("play")} className={linkClass}>
            Play
          </button>
          <button type="button" onClick={() => scrollToSection("learn")} className={linkClass}>
            Missions
          </button>
          <button type="button" onClick={() => scrollToSection("parents")} className={linkClass}>
            Families
          </button>
          <button type="button" onClick={() => scrollToSection("download")} className={linkClass}>
            Download
          </button>
          <button
            type="button"
            onClick={() => {
              setShowTerms(!showTerms);
              setShowPrivacy(false);
            }}
            className={linkClass}
          >
            Terms
          </button>
          <button
            type="button"
            onClick={() => {
              setShowPrivacy(!showPrivacy);
              setShowTerms(false);
            }}
            className={linkClass}
          >
            Privacy
          </button>
        </div>

        {showTerms ? (
          <div className="mx-auto mb-4 max-w-3xl rounded-card bg-slate-800 p-4 text-left text-sm text-slate-300">
            <h3 className="mb-2 text-lg font-semibold text-white">Terms of Use</h3>
            <p>
              By using SimplyLang, you agree not to misuse the platform. All content is provided for
              educational purposes only. You may not use the content for commercial or unauthorized
              purposes.
            </p>
          </div>
        ) : null}

        {showPrivacy ? (
          <div className="mx-auto mb-4 max-w-3xl rounded-card bg-slate-800 p-4 text-left text-sm text-slate-300">
            <h3 className="mb-2 text-lg font-semibold text-white">Privacy Policy</h3>
            <p>
              We respect your privacy. SimplyLang does not collect personally identifiable information
              unless you provide it. Your data is never sold or shared with third parties.
            </p>
          </div>
        ) : null}

        <div className="mb-4 flex justify-center gap-5 text-lg text-slate-400">
          <a href="https://github.com/AffanShaikhsurab/SimplyLang" target="_blank" rel="noopener noreferrer" className="hover:text-white" aria-label="GitHub">
            <FaGithub />
          </a>
          <a href="https://twitter.com/SimplyLang" target="_blank" rel="noopener noreferrer" className="hover:text-white" aria-label="Twitter">
            <FaTwitter />
          </a>
          <a href="mailto:info@simplylang.org" className="hover:text-white" aria-label="Email">
            <FaEnvelope />
          </a>
          <a href="https://linkedin.com/in/simplylang" target="_blank" rel="noopener noreferrer" className="hover:text-white" aria-label="LinkedIn">
            <FaLinkedin />
          </a>
          <a href="https://instagram.com/simplylang" target="_blank" rel="noopener noreferrer" className="hover:text-white" aria-label="Instagram">
            <FaInstagram />
          </a>
        </div>

        <p className="text-sm text-slate-400">
          A playful first coding language for children ages 7–10.
        </p>
        <p className="mt-2 text-xs text-slate-500">
          © {new Date().getFullYear()} SimplyLang. All rights reserved.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
