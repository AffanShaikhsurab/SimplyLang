/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#f5f3ff",
          100: "#ede9fe",
          200: "#ddd6fe",
          300: "#c4b5fd",
          500: "#8b5cf6",
          600: "#7c3aed",
          700: "#6d28d9",
          800: "#5b21b6",
          950: "#2e1065",
        },
        ink: {
          DEFAULT: "#1e293b",
          muted: "#64748b",
        },
      },
      fontFamily: {
        display: ["Fredoka", "Nunito", "system-ui", "sans-serif"],
        body: ["Nunito", "system-ui", "sans-serif"],
      },
      borderRadius: {
        card: "1.25rem",
      },
      boxShadow: {
        card: "0 4px 24px -4px rgba(109, 40, 217, 0.12)",
        "card-hover": "0 12px 32px -8px rgba(109, 40, 217, 0.18)",
      },
    },
  },
  plugins: [],
};
