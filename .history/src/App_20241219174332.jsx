import React from 'react';
import Navigation from "./components/Navigation.jsx"
import HeroSection from "./components/HeroSection.jsx";
import WhySimpleLang from "./components/WhySimpleLang.jsx";
import WhatMakesItDifferent from "./components/WhatMakesItDifferent.jsx";
import WhoIsItFor from "./components/WhoIsItFor.jsx";
import JourneySection from "./components/JourneySection.jsx";
import CallToAction from "./components/CallToAction.jsx";

const App = () => {
  return (
    <div className="min-h-screen">
      <Navigation />
      <HeroSection />
      <WhySimpleLang />
      <WhatMakesItDifferent />
      <WhoIsItFor />
      <JourneySection />
      <CallToAction />
    </div>
  );
};

export default App;