# Implementation Plan — Deliverables/Branding + Build-log/Pages Publisher

> Produced by an Opus-run planning pass (2026-07-03), reviewing `docs/workshop-design.md`, `docs/workshop-gremlin-design.md`, the canonical `~/hekton/gremlins/workshop/workshop-gremlin.md` definition, and `blog-factory-lab`'s Astro starter. Scope: the Workshop Gremlin's **Deliverables & branding** and **Build-log / Pages publisher** steps. Produces a real, buildable skeleton up to "ready to deploy." Out of scope (do not do here): the final workshop name (separate naming pass), module *content*/exercises/rubrics (later Coachgremlin runs), and the first live Pages deploy (human-confirmed gate).
>
> **Rename-safety note:** this plan was written before the naming pass, using the working title "Prompt → Loop" and a placeholder slug. The naming pass has since completed — the final name is **Terminal Velocity** (`terminal-velocity`) — and this file's rename-dependent spots (flagged inline as `RENAME-DEPENDENT`, e.g. the Astro `site`/`base` config in §4d) have been mechanically updated to the real slug. The quarantine discipline below is what made that a same-day find-replace instead of a scramble.

---

## 1. Module directory skeleton

Create a top-level `modules/` tree mirroring the four-module arc + capstone from `docs/workshop-design.md`. Numbered prefixes encode the required teaching order (the arc is a sequence, not a menu).

```
modules/
  README.md                          # the arc overview + how to work through it
  01-prompt-engineering/README.md
  02-context-engineering/README.md
  03-harness-engineering/README.md
  04-loop-engineering/README.md
  05-synthesis-capstone/README.md
```

**Naming convention:** `NN-kebab-case-topic/`. Two-digit prefix so order is unambiguous and lexical sort matches teaching order. One directory per module; each holds a single `README.md` stub for now. No `exercises/` subfolders yet — exercise specs are a later Coachgremlin run, and empty dirs add noise. When content-building starts, each module grows an `exercises/` folder; the stub reserves that expansion explicitly.

**What each module `README.md` stub must contain** (structure real, teaching content deliberately absent):
- Module title + working-title-agnostic H1 (e.g. `# Module 3 — Harness Engineering`).
- **The question this module answers** — copied verbatim from the arc in `docs/workshop-design.md` (e.g. harness = "what can it reach, and how is the work organized?"; loop = "when does it stop, how do we know it's right, and how does it get better without me watching every turn?").
- **Where it sits in the arc** — one line naming the prior/next module and the structural-vs-behavioral hinge (harness = structural/static; loop = behavioral/runtime).
- **Placeholder learning objectives** — 3-5 bullets marked `_(objectives finalized in the Coachgremlin content pass)_`.
- **Named exercise pattern it will draw from** — a pointer, not a spec:
  - `01-prompt-engineering` → single-turn precision (no external named pattern yet; note "atomic unit, necessary-but-insufficient framing").
  - `02-context-engineering` → a context-budget exercise: a deliberately oversized/noisy context the learner must curate down to a fixed budget while preserving what the task actually needs — forces a real curation tradeoff rather than talking about one in the abstract. (Flagged as a gap by the Workshop Review Panel's Instructional Designer — module 02 had no anchor at all before this pass; exact exercise spec is still a later Coachgremlin content-building task, this is only the pointer.)
  - `03-harness-engineering` → tool access / sub-agents / worktrees / persistent state material.
  - `04-loop-engineering` → the loop taxonomy (agent / verification / event-driven / hill-climbing), **Ticket-to-PR-Ready Loop**, **Restartable Handoff Loop**, and the **"ralph loop"** (Geoffrey Huntley) for the hill-climbing/self-improving concept; plus the stable-goal-vs-moving-target decision rule.
  - `05-synthesis-capstone` → the "diagnose which of the four is the bottleneck in a deliberately broken agent task, then fix it" exercise.
- **Stop condition placeholder** — `_(rubric + terminal states defined per exercise by Coachgremlin)_`. For loop engineering, name the concept (e.g. Ticket-to-PR-Ready's "can't reproduce after two attempts" terminal state) so the shape is visible.
- A closing `> Content status: skeleton only. Teaching content is built one concept at a time in a later Coachgremlin run (see docs/next-actions.md).` banner so no reader mistakes a stub for a finished module.

**`modules/README.md`** is the index: the four-module arc + capstone in order, the one-line question each answers, the "how they compose" synthesis sentence from `docs/workshop-design.md`, and the loop taxonomy table. This is the file the top-level README links into as "the workshop itself."

---

## 2. Learner-facing top-level README rework

The current `README.md` is internal Hekton scaffold framing (classification header, promotion target, vault-mutation rules, documentation contract). A self-paced public workshop landing page needs a different job: get a stranger who cloned the repo productively started. **Do not delete the Hekton framing — relocate it.**

**Plan:**
- Move the internal scaffold content (classification block, documentation contract, vault-mutation note, "two goals / extract reusable machinery" framing, key-docs index) into a new `docs/maintainers.md` (or `CONTRIBUTING.md`-style maintainer doc). `CLAUDE.md`/`AGENTS.md` already carry the agent operating rules, so the README does not need to.
- Rewrite `README.md` as the learner landing page with these sections:
  1. **Title + one-line tagline** — "Terminal Velocity" plus a hook-first tagline pulled from the brand layer (§3), leading with the doing-not-reading thesis rather than a list of the four module names.
  2. **What this is / who it's for** — the audience statement from `docs/workshop-design.md` (advanced practitioners already using agents daily; not intro-to-AI).
  3. **Prerequisites** — comfort with git/CLI/diffs; regular use of at least one coding agent/harness (Claude Code, Codex, Cursor); a working harness installed. This is the concrete gate.
  4. **How to start** — a literal copy-pasteable `git clone .../terminal-velocity && cd terminal-velocity && cat modules/README.md`-style command block, not prose bullets — the gap between reading and doing is the whole friction budget (per the Workshop Review Panel's Developer Evangelist finding, `docs/review-panel/2026-07-03-initial-design.md`). Then work through `modules/` in order; every module's core exercise is *run through your own harness*, not read.
  5. **How the modules connect** — the prompt → context → harness → loop arc in one short paragraph + link to `modules/README.md` for the full synthesis; state the capstone diagnoses which layer is the bottleneck.
  6. **The teaching method** — the "harness is the classroom / Coachgremlin frames each exercise and grades against your actual attempt, never hands over the solution" thesis.
  7. **Build-in-public note** — one line pointing at the published build-log site (§4) as a live demonstration of the practices taught.
  8. ~~Working-title banner~~ — not needed; the naming pass completed before this section executes. If a future rename happens, add a temporary banner then rather than carrying one permanently.
- Keep a slim **Key docs** footer linking `docs/workshop-design.md` and `docs/maintainers.md` for anyone who wants the design rationale, but keep the top of the file learner-first.

---

## 3. Brand layer

**Single source of truth:** one file, `docs/brand.md`, adapting the reusable pattern already proven in blog-factory-lab (`templates/brand-style-layer-template.md`, and the filled example `examples/hekton-blog/brand-style-layer.md`). Do not scatter brand values across README + site + configs; those consume `docs/brand.md`, they don't redefine it. This is the same "the only place a series' personality lives" discipline ADR-001 of the blog factory enforces.

**`docs/brand.md` sections (name/slug still isolated to one block, in case of a *future* rename):**
- **Site identity** — `Name: Terminal Velocity`, a one-line **tagline** that describes the *content* not the name (e.g. something about learning agentic engineering by doing it inside a harness — lead with the doing-not-reading thesis, not a list of module names, per the Developer Evangelist review finding), parent brand (Hekton), and `slug: terminal-velocity`. The name/slug are kept in a single block, quarantined at the top, so a *future* rename stays mechanical the way this one was.
- **Voice** — adapt from the hekton-blog example: competent, specific, dryly funny, anti-hype, treats readers as capable peers (fits an advanced-practitioner audience). First person for build-log entries; system language for workshop structure.
- **Banned language** — reuse the blog-factory banned list verbatim (no em dashes; no delve/tapestry/unlock/seamless/game-changing/leverage-unless-load-bearing; no AI-slop openers). This keeps the workshop's prose consistent with the wider Hekton house style.
- **Minimal visual identity** — inherit the starter's neutral tokens rather than invent a palette: `--accent`, `ink`/`paper` Tailwind tokens, the `.post-body` typography rhythm, and the "no section dividers, whitespace only" layout rule. Record a short `[TBD]` checklist (accent colour, favicon/wordmark, dark mode) exactly as the hekton-blog example does.
- **Application map** — a short table stating which artifacts read from this file: `README.md` (title + tagline), `site/` `BaseLayout` (header wordmark + footer), `astro.config.mjs` (`site`/title), and the site's homepage copy.

Because the name lives in exactly one quarantined block and everything else is voice/visual/rules, any *future* rename would touch `docs/brand.md` (one block), `README.md` (title), and the site config `title` — a bounded, mechanical change, the same pattern that made this project's actual rename a same-day find-replace.

---

## 4. Build-log / GitHub Pages site

Adapt `blog-factory-lab/site-starters/astro-blog` into `site/`. Good news from exploration: **the AWS coupling is not in the starter** — it lives separately in `blog-factory-lab/infra/aws-static-site/`. The starter itself is a clean Astro 5 + MDX + React + Tailwind static site. So "stripping AWS" is mostly *not copying* the infra directory (which isn't in the starter anyway) and pointing the deploy at Pages instead.

### 4a. Copy vs. strip

**Copy into `site/`:**
- `package.json`, `package-lock.json`, `astro.config.mjs`, `tailwind.config.mjs`, `tsconfig.json`, `.gitignore` (the starter's — it already ignores `dist/`, `.astro/`, `node_modules/`).
- `src/components/layout/BaseLayout.astro`, `PostLayout.astro`.
- `src/pages/404.astro`.
- `src/styles/global.css` (the `.post-body` typography and neutral tokens — this *is* the visual identity per §3).
- `public/favicon.svg`.

**Strip / drop (not needed for a maintainer build-log):**
- `src/components/narrative/*` (`GremlinNote`, `DecisionLog`, `ArtefactBlock`, `NextEpisode`) and `src/components/interactive/PlaceholderInteractive.tsx` — these serve rich blog-series narratives. A dated build-log journal doesn't need them. Dropping React islands also lets you remove `@astrojs/react`, `react`, `react-dom`, `@types/react*` from `package.json` and the `react()` integration from `astro.config.mjs` (simpler build, fewer deps). **Keep `@astrojs/mdx`** so entries can use light Markdown/MDX. (If you'd rather keep the door open for one interactive demo later, retain React; default recommendation is drop it for now.)
- The demo post `src/content/posts/hello-factory.mdx` — replaced by the build-log collection below.
- Anything under `blog-factory-lab/infra/` — do not copy; the Pages workflow (§4c) replaces it.

**Rewrite for this project:**
- `BaseLayout.astro` header wordmark ("Blog Factory") and footer → "Terminal Velocity" title/tagline from `docs/brand.md`.
- `astro.config.mjs`: set `site` and `base` for GitHub Pages project hosting (see §4d).

### 4b. Surfacing dated build-log entries on the site

Entries live at `docs/build-log/YYYY-MM-DD-*.md` (this directory does not exist yet — the first entry creates it). The site must read them **without duplicating** them into `src/`.

**Primary approach — Astro 5 Content Layer `glob` loader pointed outside `src/`.** Replace the starter's legacy `src/content/config.ts` (`defineCollection({ type: "content" })`) with a Content Layer collection:
- Define a `buildlog` collection using `glob({ pattern: '*.md', base: '../docs/build-log' })` from `astro/loaders`, so the canonical entries in `docs/build-log/` are the single source and the site reads them in place.
- Schema (simpler than the blog's): `title: string`, `description: string`, `pubDate: z.coerce.date()`, `tags: string[] default []`, `draft: boolean default false`. Drop `series`/`seriesOrder`/`interactiveComponent`/`artefact`.
- Derive the entry slug from the filename date + title.

**Pages:**
- `src/pages/index.astro` → homepage: workshop tagline + a "Build log" heading listing entries newest-first (adapt the starter's `index.astro`, swap collection name `posts`→`buildlog`, drop the `/blog/` framing).
- `src/pages/build-log/[...slug].astro` → renders one entry via `PostLayout` (adapt the starter's `blog/[...slug].astro`; strip the `interactiveComponent`/`series` props).
- `src/pages/build-log/index.astro` → full dated index (adapt `blog/index.astro`).
- Keep `404.astro`.

**Fallback approach if the cross-`src` glob proves awkward:** a tiny prebuild copy step (`site/scripts/sync-build-log.mjs`) run in `npm run build`'s pre-step that copies `docs/build-log/*.md` into `site/src/content/build-log/` (git-ignored). Documented as fallback only; the glob loader keeps `docs/build-log/` as the one true home, which matches the Gremlin contract that entries are the maintainer's deliberate journal, not machine copies.

**Seed content:** one real first entry, `docs/build-log/2026-07-03-scaffolding-the-workshop.md`, written in the `docs/brand.md` voice (deliberate prose, not a `change-log.yaml` dump — the Gremlin's Risks section explicitly warns against auto-generated entries). This proves the collection renders and gives the site non-empty content for the build check.

### 4c. GitHub Actions deploy-pages workflow

New file `.github/workflows/deploy-pages.yml`.

- **Trigger (human-gate-respecting):** start with `workflow_dispatch:` **only** (plus a commented-out `push` block). This makes the first deploy a deliberate human action per the Human Gate ("first GitHub Pages deploy is human-confirmed, never automatic"), while the workflow itself is fully defined and testable. After the human confirms the first successful deploy, uncomment `push: branches: [main], paths: ['site/**', 'docs/build-log/**', '.github/workflows/deploy-pages.yml']` to make subsequent build-log updates auto-publish.
- **Permissions** (job-level, minimal): `contents: read`, `pages: write`, `id-token: write`.
- **Concurrency:** `group: "pages"`, `cancel-in-progress: false`.
- **Jobs:**
  - `build`: `actions/checkout@v4` → `actions/setup-node@v4` (node 20, `cache: npm`, `cache-dependency-path: site/package-lock.json`) → `npm ci` in `site/` → `npm run build` in `site/` → `actions/configure-pages@v5` → `actions/upload-pages-artifact@v3` with `path: site/dist`.
  - `deploy`: `needs: build`, `environment: { name: github-pages, url: ${{ steps.deployment.outputs.page_url }} }`, step `actions/deploy-pages@v4`.
- Alternative single-job form using `withastro/action@v3` (with `path: site/`) is acceptable and shorter; the explicit two-job form above is recommended for transparency since Astro-on-Pages is a new, unproven pattern for this factory (per the Gremlin's Risks note) and the maintainer will want to read each step.
- The repo-side enablement (Settings → Pages → Source: GitHub Actions) is itself part of the human deploy gate — note it in the plan, don't automate it.

### 4d. Astro config for Pages

GitHub project pages serve under `https://<user>.github.io/<repo>/`, so:
- `site: "https://coderturtle.github.io"` and `base: "/terminal-velocity/"` in `astro.config.mjs`, with an inline comment: `// If this repo is ever renamed again, update this base to match the new slug — it's the one spot that needs to change.`
- All internal links use Astro's `base`-aware helpers / root-relative `import.meta.env.BASE_URL` prefixing rather than bare `/build-log/...`, so a *future* rename would only touch this one config line, not every link. Call this out explicitly — it's the single most common Pages-project breakage.
- If a custom domain is chosen later, `base` returns to `/` and a `public/CNAME` is added; note as a future option, not this phase.

### 4e. `.gitignore`

The repo root `.gitignore` already ignores `node_modules/`, `dist/`, `build/`. Add `.astro/` (Astro's generated types) — the starter ignores it locally but the root ignore doesn't list it. Confirm `site/node_modules` and `site/dist` are covered (they are, via the un-anchored patterns).

---

## 5. Sequencing

Ordered by the Gremlin's own handoff contracts (`~/hekton/gremlins/workshop/workshop-gremlin.md` §Handoff Contracts): module shape must be decided before the site nav can mirror it; branding seeds both README and site.

1. **Module skeleton (§1)** — first; everything else references the module arc/nav. No dependencies. *(This is also the handoff artifact Coachgremlin later consumes.)*
2. **Brand layer `docs/brand.md` (§3)** — second; README and site both read from it. Name-agnostic, so it does not wait on the naming pass. Can run **in parallel** with §1.
3. **README rework (§2)** — after §1 and §3 exist (it links `modules/README.md` and pulls tagline from `docs/brand.md`).
4. **Site adaptation (§4a-4b) + first build-log entry** — after §1 (nav mirrors module structure) and §3 (voice/visual identity). The Astro scaffold copy (§4a) can start in parallel with §1/§3; the homepage/nav wiring (§4b) needs the module shape settled.
5. **Deploy workflow (§4c-4d)** — after the site builds locally. Workflow authoring can overlap with §4b.
6. **Human checkpoint (gate):** before any live deploy — enable Pages source in repo Settings and run the `workflow_dispatch` deploy **only on coderturtle's explicit confirmation**. Per Human Gate, the first Pages deploy is never automatic. Plan stops at "ready to deploy": workflow present, site builds, `workflow_dispatch`-only trigger, `push` trigger commented out.

**Parallelizable:** §1 ∥ §3 ∥ §4a (scaffold copy). **Strictly sequential:** §4b after §1; §2 after §1+§3; §4c/§4d after §4b builds; live deploy after human confirmation.

**Rename interaction:** none of steps 1-5 is blocked by the pending name. The naming pass and subsequent repo rename can happen before or after this phase; if after, the rename updates only the quarantined spots enumerated in §3/§4d.

---

## 6. Verification

Per step, all read-only/local until the human-gated deploy:

- **Module skeleton (§1):** `find modules -name README.md` lists 6 files; each stub contains its "question this module answers" line matching `docs/workshop-design.md`; `modules/README.md` lists all five in arc order. Markdown lint/preview renders.
- **README (§2):** manual read for the learner-first sections (prerequisites, how-to-start, arc); confirm internal Hekton framing fully relocated to `docs/maintainers.md` and no dead links (`grep` for `docs/` links, confirm targets exist).
- **Brand layer (§3):** confirm name/slug are the only rename-dependent fields (single quarantined block); banned-language list present; `grep` the new README and `site/` for any em dash or banned term to prove the layer is actually applied.
- **Site build (§4):** in `site/`, `npm ci` then `npm run build` exits 0 and emits `site/dist/` with the homepage + the seeded build-log entry rendered. `npx astro check` passes (types clean after the collection-schema swap). `npm run dev` spot-check that `/terminal-velocity/` base-pathed links resolve.
- **Build-log wiring (§4b):** the seeded `docs/build-log/2026-07-03-*.md` appears on the built homepage and at its `build-log/<slug>/` route — proving the glob loader reads `docs/build-log/` in place (no duplicated copy in `src/`).
- **Workflow (§4c):** YAML validity via `actionlint` (or `python -c 'import yaml,sys; yaml.safe_load(open(...))'`); confirm permissions block is `pages: write` + `id-token: write`, trigger is `workflow_dispatch`-only with `push` commented, and artifact path is `site/dist`. No live run until the human gate.
- **Mirror drift (house rule):** after adding decisions/session-log entries for this phase, `scripts/check-mirror-drift.sh --check` must exit 0 — i.e. update the repo-local mirror at `mind-palace/20-projects/factory-output/terminal-velocity/` (`decisions.md`, `session-log.md`, `index.md`) to match new `docs/` rows. This is the repo-local mirror (not the live vault), so it's writable under `vault_mutation_allowed: false`.
- **Project scaffold integrity:** `scripts/verify-project.sh` still passes after the new top-level `modules/`, `site/`, and `.github/` directories are added.

## Critical files referenced

- `README.md`, `docs/workshop-design.md`, `docs/workshop-gremlin-design.md`
- `~/hekton/gremlins/workshop/workshop-gremlin.md`
- `<hekton>/labs/blog-factory-lab/site-starters/astro-blog/astro.config.mjs`
- `<hekton>/labs/blog-factory-lab/site-starters/astro-blog/src/content/config.ts`
- `<hekton>/labs/blog-factory-lab/templates/brand-style-layer-template.md`
