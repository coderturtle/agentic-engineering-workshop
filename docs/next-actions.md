# Next Actions: Agentic Engineering Workshop

## Immediate

- [x] Resolve GitHub push credential (was `IdentitiesOnly` missing on the `github.com-coderturtle` SSH alias) — fixed 2026-07-03, `main` pushed.
- [ ] Produce an implementation plan for the next phase (deliverables/branding + build-log/Pages publisher), planned via an Opus-run planning pass, reflecting the revised four-module arc.
- [ ] Run the Workshop Gremlin's naming agent against this project's idea/audience and have coderturtle choose the final workshop name from candidates.
- [ ] Rename the repo (local + GitHub) once the name is chosen; update `.hekton/project.yaml`, README, and both design docs' "working title" references.

## This Week

- [ ] Deliverables & branding step: module directory skeleton (prompt / context / harness / loop engineering / capstone), learner-facing README, brand layer (name, tagline, voice).
- [ ] Build-log/Pages publisher step: adapt blog-factory-lab's Astro starter, add the GitHub Actions `deploy-pages` workflow, write the first build-log entry.
- [ ] Validate one real GitHub Pages deploy end-to-end before treating the publishing pipeline as proven.

## Later

- [ ] Content-building run: invoke Coachgremlin once per concept (prompt engineering, context engineering, harness engineering, loop engineering, synthesis capstone) to produce exercise specs + rubrics, drawing on the sourced patterns in `docs/workshop-design.md` (Ticket-to-PR-Ready, Restartable Handoff, the "ralph loop").
- [ ] After this workshop ships, revise `~/hekton/gremlins/workshop/workshop-gremlin.md` and `~/hekton/gremlins/coaching/coachgremlin.md` from real experience and bump both from draft to v0.
- [ ] Register both Gremlins in the mind-palace Gremlin Registry (vault mutation currently deferred — needs explicit authorisation).
