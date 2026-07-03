# Maintainers

This is the internal/agent-facing doc. Learners should read the top-level `README.md` instead; this file is for anyone working on the workshop itself.

**Classification:** factory-output
**Lifecycle:** active
**Owner:** coderturtle
**Promotion target:** `none`

This repo has two goals:

1. **Ship a workshop** teaching how prompt engineering, context engineering, harness engineering, and loop engineering fit together as of today, for practitioners already using coding agents daily, taught by running every exercise through a real harness rather than reading about it.
2. **Extract the reusable machinery** for building future workshops: a **Workshop Gremlin** (deterministic scaffolding, naming, review panel, deliverables/branding, build-log publishing) and **Coachgremlin** (the reusable, harness-native teaching agent), both added to the Hekton factory (`~/hekton/gremlins/`) for reuse beyond this one workshop.

## Implementation Status

- 2026-07-03 — Scaffolded as factory-output. Both design tracks complete: see [Workshop Design](workshop-design.md) (the workshop itself, a four-module arc plus synthesis capstone) and [Workshop Gremlin Design](workshop-gremlin-design.md) (the reusable machinery). Gremlin definitions live at `~/hekton/gremlins/workshop/workshop-gremlin.md`, `~/hekton/gremlins/coaching/coachgremlin.md`, and `~/hekton/gremlins/workshop/workshop-review-panel.md`.
- Naming pass complete (Terminal Velocity). First [Workshop Review Panel](review-panel/2026-07-03-initial-design.md) run complete against the design docs, findings applied.
- [Implementation Plan](implementation-plan.md) executing now: module skeleton, brand layer, README rework, build-log/Pages site.

## Documentation Contract

Agents working here must inspect `.hekton/project.yaml` before structural changes, keep `docs/session-log.md` current, record meaningful design decisions in `docs/decisions.md`, and update `docs/next-actions.md` when the work queue changes.

Vault mutation is not allowed by default. The repo-local `mind-palace/` folder is only a mirror draft; do not write to the live vault unless explicitly authorised in-session.

## Voice and style for published content

Anything a learner reads (README, module content, build-log entries, the site) follows `docs/brand.md` — voice, hard rules (no em dashes, no unqualified efficacy claims), banned phrases. Internal docs under `docs/` are working documents and are exempt.

## Key Docs

- [Workshop Design](workshop-design.md) — audience, format, teaching method, module arc
- [Workshop Gremlin Design](workshop-gremlin-design.md) — reusable Gremlin/Coachgremlin decisions
- [Implementation Plan](implementation-plan.md) — module skeleton, brand layer, README rework, build-log/Pages site
- [Agent-Native Interaction Plan](agent-native-interaction-plan.md) — researched, not built: options considered, recommended module-03 pilot, Human Gate extension for agent-submitted attempts
- [Brand / Style Layer](brand.md) — voice, hard rules, visual identity
- [Workshop Review Panel Report](review-panel/2026-07-03-initial-design.md) — 7-persona critique of the design docs, first test run
- [Session Log](session-log.md)
- [Decisions](decisions.md)
- [Risks](risks.md)
- [Project Walkthrough](project-walkthrough.md)
- [Next Actions](next-actions.md)
- [Operating Model](operating-model.md)
- [Human Understanding Check](human-understanding-check.md)
- [Depth Decision](depth-decision.md)
- [Retire / Promote Review](retire-promote-review.md)
