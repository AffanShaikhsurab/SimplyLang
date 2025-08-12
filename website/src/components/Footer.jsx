import React, { useState } from "react";
import {
  FaGithub,
  FaTwitter,
  FaEnvelope,
  FaLinkedin,
  FaInstagram
} from "react-icons/fa";

const Footer = () => {
  const [showTerms, setShowTerms] = useState(false);
  const [showPrivacy, setShowPrivacy] = useState(false);

  const scrollToSection = (id) => {
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: "smooth" });
  };

  return (
    <footer className="bg-gray-100 dark:bg-gray-900 text-gray-800 dark:text-white py-8 mt-12 border-t border-gray-200 dark:border-gray-700">
      <div className="max-w-6xl mx-auto px-4 text-center">

        {/* Navigation links */}
        <div className="flex flex-col sm:flex-row justify-center items-center gap-4 sm:gap-8 mb-4">
          <button onClick={() => scrollToSection("about")} className="hover:underline text-sm text-gray-600 dark:text-gray-300">
            About
          </button>
          <button onClick={() => scrollToSection("contact")} className="hover:underline text-sm text-gray-600 dark:text-gray-300">
            Who Is It For
          </button>
          <button onClick={() => scrollToSection("policy")} className="hover:underline text-sm text-gray-600 dark:text-gray-300">
            Our Journey
          </button>
          <button onClick={() => scrollToSection("contact-us")} className="hover:underline text-sm text-gray-600 dark:text-gray-300">
            Contact Us
          </button>
          <button onClick={() => {
            setShowTerms(!showTerms);
            setShowPrivacy(false);
          }} className="hover:underline text-sm text-gray-600 dark:text-gray-300">
            Terms of Use
          </button>
          <button onClick={() => {
            setShowPrivacy(!showPrivacy);
            setShowTerms(false);
          }} className="hover:underline text-sm text-gray-600 dark:text-gray-300">
            Privacy Policy
          </button>
        </div>

        {/* Terms of Use */}
        {showTerms && (
          <div className="bg-gray-200 dark:bg-gray-800 text-gray-700 dark:text-gray-300 p-4 rounded text-sm mb-4 max-w-3xl mx-auto">
            <h3 className="text-lg font-semibold mb-2 text-gray-900 dark:text-white">Terms of Use</h3>
            <p>
              By using SimplyLang, you agree not to misuse the platform.
              All content is provided for educational purposes only.
              You may not use the content for commercial or unauthorized purposes.
              These terms may be updated at any time without prior notice.
            </p>
          </div>
        )}

        {/* Privacy Policy */}
        {showPrivacy && (
          <div className="bg-gray-200 dark:bg-gray-800 text-gray-700 dark:text-gray-300 p-4 rounded text-sm mb-4 max-w-3xl mx-auto">
            <h3 className="text-lg font-semibold mb-2 text-gray-900 dark:text-white">Privacy & Policy</h3>
            <p>
              We respect your privacy. SimplyLang does not collect personally identifiable information
              unless you provide it. We use minimal cookies only for essential functionality.
              Your data is never sold or shared with third parties. You may contact us for any privacy concerns.
            </p>
          </div>
        )}

        {/* Social Icons */}
        <div className="flex justify-center space-x-6 text-lg text-gray-500 dark:text-gray-400 mb-4">
          <a href="https://github.com/AffanShaikhsurab/SimplyLang" target="_blank" rel="noopener noreferrer" className="hover:text-gray-900 dark:hover:text-white" aria-label="GitHub">
            <FaGithub />
          </a>
          <a href="https://twitter.com/SimplyLang" target="_blank" rel="noopener noreferrer" className="hover:text-gray-900 dark:hover:text-white" aria-label="Twitter">
            <FaTwitter />
          </a>
          <a href="mailto:info@simplylang.org" className="hover:text-gray-900 dark:hover:text-white" aria-label="Email">
            <FaEnvelope />
          </a>
          <a href="https://linkedin.com/in/simplylang" target="_blank" rel="noopener noreferrer" className="hover:text-gray-900 dark:hover:text-white" aria-label="LinkedIn">
            <FaLinkedin />
          </a>
          <a href="https://instagram.com/simplylang" target="_blank" rel="noopener noreferrer" className="hover:text-gray-900 dark:hover:text-white" aria-label="Instagram">
            <FaInstagram />
          </a>
        </div>

        {/* Footer text */}
        <p className="text-xs text-gray-600 dark:text-gray-500">
          Empowering learners with a simple programming language for everyone.
        </p>
        <p className="mt-2 text-sm text-gray-500 dark:text-gray-400">
          © {new Date().getFullYear()} SimplyLang. All rights reserved.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
