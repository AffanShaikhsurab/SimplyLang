import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const Navigation = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  // Handle scroll effect
  useEffect(() => {
    const handleScroll = () => {
      const offset = window.scrollY;
      setScrolled(offset > 50);
    };
    
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
      scrolled ? 'bg-black/40 backdrop-blur-lg shadow-lg' : 'bg-black/20 backdrop-blur-sm'
    } border-b border-white/10`}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex-shrink-0">
            <Link to="/" className="text-xl font-bold text-white hover:text-cyan-300 transition-colors duration-300">
              MyWebsite
            </Link>
          </div>

          {/* Navigation links - Desktop */}
          <div className="hidden md:flex items-center space-x-1">
            <Link
              to="/about"
              className="px-4 py-2 rounded-md text-white hover:text-cyan-300 hover:bg-white/10 transition-all duration-300"
            >
              About
            </Link>
            <Link
              to="/services"
              className="px-4 py-2 rounded-md text-white hover:text-cyan-300 hover:bg-white/10 transition-all duration-300"
            >
              Services
            </Link>
            <Link
              to="/contact"
              className="px-4 py-2 rounded-md text-white hover:text-cyan-300 hover:bg-white/10 transition-all duration-300"
            >
              Contact
            </Link>
            <Link
              to="/login"
              className="ml-2 px-4 py-2 rounded-md bg-gradient-to-r from-cyan-500 to-blue-500 text-white hover:from-cyan-600 hover:to-blue-600 transition-all duration-300 shadow-md hover:shadow-lg"
            >
              Login
            </Link>
          </div>

          {/* Hamburger icon */}
          <div className="md:hidden">
            <button
              onClick={toggleMenu}
              type="button"
              className="p-2 rounded-md text-white hover:bg-white/10 focus:outline-none transition-colors duration-300"
              aria-expanded={isOpen}
              aria-label="Toggle menu"
            >
              <svg className="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                {isOpen ? (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M6 18L18 6M6 6l12 12"
                  />
                ) : (
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M4 6h16M4 12h16M4 18h16"
                  />
                )}
              </svg>
            </button>
          </div>
        </div>

        {/* Mobile menu */}
        <div className={`${isOpen ? 'max-h-64 opacity-100' : 'max-h-0 opacity-0'} md:hidden overflow-hidden transition-all duration-300 ease-in-out`}>
          <div className="px-2 pt-2 pb-3 space-y-1 bg-black/30 backdrop-blur-md rounded-lg mt-2 mb-2">
            <Link
              to="/about"
              className="block px-3 py-2 rounded-md text-white hover:bg-white/10 hover:text-cyan-300 transition-all duration-300"
              onClick={() => setIsOpen(false)}
            >
              About
            </Link>
            <Link
              to="/services"
              className="block px-3 py-2 rounded-md text-white hover:bg-white/10 hover:text-cyan-300 transition-all duration-300"
              onClick={() => setIsOpen(false)}
            >
              Services
            </Link>
            <Link
              to="/contact"
              className="block px-3 py-2 rounded-md text-white hover:bg-white/10 hover:text-cyan-300 transition-all duration-300"
              onClick={() => setIsOpen(false)}
            >
              Contact
            </Link>
            <Link
              to="/login"
              className="block px-3 py-2 rounded-md bg-gradient-to-r from-cyan-500 to-blue-500 text-white hover:from-cyan-600 hover:to-blue-600 transition-all duration-300"
              onClick={() => setIsOpen(false)}
            >
              Login
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
