import { useState } from "react";
import Navigation from "./components/Navigation.jsx";
import HeroSection from "./components/HeroSection.jsx";
import Playground from "./components/Playground.jsx";
import WhySimpleLang from "./components/WhySimpleLang.jsx";
import WhatMakesItDifferent from "./components/WhatMakesItDifferent.jsx";
import WhoIsItFor from "./components/WhoIsItFor.jsx";
import JourneySection from "./components/JourneySection.jsx";
import MissionSection from "./components/MissionSection.jsx";
import ProjectGallery from "./components/ProjectGallery.jsx";
import LearningSupport from "./components/LearningSupport.jsx";
import CallToAction from "./components/CallToAction.jsx";
import DownloadPlatform from "./components/DownloadPlatform.jsx";
import AsMentionedOn from "./components/AsMentionedOn.jsx";
import Documentation from "./components/Docs.jsx";
import ScrollToTopButton from "./components/ScrollToTop.jsx";
import Footer from "./components/Footer.jsx";

const App = () => {
  const [showDocs, setShowDocs] = useState(true);

  return (
    <div className="min-h-screen scroll-smooth bg-white">
      <Navigation showDocs={showDocs} setShowDocs={setShowDocs} />
      {showDocs ? (
        <>
          <HeroSection />
          <Playground />
          <WhySimpleLang />
          <WhatMakesItDifferent />
          <MissionSection />
          <ProjectGallery />
          <WhoIsItFor />
          <LearningSupport />
          <DownloadPlatform />
          <JourneySection />
          <AsMentionedOn />
          <CallToAction />
        </>
      ) : (
        <Documentation />
      )}
      <ScrollToTopButton />
      <Footer />
    </div>
  );
};

export default App;
