# Terminal Velocity

**Classification:** factory-output
**Lifecycle:** active
**Owner:** coderturtle
**Promotion target:** `none`

> Public workshop teaching the evolution from prompt engineering to context engineering to loop engineering, taught by leveraging agents and harnesses as the learning method itself.

This repo has two goals:

1. **Ship a workshop** teaching how prompt engineering, context engineering, and loop engineering fit together as of today — for practitioners already using coding agents daily — taught by running every exercise through a real harness (Claude Code, Codex, etc.) rather than reading about it.
2. **Extract the reusable machinery** for building future workshops: a **Workshop Gremlin** (deterministic scaffolding, naming, deliverables/branding, build-log publishing) and **Coachgremlin** (the reusable, harness-native teaching agent), both added to the Hekton factory (`~/hekton/gremlins/`) for reuse beyond this one workshop.

Working title while the Workshop Gremlin's naming agent runs: **"Prompt → Loop"**.

## Implementation Status

- 2026-07-03 — Scaffolded as factory-output. Both design tracks complete: see [Workshop Design](docs/workshop-design.md) (the workshop itself, now a four-module arc — prompt / context / harness / loop engineering — plus synthesis capstone) and [Workshop Gremlin Design](docs/workshop-gremlin-design.md) (the reusable machinery). Gremlin definitions live at `~/hekton/gremlins/workshop/workshop-gremlin.md` and `~/hekton/gremlins/coaching/coachgremlin.md`.
- [Implementation Plan](docs/implementation-plan.md) for the next phase (module skeleton, brand layer, README rework, build-log/Pages site) is written, not yet executed.
- Next: naming pass, then execute the implementation plan (see `docs/next-actions.md`).

## Documentation Contract

Agents working here must inspect `.hekton/project.yaml` before structural changes, keep `docs/session-log.md` current, record meaningful design decisions in `docs/decisions.md`, and update `docs/next-actions.md` when the work queue changes.

Vault mutation is not allowed by default. The repo-local `mind-palace/` folder is only a mirror draft; do not write to the live vault unless explicitly authorised in-session.

## Quick Start

```bash
# Add project-specific commands here
```

## Key Docs

- [Workshop Design](docs/workshop-design.md) — audience, format, teaching method, module arc
- [Workshop Gremlin Design](docs/workshop-gremlin-design.md) — reusable Gremlin/Coachgremlin decisions
- [Implementation Plan](docs/implementation-plan.md) — module skeleton, brand layer, README rework, build-log/Pages site (planned, not yet executed)
- [Session Log](docs/session-log.md)
- [Decisions](docs/decisions.md)
- [Risks](docs/risks.md)
- [Project Walkthrough](docs/project-walkthrough.md)
- [Next Actions](docs/next-actions.md)
- [Operating Model](docs/operating-model.md)
- [Human Understanding Check](docs/human-understanding-check.md)
- [Depth Decision](docs/depth-decision.md)
- [Retire / Promote Review](docs/retire-promote-review.md)
