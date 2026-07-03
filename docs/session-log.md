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

## 2026-07-03 - Live vault card moved (explicit authorization given)

coderturtle explicitly authorized moving the live Obsidian vault card for this project (a one-time authorization, not a standing permission).

### What changed

- `~/vaults/hekton-mind-palace/20-projects/factory-output/agentic-engineering-workshop/` moved to `.../terminal-velocity/`; `index.md`/`session-log.md` frontmatter and content updated to match.
- `just validate-projects` re-run: the "local repo not found" warning this rename had introduced is gone; project now reports clean as `terminal-velocity` throughout.

### Next Actions

- See review-panel entry below — ran alongside this.

## 2026-07-03 - Workshop Review Panel: designed, test-run, wired findings back in

Designed a 7-persona Workshop Review Panel (AI/ML Practitioner, Developer Evangelist, End-User/Learner, Professional Technical Writer, Skeptical Critic, Instructional Designer, Security-Conscious Reviewer) per coderturtle's request, at `~/hekton/gremlins/workshop/workshop-review-panel.md`. Test-ran it against this project's own current design docs before wiring it into the Workshop Gremlin's roster, per the Gremlin Model's "draft until run end-to-end once" discipline.

### What changed

- Ran all seven personas independently and in parallel against `README.md`, `docs/workshop-design.md`, `docs/workshop-gremlin-design.md`, `docs/implementation-plan.md`. Synthesized into `docs/review-panel/2026-07-03-initial-design.md`; raw per-persona critiques preserved in `docs/review-panel/2026-07-03-personas/`.
- Two cross-persona agreements: (1) stale "naming pending" prose survived the earlier rename's find-replace in all four current-state docs, since the prose never contained the old name as a literal string; (2) an unreconciled contradiction between "harness engineering is static" and "hill-climbing rewrites the harness," plus a missing human-review caveat on hill-climbing (independently flagged by the AI/ML Practitioner on technical-correctness grounds and the Security-Conscious Reviewer on safety grounds).
- Five single-persona findings, each real and not overlapping with another lens: unsupported/overclaiming language (Skeptical Critic, 5 instances); a missing exercise-pattern anchor for module 2 (Instructional Designer); no exercise yet exists to evaluate the core promise against (End-User/Learner); harness vocabulary possibly too Claude-Code-specific (End-User/Learner); Coachgremlin's grading trustworthiness is asserted, not shown (End-User/Learner).
- Applied fixes for everything fixable at the design-doc stage directly to the four reviewed docs (see `docs/decisions.md`). Deferred the content-building-only findings to `docs/next-actions.md`.

### Decisions Made

See `docs/decisions.md`, 2026-07-03 "Designed and test-ran a Workshop Review Panel" entry.

### Risks / Open Items

- The panel is real cost (7 parallel passes) — reserve full-panel runs for design-level checkpoints, not routine edits, per the Gremlin's own Risks section.
- Panel hasn't been run against actual module content yet (none exists) — several findings (exercise design, grader trust) can only be re-checked once content-building happens.

### Next Actions

- Wire the Workshop Review Panel into `~/hekton/gremlins/workshop/workshop-gremlin.md`'s roster as a new step (see that repo's session log/decisions for the update).
- Re-run the panel once module content exists.

## 2026-07-03 - Executed the implementation plan (§1-§4)

Executed `docs/implementation-plan.md` end to end: module skeleton, brand layer, README rework, and the Astro-on-GitHub-Pages build-log site. Stopped at "ready to deploy" per the Human Gate: no live Pages deploy without explicit confirmation.

### What changed

- `modules/`: 5 structure-only module READMEs (`01-prompt-engineering` … `05-synthesis-capstone`) plus `modules/README.md` (arc index + loop taxonomy table). Each stub states the question it answers, its position in the arc, placeholder learning objectives, a pointer to real exercise material (not a spec), and a "skeleton only" banner.
- `docs/brand.md`: name-agnostic-in-structure brand layer (name/slug already real: Terminal Velocity), adapted from blog-factory-lab's brand-style-layer template. Hard rules include no em dashes and no unqualified efficacy claims, a direct and permanent response to the Workshop Review Panel's Skeptical Critic findings, not a one-time fix.
- `README.md`: rewritten as a learner-facing landing page (what/who it's for, prerequisites, literal copy-pasteable clone command, how the modules connect, the teaching method, build-in-public note). Internal Hekton scaffold framing (classification, documentation contract, vault-mutation note) relocated to new `docs/maintainers.md`.
- `site/`: adapted from `blog-factory-lab/site-starters/astro-blog`. Dropped React and the narrative components (`GremlinNote`, `DecisionLog`, etc.) since a maintainer build-log doesn't need them; kept MDX. Build-log entries live in `docs/build-log/` and are read in place via an Astro 5 Content Layer `glob` loader (`site/src/content/config.ts`), not duplicated into `src/`. Wrote the first real entry, `docs/build-log/2026-07-03-scaffolding-the-workshop.md`, in the brand voice.
- `.github/workflows/deploy-pages.yml`: `workflow_dispatch`-only trigger, `push` trigger written but commented out, minimal permissions (`contents: read`, `pages: write`, `id-token: write`), builds `site/` and deploys `site/dist` via `actions/deploy-pages@v4`.
- `.gitignore`: added `.astro/` (was missing; `node_modules/`/`dist/` already covered).

### Decisions Made

See `docs/decisions.md`, 2026-07-03 "Executed docs/implementation-plan.md §1-§4" entry.

### Validation

- `npm install` + `npm run build` in `site/`: 4 pages built clean.
- `npx astro check`: 0 errors, 0 warnings, 0 hints.
- Confirmed the seed build-log entry renders on the homepage and at its own route with the correct `/terminal-velocity/` base path.
- Workflow YAML parsed and structure-checked via `npx js-yaml`.
- Grepped README/site/build-log/modules for em dashes and banned phrases: none found.
- All links in `README.md` and `modules/README.md` resolve.
- `scripts/check-mirror-drift.sh` and `scripts/verify-project.sh`: clean.

### Risks / Open Items

- `npm install` reported 4 dependency vulnerabilities (3 low, 1 high), inherited from the blog-factory-lab starter, not yet triaged — logged in `docs/next-actions.md`.
- No live Pages deploy has happened yet; the workflow is untested against the real GitHub Actions environment (only validated locally). First run should be watched closely.

### Next Actions

- Human-confirm the first Pages deploy (enable Pages in repo Settings, run the `workflow_dispatch` workflow), then uncomment the `push` trigger.
- Content-building run with Coachgremlin, one concept at a time.
- Triage the `site/` dependency vulnerabilities before the first real deploy.
