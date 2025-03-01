import React from 'react';
import { BookOpen, Code, Share, ArrowRight } from 'lucide-react';

const JourneySection = () => {
  const steps = [
    {
      icon: BookOpen,
      number: '01',
      title: 'Learn the Basics',
      description: 'Start with interactive tutorials designed to make learning fun and engaging',
    },
    {
      icon: Code,
      number: '02',
      title: 'Create Your First Project',
      description: 'Apply your knowledge by building real projects with guidance and support',
    },
    {
      icon: Share,
      number: '03',
      title: 'Share Your Creations',
      description: 'Join our community and showcase your work to the world',
    },
  ];

  return (
    <section className="relative py-20 overflow-hidden ">
        <div class="absolute inset-0 -z-10 h-full w-full bg-white bg-[radial-gradient(#e5e7eb_1px,transparent_1px)] [background-size:16px_16px]"></div>
      {/* Ambient background animations */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-[#e9e0ea] rounded-full mix-blend-multiply filter blur-3xl opacity-50 animate-pulse" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-[#e9e0ea] rounded-full mix-blend-multiply filter blur-3xl opacity-50 animate-pulse animation-delay-1000" />

      <div className="container relative mx-auto px-6 lg:px-12">
        <div className="mb-16 relative">
          <div className="text-sm font-medium text-gray-600 mb-4 opacity-0 animate-fade-in">
            — YOUR JOURNEY
          </div>
          <h2 className="text-4xl font-bold text-gray-900 opacity-0 animate-fade-in animation-delay-200">
            Journey to Master Simply Lang
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 relative">
          {steps.map((step, index) => (
            <div 
              key={index} 
              className="group relative opacity-0 animate-fade-in-up"
              style={{ animationDelay: `${index * 200}ms` }}
            >
              {/* Card background with glassmorphism */}
              <div className="absolute inset-0 bg-gradient-to-br from-white/80 to-white/40 rounded-xl backdrop-blur-sm border border-white/50 shadow-lg transition-all duration-300 group-hover:scale-[1.02] group-hover:shadow-xl" />
              
              {/* Card content */}
              <div className="relative p-8">
                <div className="flex items-center justify-between mb-6">
                  {/* Icon container with gradient */}
                  <div className="p-3 rounded-xl bg-gradient-to-br from-[#e9e0ea] to-white inline-block transform transition-transform duration-300 group-hover:scale-110 group-hover:rotate-3">
                    <step.icon className="w-8 h-8 text-gray-900" />
                  </div>
                  
                  {/* Step number with gradient */}
                  <span className="text-6xl font-bold bg-gradient-to-br from-gray-200 to-gray-300 bg-clip-text text-transparent opacity-50">
                    {step.number}
                  </span>
                </div>
                
                <h3 className="text-xl font-bold mb-4 text-gray-900 transform transition-all duration-300 group-hover:translate-x-1">
                  {step.title}
                </h3>
                <p className="text-gray-600 transform transition-all duration-300 group-hover:translate-x-1">
                  {step.description}
                </p>
              </div>

              {/* Connecting arrow for desktop */}
              {index < steps.length - 1 && (
                <div className="hidden md:block absolute top-1/2 -right-4 transform -translate-y-1/2 translate-x-full z-10">
                  <ArrowRight className="w-8 h-8 text-gray-300 animate-pulse" />
                </div>
              )}
            </div>
          ))}
        </div>
      </div>

      <style jsx>{`
        @keyframes fade-in {
          from { opacity: 0; }
          to { opacity: 1; }
        }

        @keyframes fade-in-up {
          from {
            opacity: 0;
            transform: translateY(20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        .animate-fade-in {
          animation: fade-in 0.6s forwards;
        }

        .animate-fade-in-up {
          animation: fade-in-up 0.8s forwards;
        }

        .animation-delay-200 {
          animation-delay: 200ms;
        }

        .animation-delay-1000 {
          animation-delay: 1000ms;
        }
      `}</style>
    </section>
  );
};

export default JourneySection;