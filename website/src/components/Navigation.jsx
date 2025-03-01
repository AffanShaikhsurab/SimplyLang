import React, { useState } from "react";

const Navigation = ({ showDocs, setShowDocs }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false); // State for mobile menu toggle

  return (
    <nav className="border-b border-gray-200">
      {/* Top Bar */}
      <div className="flex items-center justify-between p-4 md:p-0 bg-white">
        {/* Logo */}
          
        {/* Hamburger Menu Button for Mobile */}
        <button
          className="md:hidden text-gray-700 focus:outline-none"
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

      {/* Navigation Links */}
      <div
        className={`flex-col md:flex md:flex-row md:items-center ${
          isMenuOpen ? "flex" : "hidden"
        }`}
      >
        {/* Home Link */}
        <a
          href="#"
          onClick={() => {
            setShowDocs(true);
            setIsMenuOpen(false); // Close menu after click on mobile
          }}
          className={`block w-full md:w-auto px-4 py-2 md:px-6 md:py-4 text-sm text-center md:text-left ${
            !showDocs ? "bg-gray-200" : "hover:bg-gray-50"
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
          className={`block w-full md:w-auto px-4 py-2 md:px-6 md:py-4 text-sm text-center md:text-left ${
            showDocs ? "bg-gray-200" : "hover:bg-gray-50"
          }`}
        >
          Documentation
        </a>

        {/* About Us Link */}
        <a
          href="#"
          className="block w-full md:w-auto px-4 py-2 md:px-6 md:py-4 text-sm text-center md:text-left hover:bg-gray-50"
          onClick={() => setIsMenuOpen(false)} // Close menu after click on mobile
        >
          About Us
        </a>

        {/* Team Link */}
        <a
          href="#"
          className="block w-full md:w-auto px-4 py-2 md:px-6 md:py-4 text-sm text-center md:text-left hover:bg-gray-50"
          onClick={() => setIsMenuOpen(false)} // Close menu after click on mobile
        >
          Team
        </a>
      </div>
    </nav>
  );
};

export default Navigation;
