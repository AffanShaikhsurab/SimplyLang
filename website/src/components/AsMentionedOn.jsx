import { ExternalLink } from "lucide-react";
import SectionHeader from "./ui/SectionHeader.jsx";

const AsMentionedOn = () => {
  const articles = [
    {
      title: "21-Year-Old Made Coding Feel Easy",
      publication: "Digital Journal",
      url: "https://www.digitaljournal.com/pr/news/insights-news-wire/21-year-old-made-coding-feel-easy-1230313748.html",
      description: "How a young developer is revolutionizing programming with SimplyLang",
    },
    {
      title: "The Rise of Human-First Coding: How Abstraction and AI Are Transforming Software",
      publication: "London Daily News",
      url: "https://www.londondaily.news/the-rise-of-human-first-coding-how-abstraction-and-ai-are-transforming-software-9/",
      description: "Exploring the future of programming with human-centered design",
    },
  ];

  return (
    <section className="section-shell bg-brand-50/40">
      <div className="section-container">
        <SectionHeader
          eyebrow="In the news"
          title="As mentioned on"
          description="SimplyLang and its creator have been featured in leading tech publications."
          centered
        />

        <div className="mx-auto grid max-w-4xl gap-6 md:grid-cols-2">
          {articles.map((article) => (
            <a
              key={article.url}
              href={article.url}
              target="_blank"
              rel="noopener noreferrer"
              className="card-surface group block"
            >
              <div className="mb-4 flex items-start justify-between gap-3">
                <span className="badge-brand">{article.publication}</span>
                <ExternalLink className="h-4 w-4 shrink-0 text-slate-400 transition group-hover:text-brand-700" />
              </div>
              <h3 className="text-lg font-bold text-ink transition group-hover:text-brand-700">
                {article.title}
              </h3>
              <p className="mt-2 text-sm text-ink-muted">{article.description}</p>
            </a>
          ))}
        </div>

        <p className="mt-10 text-center text-ink-muted">
          Created by{" "}
          <a
            href="https://www.affanshaikhsurab.com"
            target="_blank"
            rel="noopener noreferrer"
            className="font-semibold text-brand-700 hover:text-brand-800"
          >
            Affan Shaikhsurab
          </a>
        </p>
      </div>
    </section>
  );
};

export default AsMentionedOn;
