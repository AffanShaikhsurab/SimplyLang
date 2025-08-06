import React, { useState } from "react";
import Navigation from "./components/Navigation.jsx";
import HeroSection from "./components/HeroSection.jsx";
import WhySimpleLang from "./components/WhySimpleLang.jsx";
import WhatMakesItDifferent from "./components/WhatMakesItDifferent.jsx";
import WhoIsItFor from "./components/WhoIsItFor.jsx";
import JourneySection from "./components/JourneySection.jsx";
import CallToAction from "./components/CallToAction.jsx";
import DownloadPlatform from "./components/DownloadPlatform.jsx";
import AsMentionedOn from "./components/AsMentionedOn.jsx";
import Documentation from "./components/Docs.jsx";
import ScrollToTopButton from "./components/ScrollToTop.jsx";


const App = () => {
  const [showDocs, setShowDocs] = useState(true);

  return (
    <div className="min-h-screen">
      <Navigation showDocs={showDocs} setShowDocs={setShowDocs} />
      {showDocs ? (
        <>
          <HeroSection />
          <WhySimpleLang />
          <WhatMakesItDifferent />
          <WhoIsItFor />          <JourneySection />
          <DownloadPlatform />
          <AsMentionedOn />
          <CallToAction />
        </>
      ) : (
        <Documentation />
      )}
      <ScrollToTopButton />
    </div>
  );
};

export default App;
