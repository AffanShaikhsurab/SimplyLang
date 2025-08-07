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
import Footer from "./components/Footer.jsx";

const App = () => {
  const [showDocs, setShowDocs] = useState(true);

  return (
    <div className="min-h-screen scroll-smooth">
      <Navigation showDocs={showDocs} setShowDocs={setShowDocs} />
      {showDocs ? (
        <>
          <section id="about">
            <HeroSection />
            <WhySimpleLang />
            <WhatMakesItDifferent />
          </section>

          <section id="contact">
            <WhoIsItFor />
            <DownloadPlatform />
          </section>

          <section id="policy">
            <JourneySection />
            <AsMentionedOn />
          </section>

          {/* ✅ Fix: Add ID so footer can scroll here */}
          <section id="contact-us">
            <CallToAction />
          </section>
        </>
      ) : (
        <Documentation />
      )}
      <Footer />
    </div>
  );
};

export default App;
