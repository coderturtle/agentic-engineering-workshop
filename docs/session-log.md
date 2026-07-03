# Session Log: Terminal Velocity

> Renamed from "Agentic Engineering Workshop" on 2026-07-03. Entries dated before the rename refer to the project by its working name at the time — left as-is for historical accuracy.

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

## 2026-07-03 - Implementation plan for deliverables/branding + Pages publisher (Opus)

Ran an Opus-model Plan agent (read-only; no Write/Edit access) to design the next phase, given the newly revised four-module arc. It read `docs/workshop-design.md`, `docs/workshop-gremlin-design.md`, `~/hekton/gremlins/workshop/workshop-gremlin.md`, and `blog-factory-lab`'s Astro starter before planning.

### What changed

- `docs/implementation-plan.md` (new) — module-skeleton layout, learner-facing README rework, a name-agnostic `docs/brand.md` brand layer, and a detailed Astro-on-GitHub-Pages adaptation of blog-factory-lab's starter (found that the AWS coupling lives outside the starter, in `blog-factory-lab/infra/`, so no stripping needed there), plus a `workflow_dispatch`-only deploy workflow respecting the Human Gate. Includes sequencing and per-step verification.
- `docs/decisions.md`, `docs/next-actions.md` — recorded the plan and converted next actions into concrete execution steps against the plan's section numbers.

### Decisions Made

See `docs/decisions.md`, 2026-07-03 "Produced docs/implementation-plan.md" entry.

### Next Actions

- Execute `docs/implementation-plan.md` §1-§5 (module skeleton, brand layer, README rework, site adaptation, deploy workflow), verify per §6.
- Naming pass (Workshop Gremlin naming agent) — next up.

## 2026-07-03 - Naming pass: renamed to Terminal Velocity

Ran the naming pass: generated candidates (Terminal Velocity, Loop Native, Bounded Autonomy, Prompt → Loop), checked slug availability under `coderturtle` via `gh api`, presented to coderturtle who chose **Terminal Velocity**.

### What changed

- GitHub repo renamed `agentic-engineering-workshop` → `terminal-velocity` (`gh repo rename`; old URL auto-redirects, PR #1 and issues intact).
- Local directory renamed to match; git remote `origin` updated to `git@github.com-coderturtle:coderturtle/terminal-velocity.git`; `git fetch` confirmed clean.
- Repo-local mind-palace mirror folder renamed (`mind-palace/20-projects/factory-output/terminal-velocity/`).
- `.hekton/project.yaml`, `CLAUDE.md`, `CODEX.md`, `AGENTS.md`, `README.md`, and all current-state docs/scaffold files updated to the new name via a scoped find-replace (excluding `docs/decisions.md`/`docs/session-log.md` and their mirrors, which keep historical rows under the old name and got a title-line + new-entry treatment instead).
- `docs/implementation-plan.md`'s rename-dependent spots (Astro `site`/`base` config) updated to the real slug.

### Decisions Made

See `docs/decisions.md`, 2026-07-03 "Naming pass complete" entry.

### Risks / Open Items

- The **live** Obsidian vault card (`~/vaults/hekton-mind-palace/20-projects/factory-output/agentic-engineering-workshop/`) still exists under the old path — vault mutation is not authorised in this session, so it was not moved/renamed. This mirrors a known prior pattern in this factory (the PulseGremlin rename, 2026-06-21, per `~/hekton/docs/decisions.md`) where a rename's vault mirror was left to drift. Flagging explicitly here so it doesn't repeat silently — see `docs/next-actions.md`.
- `~/hekton`'s `scripts/pm/brain-registry.json` entry and `~/hekton/gremlins/workshop/workshop-gremlin.md`'s "First Run" section still reference the old project name/paths — updating those in the same session (see `~/hekton` session log / decisions for that repo).

### Next Actions

- Human-authorize a vault card move/rename for the live Obsidian vault (out of session scope until then).
- Proceed to executing `docs/implementation-plan.md`.
