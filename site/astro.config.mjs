// @ts-check
import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  site: "https://coderturtle.github.io",
  // RENAME-DEPENDENT: if this repo is ever renamed again, update this base to match
  // the new slug. It's the one spot that needs to change; every internal link uses
  // Astro's base-aware helpers rather than bare paths, so nothing else does.
  base: "/terminal-velocity/",
  integrations: [mdx(), tailwind()],
  output: "static",
});
