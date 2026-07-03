# Next Actions: Terminal Velocity

## Immediate

- [x] Resolve GitHub push credential (was `IdentitiesOnly` missing on the `github.com-coderturtle` SSH alias) — fixed 2026-07-03, `main` pushed.
- [x] Produce an implementation plan for the next phase (deliverables/branding + build-log/Pages publisher) — `docs/implementation-plan.md`, produced via an Opus-run planning pass, reflecting the revised four-module arc.
- [x] Run the Workshop Gremlin's naming agent — chose **Terminal Velocity**. Repo, local dir, mind-palace mirror (repo-local and live vault) all renamed 2026-07-03.
- [x] Design + test-run the Workshop Review Panel (7 personas) against this project's current design docs — `~/hekton/gremlins/workshop/workshop-review-panel.md`; report at `docs/review-panel/2026-07-03-initial-design.md`. Fixes from that run applied directly to README.md, docs/workshop-design.md, docs/workshop-gremlin-design.md, docs/implementation-plan.md.

## This Week

- [ ] Execute `docs/implementation-plan.md` §1: module directory skeleton (`modules/01-prompt-engineering/` … `05-synthesis-capstone/`, each a structure-only README stub). Module 02 now has an exercise-pattern anchor (context-budget curation exercise) per the review panel's Instructional Designer finding.
- [ ] Execute §3: `docs/brand.md` brand layer (real name "Terminal Velocity", quarantined in one block for any future rename; adapted from blog-factory-lab's brand-style-layer template).
- [ ] Execute §2: rework top-level `README.md` for a learner audience with a literal copy-pasteable Quick Start command block (per the review panel's Developer Evangelist finding); relocate internal Hekton framing to `docs/maintainers.md`.
- [ ] Execute §4: adapt `blog-factory-lab/site-starters/astro-blog` into `site/`, wire up `docs/build-log/` via a Content Layer `glob` loader, write the first build-log entry, add `.github/workflows/deploy-pages.yml` (`workflow_dispatch`-only trigger — no live deploy without explicit human confirmation per the Human Gate).
- [ ] Verify per `docs/implementation-plan.md` §6 (site build, workflow YAML validity, mirror-drift check) before treating the phase as done.

## Later

- [ ] Content-building run: invoke Coachgremlin once per concept (prompt engineering, context engineering, harness engineering, loop engineering, synthesis capstone) to produce exercise specs + rubrics, drawing on the sourced patterns in `docs/workshop-design.md` (Ticket-to-PR-Ready, Restartable Handoff, the "ralph loop") and the review panel's deferred content-building guidance (harness-agnostic exercise design, cumulative-not-independent exercises, module-4 exercise budget, capstone concreteness pulled earlier — see `docs/review-panel/2026-07-03-initial-design.md`).
- [ ] Run the Workshop Review Panel again once module content exists (it can only meaningfully evaluate design docs so far, per its own persona findings).
- [ ] After this workshop ships, revise `~/hekton/gremlins/workshop/workshop-gremlin.md`, `~/hekton/gremlins/coaching/coachgremlin.md`, and `~/hekton/gremlins/workshop/workshop-review-panel.md` from real experience and bump all three from draft to v0.
- [ ] Register all three Gremlins in the mind-palace Gremlin Registry (vault mutation currently deferred beyond this project's own card — needs explicit authorisation for the registry file itself).
