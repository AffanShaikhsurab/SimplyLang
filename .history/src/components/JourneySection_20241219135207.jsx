import React from 'react';
import { BookOpen, Code, Share } from 'lucide-react';

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
    <section className="journey-section py-20" style={{ backgroundColor: 'rgba(212,202,217,255)' }}> {/* Skin color background */}
      <div className="container mx-auto px-12">
        <div className="mb-12 text-center md:text-left"> {/* Center text on smaller screens */}
          <div className="text-sm font-medium text-gray-600 mb-4">— YOUR JOURNEY</div>
          <h2 className="text-4xl font-bold text-gray-800">Journey to Master SIMPLE Lang</h2> {/* Darker text for contrast */}
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {steps.map((step, index) => (
            <div key={index} className="relative group"> {/* Add group for hover effect */}
              <div className="card bg-white p-8 rounded-lg shadow-md transition-transform duration-300 hover:scale-105 hover:shadow-lg relative overflow-hidden"
                style={{
                    background: 'linear-gradient(145deg, #ffffff, #e6e6e6)',
                    boxShadow: '5px 5px 10px #bebebe, -5px -5px 10px #ffffff'
                }}
              >
                <div className="flex items-center justify-between mb-6">
                  <step.icon className="w-12 h-12 text-gray-800 transition duration-300 group-hover:text-blue-500" /> {/* Icon hover effect */}
                  <span className="text-4xl font-bold text-gray-300">{step.number}</span>
                </div>
                <h3 className="text-xl font-bold mb-4 text-gray-800">{step.title}</h3>
                <p className="text-gray-600">{step.description}</p>
                {/* Glow Effect (using pseudo-element) */}
                <div className="absolute inset-0 rounded-lg pointer-events-none opacity-0 transition duration-300 group-hover:opacity-100"
                    style={{
                        background: 'radial-gradient(circle, rgba(173, 216, 230,0.3), transparent)',
                        zIndex: -1,
                    }}
                />
              </div>
              {index < steps.length - 1 && (
                <div className="hidden md:block absolute top-1/2 right-0 w-8 h-px bg-gray-300 transform translate-x-full" />
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default JourneySection;