# Session Log: Agentic Engineering Workshop

## 2026-07-03 - Initial scaffold

Project scaffolded as **factory-output**. Purpose: Public workshop teaching the evolution from prompt engineering to context engineering to loop engineering, taught by leveraging agents and harnesses as the learning method itself.

### Decisions Made

- Classification: factory-output
- Owner: coderturtle
- Vault mutation: not allowed by default
- Promotion target: none

### Next Actions

- Define brief and first phase plan
- Add first implementation
- Record initial decisions

## 2026-07-03 - Two-track design pass (Workshop Gremlin + this workshop)

Ran two design/interview tracks per the project's founding intent: (A) the reusable Workshop Gremlin + Coachgremlin, (B) this specific workshop's content/format/name.

### What changed

- `docs/workshop-gremlin-design.md` (new) — Track A output: Workshop Gremlin + Coachgremlin decisions and rationale.
- `docs/workshop-design.md` (new) — Track B output: audience, format, agent-native teaching method, three-part module arc + synthesis capstone, working title.
- `~/hekton/gremlins/workshop/workshop-gremlin.md` (new, in `~/hekton`) — Tier 3 Type B Gremlin definition, draft.
- `~/hekton/gremlins/coaching/coachgremlin.md` (new, in `~/hekton`) — Tier 3 Type A Gremlin definition, draft.
- `~/hekton/agents/index.md` — registered both under a new "Cross-Project Gremlins" section.
- `labs/hekton-cli-lab` — extended the Hekton commit signature with `Hekton-Harness`/`Hekton-Model` trailers (done in an isolated worktree; see Decisions and Risks).
- README, `docs/next-actions.md`, `docs/decisions.md` updated from scaffold placeholders to real content.

### Decisions Made

See `docs/decisions.md` for the full list (audience, format, teaching method, Coachgremlin tier, Gremlin home, publishing approach, naming-as-deliverable, commit signature extension).

### Risks / Open Items

- GitHub push still blocked on a credential mismatch (see `docs/risks.md`) — repo is local-only.
- `hekton-cli-lab`'s primary checkout has unrelated pre-existing uncommitted WIP from another session; the commit-signature change was made in an isolated git worktree instead, to avoid touching that dirty tree.

### Next Actions

- See `docs/next-actions.md` — naming pass, deliverables/branding, build-log/Pages publisher, then Coachgremlin content-building.

## 2026-07-03 - Harness engineering research pass + module arc revision

Reviewed three external sources on loop engineering (Forward Future's Loop Library, LangChain's "Art of Loop Engineering," CodeRabbit's Loop Engineering post) at the user's request, to check for angles the workshop design was missing before the naming pass.

### What changed

- `docs/workshop-design.md` — split the module arc from three to four core modules: prompt engineering, context engineering, **harness engineering** (new), loop engineering, plus the synthesis capstone (now four-way, not three-way). Added: our own synthesis of how harness engineering evolved into loop engineering (structural "what can it reach" vs. behavioral "when does it stop/how does it improve"); a four-layer loop taxonomy (agent / verification / event-driven / hill-climbing) for the loop module; the stable-goal-vs-moving-target decision rule as a teachable rubric item; named real-world patterns (Ticket-to-PR-Ready, Restartable Handoff, the "ralph loop") earmarked as source material for Coachgremlin exercises; a Sources section citing all three articles.
- `docs/decisions.md` — recorded the arc-split decision and its rationale.

### Decisions Made

See `docs/decisions.md`, 2026-07-03 "Split the arc from three modules to four" entry.

### Next Actions

- Implementation plan for the next phase (deliverables/branding + build-log/Pages publisher), to be produced by an Opus-run planning pass — see follow-up entry.
- Naming pass after the implementation plan is in hand.
