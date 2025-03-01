import React, { useState, useEffect, useRef } from 'react';
import { Play, Cake } from 'lucide-react';

const WhatMakesItDifferent = () => {
  const [robotPosition, setRobotPosition] = useState({ x: 50, y: 50, direction: 'east' });
  const [isAnimating, setIsAnimating] = useState(false);
  const robotRef = useRef(null);
  const containerRef = useRef(null);

  const codeSnippet = `moveRobot do
    robot.move("forward", 2)
    robot.turn("right")
    robot.move("forward", 1)

    if robot.detectObstacle() then
        robot.stop()
        robot.alert("Path blocked!")
    .
.
`;

  const executeCode = () => {
    if (isAnimating) return;
    setIsAnimating(true);
    
    const animate = async () => {
      // Move forward 2 units
      await animateMove({ x: robotPosition.x + 100, y: robotPosition.y }, 1000);
      
      // Turn right
      await animateRotation(90, 500);
      
      // Move forward 1 unit
      await animateMove({ x: robotPosition.x + 100, y: robotPosition.y + 50 }, 500);
      
      setIsAnimating(false);
    };

    animate();
  };

  const animateMove = (newPosition, duration) => {
    return new Promise((resolve) => {
      setRobotPosition(prev => ({ ...prev, ...newPosition }));
      setTimeout(resolve, duration);
    });
  };

  const animateRotation = (degrees, duration) => {
    return new Promise((resolve) => {
      if (robotRef.current) {
        robotRef.current.style.transform += ` rotate(${degrees}deg)`;
      }
      setTimeout(resolve, duration);
    });
  };

  useEffect(() => {
    if (robotRef.current) {
      robotRef.current.style.transform = `translate(${robotPosition.x}px, ${robotPosition.y}px)`;
    }
  }, [robotPosition]);

  return (
    <section className="relative py-20 overflow-hidden">
      {/* Ambient animation */}
      <div class="relative h-full w-full bg-white"><div class="absolute bottom-0 left-0 right-0 top-0 bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:14px_24px] [mask-image:radial-gradient(ellipse_80%_50%_at_50%_0%,#000_70%,transparent_110%)]"></div></div>
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-[#e9e0ea] rounded-full mix-blend-multiply filter blur-3xl opacity-50 animate-pulse" />
      
      <div className="container relative mx-auto px-6 lg:px-12">
        <div className="mb-12">
          <div className="text-sm font-medium text-gray-600 mb-4">— UNIQUE FEATURES</div>
          <h2 className="text-4xl font-bold text-gray-900 mb-4">
            What Makes Simply Lang Different?
          </h2>
          <p className="text-gray-600 max-w-2xl">
            Experience real-time code execution with our interactive robot simulator.
            Write simple commands and watch them come to life instantly.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
          {/* Code Editor */}
          <div className="relative group">
            <div className="absolute inset-0 bg-gradient-to-r from-[#e9e0ea] to-[#f3eef4] blur-xl opacity-75 -z-10 group-hover:opacity-100 transition-opacity duration-300" />
            <div className="relative backdrop-blur-sm bg-white/90 rounded-xl border border-white/50 overflow-hidden shadow-xl">
              <div className="flex items-center gap-2 px-4 py-3 border-b border-gray-200">
                <div className="w-3 h-3 rounded-full bg-red-400" />
                <div className="w-3 h-3 rounded-full bg-yellow-400" />
                <div className="w-3 h-3 rounded-full bg-green-400" />
                <span className="ml-2 text-sm text-gray-600">robot_control.js</span>
              </div>
              <div className="p-6 font-mono text-sm">
                <pre className="text-gray-800">
                  {codeSnippet}
                </pre>
                <button
                  onClick={executeCode}
                  disabled={isAnimating}
                  className="mt-4 flex items-center gap-2 px-4 py-2 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition-colors duration-200 disabled:opacity-50"
                >
                  <Play size={16} />
                  <span>{isAnimating ? 'Running...' : 'Run Code'}</span>
                </button>
              </div>
            </div>
          </div>

          {/* Robot Playground */}
          <div className="relative group" ref={containerRef}>
            <div className="absolute inset-0 bg-gradient-to-r from-[#e9e0ea] to-[#f3eef4] blur-xl opacity-75 -z-10 group-hover:opacity-100 transition-opacity duration-300" />
            <div className="relative h-[400px] backdrop-blur-sm bg-white/90 rounded-xl border border-white/50 overflow-hidden">
              <div 
                ref={robotRef}
                className="absolute w-12 h-12 transition-transform duration-1000 ease-in-out"
              >
                <Cake className="w-full h-full text-gray-900" />
              </div>
              {/* Grid pattern */}
              <div className="absolute inset-0" style={{
                backgroundImage: 'linear-gradient(#e9e0ea 1px, transparent 1px), linear-gradient(90deg, #e9e0ea 1px, transparent 1px)',
                backgroundSize: '20px 20px'
              }} />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default WhatMakesItDifferent;