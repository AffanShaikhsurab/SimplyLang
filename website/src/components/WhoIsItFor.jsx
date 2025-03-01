import React from 'react';
import { Palette, GraduationCap, Baby, Compass } from 'lucide-react';

const WhoIsItFor = () => {
  const audiences = [
    {
      icon: Baby,
      title: 'Children',
      description: 'A playful introduction to programming concepts through interactive games and visual learning'
    },
    {
      icon: Palette,
      title: 'Artists',
      description: 'Express your creativity through code with our visual-first approach to programming'
    },
    {
      icon: GraduationCap,
      title: 'Teachers',
      description: 'Empower your students with a programming language designed for learning and growth'
    },
    {
      icon: Compass,
      title: 'Curious Explorers',
      description: 'Discover the joy of programming with our intuitive and engaging platform'
    }
  ];

  return (
    <section className="relative py-20 overflow-hidden">
      <div class="absolute top-0 -z-10 h-full w-full bg-white"><div class="absolute bottom-auto left-auto right-0 top-0 h-[500px] w-[500px] -translate-x-[30%] translate-y-[20%] rounded-full bg-[rgba(173,109,244,0.5)] opacity-50 blur-[80px]"></div></div>
      {/* Animated background elements */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-[#e9e0ea] rounded-full mix-blend-multiply filter blur-3xl opacity-50 animate-pulse" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-[#e9e0ea] rounded-full mix-blend-multiply filter blur-3xl opacity-50 animate-pulse animation-delay-1000" />

      <div className="container relative mx-auto px-6 lg:px-12">
        <div className="mb-16 relative">
          <div className="text-sm font-medium text-gray-600 mb-4 opacity-0 animate-fade-in">— TARGET AUDIENCE</div>
          <h2 className="text-4xl font-bold text-gray-900 opacity-0 animate-fade-in animation-delay-200">
            Who Is Simply Lang For?
          </h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {audiences.map((audience, index) => (
            <div 
              key={index} 
              className="group relative opacity-0 animate-fade-in-up"
              style={{ animationDelay: `${index * 200}ms` }}
            >
              {/* Card background with gradient and glassmorphism */}
              <div className="absolute inset-0 bg-gradient-to-br from-white/80 to-white/40 rounded-xl backdrop-blur-sm border border-white/50 shadow-lg transition-all duration-300 group-hover:scale-[1.02] group-hover:shadow-xl" />
              
              {/* Card content */}
              <div className="relative p-8">
                {/* Icon container with gradient background */}
                <div className="mb-6 p-3 rounded-xl bg-gradient-to-br from-[#e9e0ea] to-white inline-block transform transition-transform duration-300 group-hover:scale-110 group-hover:rotate-3">
                  <audience.icon className="w-8 h-8 text-gray-900" />
                </div>
                
                <h3 className="text-xl font-bold mb-4 text-gray-900 transform transition-all duration-300 group-hover:translate-x-1">
                  {audience.title}
                </h3>
                <p className="text-gray-600 transform transition-all duration-300 group-hover:translate-x-1">
                  {audience.description}
                </p>
              </div>
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

export default WhoIsItFor;