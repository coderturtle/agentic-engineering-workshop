# Next Actions: Agentic Engineering Workshop

## Immediate

- [x] Resolve GitHub push credential (was `IdentitiesOnly` missing on the `github.com-coderturtle` SSH alias) — fixed 2026-07-03, `main` pushed.
- [x] Produce an implementation plan for the next phase (deliverables/branding + build-log/Pages publisher) — `docs/implementation-plan.md`, produced via an Opus-run planning pass, reflecting the revised four-module arc.
- [ ] Run the Workshop Gremlin's naming agent against this project's idea/audience and have coderturtle choose the final workshop name from candidates.
- [ ] Rename the repo (local + GitHub) once the name is chosen; update `.hekton/project.yaml`, README, and both design docs' "working title" references.

## This Week

- [ ] Execute `docs/implementation-plan.md` §1: module directory skeleton (`modules/01-prompt-engineering/` … `05-synthesis-capstone/`, each a structure-only README stub).
- [ ] Execute §3: `docs/brand.md` brand layer (name/slug quarantined to one block, adapted from blog-factory-lab's brand-style-layer template).
- [ ] Execute §2: rework top-level `README.md` for a learner audience; relocate internal Hekton framing to `docs/maintainers.md`.
- [ ] Execute §4: adapt `blog-factory-lab/site-starters/astro-blog` into `site/`, wire up `docs/build-log/` via a Content Layer `glob` loader, write the first build-log entry, add `.github/workflows/deploy-pages.yml` (`workflow_dispatch`-only trigger — no live deploy without explicit human confirmation per the Human Gate).
- [ ] Verify per `docs/implementation-plan.md` §6 (site build, workflow YAML validity, mirror-drift check) before treating the phase as done.

## Later

- [ ] Content-building run: invoke Coachgremlin once per concept (prompt engineering, context engineering, harness engineering, loop engineering, synthesis capstone) to produce exercise specs + rubrics, drawing on the sourced patterns in `docs/workshop-design.md` (Ticket-to-PR-Ready, Restartable Handoff, the "ralph loop").
- [ ] After this workshop ships, revise `~/hekton/gremlins/workshop/workshop-gremlin.md` and `~/hekton/gremlins/coaching/coachgremlin.md` from real experience and bump both from draft to v0.
- [ ] Register both Gremlins in the mind-palace Gremlin Registry (vault mutation currently deferred — needs explicit authorisation).
