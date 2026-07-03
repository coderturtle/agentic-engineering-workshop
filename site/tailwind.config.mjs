/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}"],
  theme: {
    extend: {
      // Brand layers extend these tokens per series. Keep the base neutral.
      colors: {
        ink: "#1a1a1a",
        paper: "#fafaf8",
      },
    },
  },
  plugins: [],
};
