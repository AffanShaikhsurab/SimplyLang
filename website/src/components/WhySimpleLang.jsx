import React from 'react';
import { Zap, Brain, Users, Share2 } from 'lucide-react';

const WhySimpleLang = () => {
  const features = [
    {
      icon: Zap,
      title: 'Intuitive',
      description: 'Natural syntax that feels like writing in plain English'
    },
    {
      icon: Brain,
      title: 'Instant',
      description: 'See your code come to life immediately with real-time feedback'
    },
    {
      icon: Users,
      title: 'Fun',
      description: 'Learn through interactive examples and engaging projects'
    },
    {
      icon: Share2,
      title: 'Grows With You',
      description: 'Progress from basics to advanced concepts at your own pace'
    }
  ];

  return (
    <section className="relative py-20 overflow-hidden ">
      <div class="absolute top-0 z-[-2] h-screen w-screen rotate-180 transform bg-white bg-[radial-gradient(60%_120%_at_50%_50%,hsla(0,0%,100%,0)_0,rgba(252,205,238,.5)_100%)]"></div>
      {/* Subtle background blur element - matching hero lavender tone */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-[#e9e0ea] rounded-full mix-blend-multiply filter blur-3xl opacity-50" />
      
      <div className="container relative mx-auto px-6 lg:px-12">
        
        <div className="mb-12 text-left">
          <div className="inline-block">
            <div className="text-sm font-medium text-gray-600 mb-4">— WHY CHOOSE US</div>
            <h2 className="text-4xl font-bold text-gray-900">
              Why Simply Lang?
            </h2>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <div class="absolute top-0 -z-10 h-full w-full bg-white"><div class="absolute bottom-auto left-auto right-0 top-0 h-[500px] w-[500px] -translate-x-[30%] translate-y-[20%] rounded-full bg-[rgba(173,109,244,0.5)] opacity-50 blur-[80px]"></div></div>
          {features.map((feature, index) => (
            <div
              key={index}
              className="group relative p-8 rounded-xl backdrop-blur-sm bg-white/40 border border-white/60 hover:bg-white/60 transition-all duration-300"
            >
              <div className="relative z-10">
                <div className="mb-6 inline-block">
                  <feature.icon className="w-8 h-8 text-gray-900" />
                </div>
                <h3 className="text-xl font-bold mb-4 text-gray-900">
                  {feature.title}
                </h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default WhySimpleLang;