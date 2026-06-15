import { ArrowRight, Apple, Server, AppWindow } from "lucide-react";
import SectionHeader from "./ui/SectionHeader.jsx";

const DownloadPlatform = () => (
  <section id="download" className="section-shell bg-white">
    <div className="section-container">
      <div className="mx-auto max-w-3xl rounded-card border border-brand-100 bg-gradient-to-br from-brand-50 to-white p-8 shadow-card md:p-12">
        <SectionHeader
          eyebrow="Offline option"
          title="Ready for offline coding?"
          description="Start with the browser playground first. Download SimplyLang when learners are ready to save files and explore the full text language."
          centered
        />

        <div className="flex flex-col items-center gap-6">
          <button type="button" className="btn-primary">
            Download SimplyLang
            <ArrowRight className="h-5 w-5" />
          </button>

          <div className="flex gap-3">
            <div className="rounded-xl bg-brand-100 p-4 text-ink-muted">
              <Apple className="h-6 w-6" />
            </div>
            <button
              type="button"
              onClick={() => {
                const link = document.createElement("a");
                link.href = "../download/SimplyLangInstaller.exe";
                link.download = "SimplyLangInstaller.exe";
                link.click();
              }}
              className="rounded-xl bg-brand-100 p-4 text-ink transition hover:bg-brand-200"
              aria-label="Download for Windows"
            >
              <AppWindow className="h-6 w-6" />
            </button>
            <div className="rounded-xl bg-brand-100 p-4 text-ink-muted">
              <Server className="h-6 w-6" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
);

export default DownloadPlatform;
