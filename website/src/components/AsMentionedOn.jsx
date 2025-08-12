import React from 'react';

const AsMentionedOn = () => {
  const articles = [
    {
      title: "21-Year-Old Made Coding Feel Easy",
      publication: "Digital Journal",
      url: "https://www.digitaljournal.com/pr/news/insights-news-wire/21-year-old-made-coding-feel-easy-1230313748.html",
      description: "How a young developer is revolutionizing programming with Simply Lang"
    },
    {
      title: "The Rise of Human-First Coding: How Abstraction and AI Are Transforming Software",
      publication: "London Daily News",
      url: "https://www.londondaily.news/the-rise-of-human-first-coding-how-abstraction-and-ai-are-transforming-software-9/",
      description: "Exploring the future of programming with human-centered design"
    }
  ];

  return (
    <section className="py-16 bg-gradient-to-br from-purple-50 to-blue-50 dark:from-gray-900 dark:to-black">
      <div className="container mx-auto px-6">
        <div className="text-center mb-12">
          <h2 className="text-3xl md:text-4xl font-bold text-gray-800 dark:text-white mb-4">
            As Mentioned On
          </h2>
          <p className="text-lg text-gray-600 dark:text-gray-300 max-w-2xl mx-auto">
            Simply Lang and its creator have been featured in leading tech publications
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
          {articles.map((article, index) => (
            <a
              key={index}
              href={article.url}
              target="_blank"
              rel="noopener noreferrer"
              className="group bg-white dark:bg-gray-800 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 overflow-hidden border border-gray-100 dark:border-gray-700 hover:border-purple-200 dark:hover:border-purple-500"
            >
              <div className="p-6">
                <div className="flex items-start justify-between mb-4">
                  <div className="bg-gradient-to-r from-purple-500 to-blue-500 text-white px-3 py-1 rounded-full text-sm font-medium">
                    {article.publication}
                  </div>
                  <svg 
                    className="w-5 h-5 text-gray-400 dark:text-gray-500 group-hover:text-purple-500 dark:group-hover:text-purple-400 transition-colors duration-300"
                    fill="none" 
                    stroke="currentColor" 
                    viewBox="0 0 24 24"
                  >
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                  </svg>
                </div>
                
                <h3 className="text-xl font-bold text-gray-800 dark:text-white mb-3 group-hover:text-purple-600 dark:group-hover:text-purple-400 transition-colors duration-300 line-clamp-2">
                  {article.title}
                </h3>
                
                <p className="text-gray-600 dark:text-gray-300 text-sm leading-relaxed">
                  {article.description}
                </p>

                <div className="mt-4 flex items-center text-purple-600 dark:text-purple-400 font-medium text-sm group-hover:text-purple-700 dark:group-hover:text-purple-300 transition-colors duration-300">
                  Read Article
                  <svg className="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                  </svg>
                </div>
              </div>
            </a>
          ))}
        </div>

        <div className="text-center mt-12">
          <p className="text-gray-600 dark:text-gray-300">
            Created by{" "}
            <a
              href="https://www.affanshaikhsurab.com"
              target="_blank"
              rel="noopener noreferrer"
              className="text-purple-600 dark:text-purple-400 hover:text-purple-700 dark:hover:text-purple-300 font-medium underline decoration-2 decoration-purple-200 dark:decoration-purple-500 hover:decoration-purple-300 dark:hover:decoration-purple-400 transition-all duration-300"
            >
              Affan Shaikhsurab
            </a>
          </p>
        </div>
      </div>
    </section>
  );
};

export default AsMentionedOn;
