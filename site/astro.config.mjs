// @ts-check
import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  // Custom domain (terminal-velocity.coderturtle.io) via GitHub Pages + Route53 CNAME,
  // see .hekton/project.yaml's `deployment` block and docs/decisions.md. Site now serves
  // at the domain root, not under /terminal-velocity/ on coderturtle.github.io.
  site: "https://terminal-velocity.coderturtle.io",
  base: "/",
  integrations: [mdx(), tailwind()],
  output: "static",
});
