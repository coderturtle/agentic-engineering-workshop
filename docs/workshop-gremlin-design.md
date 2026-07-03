# Workshop Gremlin — Design (Track A)

> Canonical definitions live in `~/hekton/gremlins/workshop/workshop-gremlin.md` and `~/hekton/gremlins/coaching/coachgremlin.md`. This doc is the record of *why* they're shaped the way they are, produced by interviewing coderturtle while scaffolding this workshop.

## Why this exists

This workshop has two goals, not one: ship a specific workshop, and extract the reusable machinery for building future workshops without re-deriving it each time. Building the machinery *as* the workshop is built keeps the abstraction honest — it's shaped by one real run before being asked to generalize.

## What got designed

### Workshop Gremlin (Tier 3, Type B, scope: cross-project)

A designed (not earned) multi-agent Gremlin per the Hekton Gremlin Model's Path B. Its job: turn a workshop idea into a scaffolded, named, branded, publishable repo. It stops before content exists.

Roster: Scaffolding step (wraps Quartergremlin), Workshop Naming agent, Deliverables & branding agent, Build-log/Pages publisher agent, and a defined (not owned) handoff to Coachgremlin for content-building later.

Full roster, handoffs, completion condition, and human gates: `~/hekton/gremlins/workshop/workshop-gremlin.md`.

### Coachgremlin (Tier 3, Type A, scope: cross-project)

The reusable teaching agent — deliberately *not* a Tier 2 factory agent, because teaching a workshop learner is a domain artefact of the project being taught, not an operation on Hekton itself. It teaches by putting the learner inside a bounded, harness-driven exercise against a rubric, then gives feedback on the actual attempt. It does not lecture and does not hand over solutions.

Full definition: `~/hekton/gremlins/coaching/coachgremlin.md`.

## Key decisions

| Decision | Choice | Why |
|---|---|---|
| Coachgremlin's tier | Tier 3, cross-project (not Tier 2 factory agent) | Tier 2 agents operate *on* Hekton itself (scaffolding, reviewing Hekton's own docs). Teaching a learner is a domain output of the project being taught — that's Tier 3 by the model's own definition, even though it's reusable across many projects. |
| Publishing approach | Astro (adapted from blog-factory-lab's starter) deployed via GitHub Actions `deploy-pages` | User explicitly wants GitHub Pages, not the existing AWS S3/CloudFront pattern blog-factory-lab targets. Reuses the Astro starter and brand-layer pattern without pulling in AWS. |
| Scaffolding approach | Wrap Quartergremlin (`scaffold-project.sh`) rather than a standalone scaffolder | Quartergremlin already produces a validated, classified Hekton container (`.hekton/`, docs, mind-palace mirror, GitHub remote per privacy policy). Reinventing that would duplicate proven machinery for no benefit. |
| Where the Gremlin lives | Factory scope (`~/hekton/gremlins/`) from the start, not lab-born-then-promoted | User's explicit intent was "add it to the hekton factory to reuse going forward" — defining it at factory scope from birth matches that intent directly, even though the strict Gremlin Model path for new capability is usually lab-born-then-promoted. This workshop's build is the Gremlin's first run (draft → v0 once complete). |
| Naming agent as a required deliverable | Yes — not cosmetic | The user explicitly asked for a workshop-naming agent as part of the Gremlin, and for this workshop's own name to come out of that process rather than being picked ad hoc. |

## Human gates (non-negotiable across both)

- The human picks the final workshop name from the naming agent's candidates — no auto-selection.
- First push of a public repo, and first GitHub Pages deploy, are human-confirmed actions.
- Coachgremlin never certifies a learner "complete" for anything with external consequence without human confirmation of the rubric result.

## Status and what's left

Both definitions are **draft**. This workshop (`terminal-velocity`) is the Workshop Gremlin's first end-to-end run — repo scaffolding, naming (complete: **Terminal Velocity**), and a first Workshop Review Panel test run are done; deliverables/branding and the build-log/Pages publisher are the open next actions (see `docs/next-actions.md`). Once this run completes, both Gremlin definitions should be revised from real experience and versioned up per the model's rules (major bump for roster changes, minor for prompt/contract changes within a fixed roster).
