# Next Actions: Terminal Velocity

## Immediate

- [x] Resolve GitHub push credential (was `IdentitiesOnly` missing on the `github.com-coderturtle` SSH alias) — fixed 2026-07-03, `main` pushed.
- [x] Produce an implementation plan for the next phase (deliverables/branding + build-log/Pages publisher) — `docs/implementation-plan.md`, produced via an Opus-run planning pass, reflecting the revised four-module arc.
- [x] Run the Workshop Gremlin's naming agent — chose **Terminal Velocity**. Repo, local dir, mind-palace mirror (repo-local and live vault) all renamed 2026-07-03.
- [x] Design + test-run the Workshop Review Panel (7 personas) against this project's current design docs — `~/hekton/gremlins/workshop/workshop-review-panel.md`; report at `docs/review-panel/2026-07-03-initial-design.md`. Fixes from that run applied directly to README.md, docs/workshop-design.md, docs/workshop-gremlin-design.md, docs/implementation-plan.md.

## This Week

- [x] Execute `docs/implementation-plan.md` §1: module directory skeleton (`modules/01-prompt-engineering/` … `05-synthesis-capstone/`, each a structure-only README stub, plus `modules/README.md` index with the loop taxonomy). Module 02's exercise-anchor gap closed.
- [x] Execute §3: `docs/brand.md` brand layer. Real name throughout; hard rules (no em dash, no unqualified efficacy claims) written directly in response to the review panel's Skeptical Critic findings.
- [x] Execute §2: reworked top-level `README.md` for a learner audience with a literal copy-pasteable clone command; relocated internal Hekton framing to `docs/maintainers.md`.
- [x] Execute §4: adapted `blog-factory-lab/site-starters/astro-blog` into `site/` (dropped React/narrative components per the plan, kept MDX), wired `docs/build-log/` via an Astro 5 Content Layer `glob` loader (entries stay in `docs/build-log/`, not duplicated into `src/`), wrote the first build-log entry, added `.github/workflows/deploy-pages.yml` (`workflow_dispatch`-only trigger, `push` commented out — no live deploy without explicit human confirmation per the Human Gate).
- [x] Verified per `docs/implementation-plan.md` §6: `npm run build` and `npx astro check` both clean; seed entry renders on the homepage and its own route with the correct `/terminal-velocity/` base path; workflow YAML validated; no em dashes or banned phrases in published content; all README/modules links resolve; mirror-drift and `verify-project.sh` clean.

## Later

- [x] **Hands-on-by-design retrofit**: added a "Required to advance" gate to all 5 module READMEs plus `modules/README.md`'s arc table, per coderturtle's direction that every workshop must require the learner to produce/demonstrate something, never just read. Now a standing principle in `~/hekton/gremlins/workshop/workshop-gremlin.md`'s Design Principles, not just this workshop's choice.
- [x] Fixed a pre-existing em-dash violation across `modules/` and `README.md` (written before `docs/brand.md`'s hard rules existed) — published content is now clean.
- [ ] **Human-confirm the first GitHub Pages deploy**: enable Pages (Settings → Source: GitHub Actions) on the repo, then manually run the `workflow_dispatch` workflow. Only after that succeeds, uncomment the `push` trigger in `.github/workflows/deploy-pages.yml` for future auto-publish.
- [ ] Content-building run: invoke Coachgremlin once per concept (prompt engineering, context engineering, harness engineering, loop engineering, synthesis capstone) to produce exercise specs + rubrics that satisfy each module's stated gate, drawing on the sourced patterns in `docs/workshop-design.md` (Ticket-to-PR-Ready, Restartable Handoff, the "ralph loop") and the review panel's deferred content-building guidance (harness-agnostic exercise design, cumulative-not-independent exercises, module-4 exercise budget, capstone concreteness pulled earlier — see `docs/review-panel/2026-07-03-initial-design.md`).
- [ ] Run the Workshop Review Panel again once module content exists (it can only meaningfully evaluate design docs so far, per its own persona findings) — this run should also verify each module's actual exercise satisfies its stated gate, not just that a gate is written.
- [ ] **Backlogged, not scoped**: agent-native workshop interaction (see `docs/workshop-design.md`'s "Backlogged" section and `~/hekton/gremlins/workshop/workshop-gremlin.md`'s "Future Direction"). Needs its own design pass before it's a real next action.
- [ ] Coachgremlin's first real run (any concept) is the next Gremlin still needing evidence behind its draft status.
- [ ] Register all three Gremlins in the mind-palace Gremlin Registry (vault mutation currently deferred beyond this project's own card — needs explicit authorisation for the registry file itself).
- [ ] Consider running `npm audit` on `site/`'s dependencies before the first real deploy (4 vulnerabilities reported at install time, inherited from the blog-factory-lab starter, not yet triaged).
