import React, { useState } from "react";
import { useTheme } from "../contexts/ThemeContext";
import { Sun, Moon } from "lucide-react";

const Navigation = ({ showDocs, setShowDocs }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false); // State for mobile menu toggle
  const { theme, toggleTheme } = useTheme();

  return (
    <nav className="border-b border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800">
      {/* Top Bar */}
      <div className="flex items-center justify-between p-4 md:p-0">
        {/* Logo */}
        <div className="flex items-center">
          {/* Your Logo Component or Img Tag Here */}
        </div>

        <div className="flex items-center md:hidden">
          {/* Hamburger Menu Button for Mobile */}
          <button
            className="text-gray-700 dark:text-gray-300 focus:outline-none"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-label="Toggle Menu"
          >
            {isMenuOpen ? (
              <span>&#x2715;</span> // Close icon
            ) : (
              <span>&#9776;</span> // Hamburger icon
            )}
          </button>
        </div>
      </div>

      {/* Navigation Links */}
      <div
        className={`flex-col md:flex md:flex-row md:items-center ${
          isMenuOpen ? "flex" : "hidden"
        } bg-white dark:bg-gray-800`}
      >
        {/* Home Link */}
        <a
          href="#"
          onClick={() => {
            setShowDocs(true);
            setIsMenuOpen(false); // Close menu after click on mobile
          }}
          className={`block w-full md:w-auto px-4 py-2 md:px-6 md:py-4 text-sm text-center md:text-left text-gray-700 dark:text-gray-300 ${
            !showDocs
              ? "bg-gray-200 dark:bg-gray-700"
              : "hover:bg-gray-50 dark:hover:bg-gray-700"
          }`}
        >
          Home
        </a>

        {/* Documentation Link */}
        <a
          href="#"
          onClick={() => {
            setShowDocs(false);
            setIsMenuOpen(false); // Close menu after click on mobile
          }}
          className={`block w-full md:w-auto px-4 py-2 md:px-6 md:py-4 text-sm text-center md:text-left text-gray-700 dark:text-gray-300 ${
            showDocs
              ? "bg-gray-200 dark:bg-gray-700"
              : "hover:bg-gray-50 dark:hover:bg-gray-700"
          }`}
        >
          Documentation
        </a>

        {/* About Us Link */}
        <a
          href="#"
          className="block w-full md:w-auto px-4 py-2 md:px-6 md:py-4 text-sm text-center md:text-left text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700"
          onClick={() => setIsMenuOpen(false)} // Close menu after click on mobile
        >
          About Us
        </a>

        {/* Team Link */}
        <a
          href="#"
          className="block w-full md:w-auto px-4 py-2 md:px-6 md:py-4 text-sm text-center md:text-left text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700"
          onClick={() => setIsMenuOpen(false)} // Close menu after click on mobile
        >
          Team
        </a>

        {/* Theme Toggle Button */}
        <div className="block w-full md:w-auto px-4 py-2 md:px-6 md:py-4 text-sm text-center md:text-left">
            <button
                onClick={toggleTheme}
                className="p-2 rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-800 focus:ring-white"
                aria-label="Toggle Dark Mode"
            >
                {theme === "light" ? (
                  <Sun className="h-6 w-6 text-gray-700 dark:text-gray-300" />
                ) : (
                  <Moon className="h-6 w-6 text-gray-300" />
                )}
            </button>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
