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

## 2026-07-03 - Hands-on-by-design made a hard requirement; agent-native interaction backlogged

Before the first Pages deploy, coderturtle set a core principle: every workshop this factory produces must be hands-on, requiring the learner to produce or demonstrate something concrete to advance, never passive reading. Also raised a genuinely novel backlog idea: workshop content structured for direct agent/harness interaction, not just human-in-a-harness reading.

### What changed

- All 5 module READMEs and `modules/README.md`'s arc table gained an explicit "Required to advance" element, even at skeleton stage (e.g. module 01: "a working prompt that gets a hard task right first try," not "read this section").
- `docs/workshop-design.md`'s teaching-method section states the hands-on requirement as a hard requirement, not aspiration, and gained a new "Backlogged" section for the agent-native interaction idea.
- `~/hekton/gremlins/workshop/workshop-gremlin.md`: new "Design Principles for Every Workshop" section (hands-on by design is now factory-wide, not this-workshop-specific); the module-README template gained a required 7th part (the gate); a new "Future Direction: Agent-Native Workshop Interaction" section captures the backlog idea without committing to build it.
- `~/hekton/gremlins/coaching/coachgremlin.md`: cross-referenced both, since Coachgremlin's existing "no passive reading" stance was the model for the new factory-wide principle, and its Workflow is the most likely place agent-native interaction would eventually plug in if that's ever built.
- `~/hekton/gremlins/workshop/workshop-review-panel.md`: the Instructional Designer persona now explicitly checks whether every module states a real gate, not just plausible-sounding objectives.
- Caught and fixed a real, pre-existing em-dash violation across `modules/` and `README.md` (written before `docs/brand.md`'s hard rules existed) during this same consistency pass — not a review-panel finding this time, a self-check.

### Decisions Made

See `docs/decisions.md`, three 2026-07-03 entries: "Hands-on-by-design made a hard, non-negotiable requirement," "Backlogged (not scoped): agent-native workshop interaction," and "Fixed a pre-existing em-dash violation."

### Risks / Open Items

- The required gates are still placeholders (e.g. "rubric TBD by Coachgremlin") — the real test is whether the content-building pass actually produces exercises that satisfy them, not just states them.
- Agent-native interaction is explicitly unscoped. Whoever picks it up should resolve whether it dilutes or strengthens the "harness is the classroom" thesis before building anything.

### Next Actions

- Content-building pass should treat each module's stated gate as a hard constraint on the exercise it designs, not just inspiration.
- Re-run the Workshop Review Panel once content exists, checking that gates are actually satisfied, not just present.
- Still pending: human-confirmed first Pages deploy.

## 2026-07-03 - Local verification + deep research pass on agent-native interaction

Before the live Pages deploy, ran the site locally to actually verify it (not just trust the build), and commissioned a deep Opus research pass on the agent-native workshop interaction idea backlogged earlier.

### What changed

- **Local run:** started the Astro dev server, drove it with headless Chromium (Playwright), and reviewed real screenshots of the homepage and the build-log entry page. Both render correctly under the `/terminal-velocity/` base path; no console errors. Dev server stopped afterward.
- **`docs/agent-native-interaction-plan.md`** (new): a deep research pass reading `workshop-gremlin.md`'s Future Direction section, `coachgremlin.md`, the module skeleton, and the review panel definition. Key finding: Coachgremlin is an agent, not a running service, so the correct default is a static machine-readable manifest, not a live server (an MCP server is a real option but should be phase 3, gated on the static pilot proving out first, and doubles as module-03 teaching content rather than being the entry point). Compares 5 technical options (manifest, MCP server, CLI contract, GitHub Action, file-drop convention), answers the three open questions left in the original backlog note, and recommends piloting module 03 (harness engineering) first, explicitly excluding module 01 (prompt engineering) as a poor fit since prompt-authoring is the human's job. Specifies a concrete Human Gate extension for agent-submitted attempts: an `attempt_driver` field plus an attestation-of-understanding requirement (not just artifact existence).
- `docs/workshop-design.md`'s "Backlogged" section links the new plan; `docs/next-actions.md` and `docs/decisions.md` updated.

### Decisions Made

See `docs/decisions.md`, 2026-07-03 "Verified the site locally before any deploy" and "Commissioned a deep Opus research pass on agent-native workshop interaction" entries.

### Risks / Open Items

The plan is still just a plan. The real test is whether the content-building pass and any future pilot implementation actually honor the non-delegation clauses it specifies, not just cite them.

### Next Actions

- Still pending: human-confirmed first Pages deploy.
- If the agent-native pilot is picked up: schema first, then the grader persona, then module 03's manifest, ideally alongside real module-03 Coachgremlin content.

## 2026-07-03 - Workshop Lifecycle documented (Build/Learn); takeaways designed per module

coderturtle asked whether Workshop Gremlin and Coachgremlin should merge into one "hybrid agent-human workshop" workflow, and separately asked what a learner (or their agent) should walk away from a workshop with.

### What changed

- **Did not merge the Gremlins.** `~/hekton/gremlins/workshop/workshop-lifecycle.md` (new, in `~/hekton`) documents them as two phases of one lifecycle instead: Build (Workshop Gremlin, runs a handful of times, pre-learner) then Learn (Coachgremlin, runs continuously, per concept per learner). Both Gremlin definitions gained a `Lifecycle Phase` header; `agents/index.md` gained a Phase column. Full reasoning for staying separate: cardinality, reuse grain, audience, each independently sufficient.
- **Takeaways added as a standing principle**, not just this workshop's idea: `workshop-gremlin.md` gained Design Principle 4 (every gate produces a keepable takeaway) and the module-README template grew from 7 to 8 parts. `coachgremlin.md`'s Workflow gained a "package the takeaway" step (6th), plus matching Outputs and Completion Checklist updates.
- **Concrete takeaways designed for all 5 modules** and written into `modules/*/README.md` plus a new `modules/README.md` "What you keep" table: a reusable prompt template (01), a context-budgeting Skill (02), a real sub-agent/harness-config definition (03, strongest fit, also the agent-native-interaction pilot candidate), a reusable loop template (04), and a diagnostic-playbook Skill (05, compressing all four layers into one method).
- `docs/workshop-design.md` and `docs/workshop-gremlin-design.md` updated to reflect both decisions; `docs/workshop-gremlin-design.md`'s status section corrected (Workshop Gremlin and the Review Panel are v0; Coachgremlin is still draft, no real run yet).

### Decisions Made

See `docs/decisions.md`, 2026-07-03 "Workshop Gremlin and Coachgremlin stay separate" and "Every module's gate now produces a takeaway" entries.

### Risks / Open Items

The takeaways are designed, not proven. Coachgremlin has never run for real; whether "package the takeaway" actually produces something a learner would keep, versus busywork tacked onto the exercise, is untested until a real content-building pass happens.

### Next Actions

- Content-building pass for any module should treat producing the stated takeaway as part of the exercise's success criteria, not an afterthought.
- Coachgremlin's first real run is the next piece of evidence this factory needs, for the takeaway-packaging step specifically as well as the exercise/rubric loop generally.

## 2026-07-03 - Clean-break audit, dogfooded loop engineering, Coachgremlin implementation plan

Three things, in order: audited both repos for a clean session handoff; built the loop-engineering dogfood opportunity identified earlier; produced a detailed content-building plan so Coachgremlin's first real run can happen in a fresh session.

### What changed

- **Clean-break audit.** `terminal-velocity` (PR #1) was already clean, everything pushed. `~/hekton` was not: 11 commits of real Gremlin/Lifecycle work were sitting on a local-only branch while every other branch in that repo routinely goes through PR review. Pushed it and opened `~/hekton` PR #26.
- **Docs Consistency Loop, built and wired.** New `scripts/check-brand-lint.sh` (em dashes, banned phrases, scoped to published content only per `docs/brand.md`), alongside the existing `scripts/check-mirror-drift.sh`. Both wired warn-only into the pre-push hook (`scripts/setup-hooks.sh`), regenerated locally so it's live now. Documented as a named verification loop in `~/hekton/gremlins/workshop/workshop-lifecycle.md`'s new "Dogfooding" section, mapped explicitly onto this project's own loop taxonomy. Deliberately did not automate the more interesting hill-climbing candidate (Gremlin-contract revision after each run), citing this factory's own stable-goal-vs-moving-target rule: each Gremlin has had only 1-2 real runs, short of the 3+ the Gremlin Model requires before a contract counts as stable.
- **`docs/coachgremlin-implementation-plan.md`** (new, Opus-run): real exercise specs, rubrics, stop conditions, and takeaway-packaging instructions for all 5 modules, built against one shared cumulative fixture (a small deliberately-flawed `receipts` CLI). Resolves every constraint the Workshop Review Panel deferred to content-building: modules made genuinely cumulative (02 reuses 01's task under noise; 03's harness runs 01-02; 04's loop runs inside 03's harness; 05 sabotages assemblies of 01-04), harness-agnostic-vs-Claude-Code-leaning decided explicitly per module with translation tables, module 04 right-sized (one required core plus three optional graded extensions instead of four heavy exercises), and the capstone built genuinely ambiguous (multi-variant sabotage, obvious culprit is not the real one). Recommends **module 04's Ticket-to-PR-Ready core** as Coachgremlin's actual first real run, not module 01 despite being cheaper, because 04 exercises Coachgremlin's two least-proven Workflow steps (observe the attempt; package the takeaway, added only today) and forces the shared fixture to get built first. Includes a concrete go/no-go dry-run design: run a deliberately weak/rubric-gaming attempt through it and confirm Coachgremlin actually catches it, the direct test of the review panel's "grader trust asserted, not shown" finding.

### Decisions Made

See `docs/decisions.md`, three 2026-07-03 entries: "Named and wired the Docs Consistency Loop," "~/hekton's branch pushed and PR #26 opened," and "Detailed Coachgremlin content-building plan produced."

### Risks / Open Items

The content-building plan is thorough but unexecuted. The real test is the module-04 dry run itself: whether Coachgremlin's rubric actually discriminates a good attempt from a gaming one, and whether "package the takeaway" produces something a learner would keep. Both are open until that dry run happens.

### Next Actions

- Fresh session: build the shared `receipts` fixture, then run Module 04's core exercise as Coachgremlin's first real dry run, per `docs/coachgremlin-implementation-plan.md` §5-§6.
- `~/hekton` PR #26 needs human review.
- Still pending: human-confirmed first Pages deploy.

## 2026-07-03 - Executed the Coachgremlin plan's step 0 and step 1: fixture built, Module 04 dry run run for real

Picked up `docs/coachgremlin-implementation-plan.md` §6 exactly where the prior session's next-actions left it: build the shared fixture, then run Module 04's core exercise as Coachgremlin's actual first dry run, gating the rest of the content-authoring pass on the outcome. Coachgremlin has no live service, so this session played each role the dry run needs directly: fixture author, good-faith learner, rubric-gaming learner, then grader.

### What changed

- **`fixtures/receipts/`** (new): the shared cumulative fixture. A small stdlib-only Python CLI (`receipts/grouping.py`, `cli.py`) implementing `group_expenses_by_month(rows, tz)` per `SPEC.md`'s four required edge cases, with one seeded bug (month key computed from the raw UTC timestamp, never converted to `tz`) isolated to exactly one failing test (`tests/test_grouping.py`). Verified isolation by actually running the suite against the buggy code before writing anything else. Caught and fixed a real bug in my own test data along the way: a malformed-row test's "good" timestamp happened to cross a DST boundary in `America/New_York`, an unintended second failure the fix would have needed to also satisfy; corrected the timestamp so only the intended edge case is exercised.
- **`modules/04-loop-engineering/README.md`**: replaced the `_(rubric + terminal state defined per exercise by Coachgremlin)_` placeholder with the real Ticket-to-PR-Ready core exercise, a 5-criterion rubric, and a two-terminal-state stop condition, all against the fixture's seeded bug. Extensions A/B/C intentionally left unauthored (they wait on Module 03's harness per the plan's sequencing).
- **`runs/2026-07-03-module-04-dry-run/`** (new): Coachgremlin's first real dry run, executed for real, not simulated.
  - `attempt-good/`: a real bounded loop (`loop.sh`) that reproduces the failure, root-causes it correctly, applies a genuine two-line fix (`zoneinfo` conversion) to exactly the right file, reruns the full suite, and hits `TERMINAL STATE: SUCCESS` on attempt 1. Building this loop script surfaced a real bug in the harness itself: `set -o pipefail` made the reproduce-step check see `unittest`'s nonzero exit (tests failing) instead of `grep`'s match result, so it silently reported "could not reproduce" on a genuinely reproduced failure. A loop-engineering exercise shipping a broken verification step on the first draft is either an embarrassment or free bonus material; treating it as the latter. Fixed by writing to a log file and grepping that, instead of piping through the check.
  - `attempt-gaming/`: a deliberately weak attempt that "fixes" the bug by rewriting the failing test's own assertion to match the buggy output, never touching the implementation. Also a real transcript, not narrated.
  - `grading.md`: graded both against the module's rubric. Real finding: two of the five criteria, read literally, would have passed the gaming attempt (it does state terminal states up front, and a terminal state does fire). Only inspecting *which file* the diff touched (test file vs. implementation) catches it, and that requirement was implicit in the rubric text, not stated. Closed the gap in the rubric itself (`modules/04-loop-engineering/README.md`'s criterion 4 now names the test file as an explicit hard boundary) rather than leaving it as a written-down risk.
  - `takeaway-validation/`: the packaged takeaway (`.claude/commands/ticket-to-pr-ready.md`, new) applied by hand, step by step, to a second, unrelated bug (an off-by-one slice in a word-frequency function, nothing to do with timezones), to satisfy the plan's bar that a takeaway is reusable, not just written. It worked: found the bug, fixed it in one line, left the test file alone, terminal state fired.
  - `retro.md`: go/no-go against the plan §5 checklist, checked point by point with evidence. **Go**, with the rubric-gaming finding above as the one real gap this dry run was built to surface.
  - `run-20260703-AEW-001.yaml`: the run recorded per `runs/.schema.yaml`, `human_confirmed: false` (Human Gate: recommendation, not self-certified).
- **`~/hekton/gremlins/coaching/coachgremlin.md`**: fed the grading-discipline finding back into Coachgremlin's own contract (its Workflow step 3 and Completion Checklist now require checking which files a diff touches before trusting a green terminal state on a verification-loop exercise), not just noted as a one-off finding in this project. See `~/hekton/docs/session-log.md`'s matching entry.

### Decisions Made

See `docs/decisions.md`, four 2026-07-03 entries: "Built the shared `receipts` fixture," "Authored Module 04's core exercise content," and "Ran Coachgremlin's first real dry run (Module 04 core); go."

### Validation

- `fixtures/receipts`: full suite run against the shipped (buggy) code, confirmed exactly one failure (`test_month_boundary_crosses_in_target_timezone`); CLI smoke-tested against `data/sample_receipts.csv`.
- `attempt-good/loop.sh` and `attempt-gaming/loop.sh`: both run for real, transcripts are genuine command output (`transcript.txt` in each), diffs (`diff.patch`) confirm what each attempt actually touched.
- `takeaway-validation/`: the packaged template's steps applied to an unrelated bug for real, transcript captured.
- `scripts/check-brand-lint.sh`: clean after both `modules/04-loop-engineering/README.md` edits (fixture code itself is out of the published-content scope, by design, per `fixtures/receipts/README.md`).

### Risks / Open Items

- This dry run used one grader (this session) grading its own two constructed attempts. `retro.md` flags that a stronger future test would have an independent pass grade the same transcripts blind.
- `~/hekton`'s working tree has unrelated uncommitted work (`config/projects.yaml`, `justfile`, new `scripts/`) from prior sessions; left untouched, not this session's to resolve, flagged in that repo's own session log.
- Extensions A/B/C for Module 04 and the bloated/sabotaged fixture variants (Modules 02/05) remain intentionally unbuilt; sequencing is in `docs/coachgremlin-implementation-plan.md` §6.

### Next Actions

- coderturtle review of this dry run (`runs/2026-07-03-module-04-dry-run/retro.md`) and the `coachgremlin.md` edit, per the Human Gate.
- Per plan §6 step 2: author Module 01 next (cheap, atomic, reuses the fixture's function spec), applying any further retro lessons.
- `~/hekton` PR #26 still needs human review; first Pages deploy still pending human confirmation.

## 2026-07-03 - Committed the dry run, then closed a review-panel gap with a filtered real-transcript preview

Committed the fixture/Module-04/dry-run work above (`e22fb88`, local, not pushed). Then picked up a side question raised while reviewing that work: this session's takeaway artifacts (`.claude/commands/ticket-to-pr-ready.md`, the `receipts` fixture) are things a learner's own agent consumes, but is there anything a human needs that isn't that? The Workshop Review Panel's End-User/Learner persona had already flagged the relevant gap, back when no real content existed: no sample module, no walkthrough, "come back later."

### What changed

- **`scripts/render-transcript-preview.py`** (new): a filter, not a content generator. Reads `runs/2026-07-03-module-04-dry-run/attempt-good/transcript.txt` and writes `docs/sample-attempt-preview.md`, condensing five verbose `unittest` lines into a pass/fail count, extracting the one failure's assertion message instead of its full traceback, and splitting narrative prose from `grep -n`-style code fragments so they don't run together. Every fact in the output is pulled from the real transcript; nothing is invented. Rerunning the script regenerates the page from source, so it can't silently drift the way a hand-maintained "sample module" would.
- **`docs/sample-attempt-preview.md`** (new, generated): the condensed preview. Added to `scripts/check-brand-lint.sh`'s scope since it's linked from the README and read by prospective learners, not an internal planning doc.
- **`README.md`**: new "See it in action" section, before "How to start," linking the preview so a visitor can see what a real attempt looks like before cloning anything or setting up an agent.
- **`docs/decisions.md`**: recorded the approach and why it doesn't contradict the workshop's own anti-tutorial thesis (real, mechanically-extracted evidence, not manufactured "hello world" content).

### Why this shape and not a DIY mini-project

Considered and rejected building separate human-facing code samples or interactive mini-projects as a second content track. The workshop's whole thesis is "you learn this by doing it inside a harness, not by reading about it" (`docs/workshop-design.md`); a parallel tutorial track would fight that thesis and need to be kept in sync forever. A filtered excerpt of real, already-existing evidence closes the review panel's actual gap (a prospective learner has nothing to look at before committing) without inventing a second thing to maintain.

### A bug, on brand

The filter script shipped a real bug on the first run: its banner-detection regex (`^===.*===$`, meant to catch this script's own `=== ... ===` framing lines) also matched `unittest`'s bare `======...======` divider, which silently truncated the "reproduce" step and dropped the one failure's detail line from the output. Caught by actually reading the generated file rather than trusting the script ran without errors, which is the exact discipline this whole session has been about. Fixed (`^=== .+ ===$`, requiring the space unittest's divider doesn't have) and left as a code comment, not scrubbed from history.

### Validation

- Ran the script, read the generated `docs/sample-attempt-preview.md` in full, caught the truncation bug by inspection, fixed it, reran, confirmed the failure detail and all four steps render correctly with no double-blank-line artifacts.
- `scripts/check-brand-lint.sh`: clean (15 files now in scope, up from 14).
- `scripts/verify-project.sh` and `scripts/check-mirror-drift.sh`: clean.
- Grepped the new file and the README edit for em dashes: none.

### Next Actions

- Same as above: coderturtle review of the dry run, then Module 01 next.
- If the fixture or the dry-run transcript ever changes, rerun `scripts/render-transcript-preview.py` before assuming the published preview still matches.

## 2026-07-03 - Authored and verified Modules 01, 02, 03, 05; all five core exercises real

Continued straight through `docs/coachgremlin-implementation-plan.md` §6 past the Module 04 dry run's "go": authored the remaining four modules' core exercises, one at a time, each built against a real fixture variant and actually run at least once before being called done, not just written and hoped for. Chose depth over exhaustive rigor per module (one real verification pass each, not a full adversarial dry run like Module 04 got), except where the rubric's own criterion required more (Module 01's reproducibility needed three independent runs; Module 05's "rule out the other three" needed a full written defense for at least one variant). Module 03's agent-native manifest co-production was deliberately deferred, content only this pass.

### What changed

- **Module 01 (prompt engineering).** New fixture variant, `fixtures/receipts/variants/unimplemented/`: `group_expenses_by_month` stubbed to `raise NotImplementedError` instead of shipping the seeded bug, so the exercise is genuinely "write the implementation from spec," not "fix an existing one" (that's Module 04's job, and the two would have collapsed into each other if they shared a starting point). Designed a candidate prompt naming the exact signature and all four edge cases, with an explicit "do not touch the test file" scope constraint. Validated for real: three independent, isolated subagents, each given only the prompt and no visibility into anything else, all three produced a correct implementation on the first try, none touched the test file (`runs/2026-07-03-module-01-dry-run/`). `modules/01-prompt-engineering/README.md` authored; takeaway packaged as `.claude/commands/spec-impl.md`, a generalized template with each constraint's rationale attached.
- **Module 02 (context engineering).** `fixtures/receipts/variants/bloated/`: the unimplemented variant buried under 9,289 lines of generated noise (padded README, versioned CHANGELOG, an unrelated `legacy_export.py`, stale docs, a red-herring per-state tax-rate config), via new `scripts/generate-bloated-variant.py` so the noise is reproducible, not hand-typed. New `scripts/context-budget.sh`, a harness-neutral line/char counter. Curated the bloated variant down to 182 lines (well under the 2,000-line budget) by hand, cutting `receipts/cli.py` as a legitimate exclusion (not imported by the test suite) alongside all the noise; reran Module 01's exact prompt against the curated set in a fresh, isolated subagent, confirmed it still passed (`runs/2026-07-03-module-02-dry-run/`). `modules/02-context-engineering/README.md` authored; takeaway packaged as `.claude/skills/context-budgeting/SKILL.md`.
- **Module 03 (harness engineering).** Extended the canonical fixture with a second, independent target: `group_expenses_by_category`, stubbed, plus a pre-written failing `tests/test_by_category.py` covering both the function and a not-yet-existing `--by-category` CLI flag. Defined a bounded sub-agent, `.claude/agents/receipts-category-summary.md` (scope: `receipts/` only, verify only the new test file since the rest of the suite has Module 04's unrelated known failure). Ran a genuine two-phase reset-and-resume: a fresh subagent implemented the function, deliberately stopped before touching `cli.py`, and wrote real progress notes; a second, completely fresh subagent with zero memory of the first read only those notes and finished the CLI wiring correctly. Independently reverified at every step (diffed untouched files, reran tests directly, checked default CLI behavior stayed unbroken) rather than trusting either subagent's self-report (`runs/2026-07-03-module-03-dry-run/`). `modules/03-harness-engineering/README.md` authored, including a Claude Code to Cursor to Codex translation table; takeaway is the sub-agent definition itself. Agent-native manifest (`docs/agent-native-interaction-plan.md`'s schema/grader persona/`module.yaml`/`AGENT.md`) explicitly not built this pass.
- **Module 05 (synthesis capstone).** Two sabotaged variants, `fixtures/receipts/variants/sabotaged-harness/` and `fixtures/receipts/variants/sabotaged-loop/` (of the plan's stated two-to-four; a prompt- and context-bottleneck variant remain a defined, unbuilt extension), sharing an identical prompt and background doc as constant red herrings so neither is ever the real answer. One variant's harness config wrongly scopes edits to `docs/` instead of `receipts/`; the other's loop checks for a success string `unittest` never prints, so it reports failure regardless of the real result. Diagnosed both for real: a scope-obedient subagent genuinely couldn't fix the harness variant, and an isolating test (fixing only the harness config in a throwaway, touching nothing else) flipped it to a genuine `TERMINAL STATE: SUCCESS`; the loop variant was diagnosed with a full written defense ruling out the other three layers with evidence, not assertion, after confirming a known-correct fix still didn't clear the sabotaged loop's broken check (`runs/2026-07-03-module-05-dry-run/`, `sabotaged-loop-defense.md`). `modules/05-synthesis-capstone/README.md` authored; takeaway packaged as `.claude/skills/diagnose-agent-failure/SKILL.md`, generalizing both diagnoses into one method with a symptom-to-suspect-to-confirm-to-fix quick-reference table.
- **`modules/README.md`** and **`fixtures/receipts/SPEC.md`**: content-status banners updated from "skeleton only" / "not yet built" to reflect that all five core exercises are real and verified, with pointers to each module's evidence directory.
- **`scripts/check-brand-lint.sh`**: scope extended to `.claude/commands/`, `.claude/skills/`, and `docs/sample-attempt-preview.md` across this and the prior session, since takeaway artifacts are learner-facing, not internal scaffolding.

### Decisions Made

See `docs/decisions.md`, four 2026-07-03 entries, one per module.

### Validation

- Every module's fixture variant was run against its pristine (broken/stubbed) state and confirmed to fail exactly as designed before any content was written around it.
- Every module's exercise was actually attempted, not just described: Module 01 three times independently; Modules 02, 03, 05 at least once each, with Module 03 spanning two genuinely separate sessions and Module 05 covering both shipped variants.
- Every attempt's self-reported result was independently reverified from this session (diffed untouched files, reran test suites directly), not trusted at face value.
- `scripts/check-brand-lint.sh`, `scripts/verify-project.sh`: clean after all four modules.
- All shipped fixture variants confirmed still in their pristine, unfixed/unsolved state after verification work (throwaway copies absorbed every actual fix attempt), so a real learner still gets a genuine exercise.

### Risks / Open Items

- Every rubric above was validated by the same session that authored it, same caveat as RISK-0004 from the Module 04 dry run, now true across all five modules, not just one. An independent read of any of these exercises hasn't happened yet.
- Deliberately deferred, not forgotten: Module 04's three extensions, Module 05's prompt- and context-bottleneck variants, and Module 03's agent-native manifest co-production.
- The bloated variant's exact line count (9,289) is comfortably over budget but short of the plan's "roughly 12k" figure; judged sufficient since the point is forcing real curation, not hitting an exact number.

### Next Actions

- coderturtle review of all five modules' content and evidence, per the Human Gate; this is the point to decide whether Coachgremlin's dry-run treatment should be repeated more fully on any one of them before the Workshop Review Panel re-run.
- Re-run the Workshop Review Panel on real content (`docs/coachgremlin-implementation-plan.md` §6 step 7), now that all five modules have it.
- Build the deferred extensions/variants/manifest above, in whatever order the review surfaces as highest-value.
- Still pending: human-confirmed first Pages deploy; `~/hekton` PR #26 review.

## 2026-07-03 - Site gets a guide page; build log catches up four entries

coderturtle asked to inspect the site locally, then asked for two structural things on it: a guide page (points to the repo, a runbook, what both a human and their agent get out of the workshop, the harness-as-classroom idea) alongside the existing build log, and more build-log entries since the journal had only ever gotten one, despite the project having moved a long way past that first day's scaffolding.

### What changed

- **`site/src/pages/index.astro`** rewritten from a build-log-listing homepage into the guide: what the workshop is, the harness-is-the-classroom bet stated plainly as a bet, a "what you walk away with" section split explicitly between the human's judgment and the agent's packaged takeaways (reusing `modules/README.md`'s "what you keep" framing), a numbered runbook (prerequisites, clone command, start at `modules/README.md`, module order, the hands-on-by-design rule), a link to `docs/sample-attempt-preview.md` on GitHub as a look-before-you-clone preview, and the three most recent build-log entries with a link to the full index.
- **`site/src/components/layout/BaseLayout.astro`**: header gained a two-item nav (Guide, Build log) now that there are two sections; footer copy generalized since it no longer only describes a build log.
- **`docs/build-log/`**: four new dated entries catching the journal up to the project's actual state, each a real narrative with real tension per `docs/brand.md`'s voice rules, not a highlight reel: the hands-on-by-design rule and the em-dash self-check that immediately followed it; the Workshop-Gremlin-vs-Coachgremlin lifecycle decision and the takeaways idea; Coachgremlin's first real dry run (the rubric almost let a cheating attempt pass, and the loop harness that ran the good attempt had a real `pipefail` bug of its own); and the four-module authoring pass, including the moment the capstone's own sabotaged-loop variant turned out to need the identical fix as the bug that broke the earlier dry run's harness. `pubDate` values use distinct same-day timestamps so ordering resolves correctly.

### Decisions Made

See `docs/decisions.md`, 2026-07-03 "Site restructured: guide page plus build log; four build-log entries added" entry.

### Validation

- `npx astro check`: 0 errors, 0 warnings, 0 hints.
- `npm run build`: all 8 pages built clean, including all 5 build-log entries and the new guide homepage.
- Dev server run live, not just built: curled the homepage (200, correct title, nav present), the build-log index (200, all 5 entries present in correct newest-first order), and a spot-checked new entry route (200).
- `scripts/check-brand-lint.sh`: clean across all new site and build-log content (23 files in scope, up from 19).

### Risks / Open Items

- No live screenshot review this session (Playwright wasn't set up as a project dependency and wasn't worth installing just for this); relied on `astro check`, a full build, and direct HTTP verification of rendered content instead. coderturtle is inspecting the running dev server directly, which covers the gap.
- The guide's GitHub links (repo clone URL, the sample-preview blob link) will 404 until the local commits are pushed.

### Next Actions

- coderturtle: visually confirm the guide page and new build-log entries in the browser.
- Push the local commits so the guide page's GitHub links resolve.
- Consider whether the guide page should also get a screenshot-based visual review before the first live Pages deploy, per this project's established practice of not trusting a build's exit code alone.

## 2026-07-03 - Ran the Workshop Review Panel against real content for the first time (Module 01), fixed what it found

coderturtle read Module 01 and called it "probably good but not very digestible," and asked to run the Workshop Review Panel against it if it hadn't already run against real content. It hadn't: the one prior run (`docs/review-panel/2026-07-03-initial-design.md`) only had design docs to work with, before any exercise existed, and "re-run once real module content exists" was still an open follow-up action in the panel's own definition. So this was the panel's actual second run, and its first against something a learner would really attempt.

### What changed

- **Ran all seven personas** (`~/hekton/gremlins/workshop/workshop-review-panel.md`) independently and in parallel against `modules/01-prompt-engineering/README.md` and its supporting artifacts (`SPEC.md`, `.claude/commands/spec-impl.md`, the dry-run evidence). Raw critiques preserved in `docs/review-panel/2026-07-03-module-01-personas/`; synthesis at `docs/review-panel/2026-07-03-module-01-content.md`.
- **Two cross-persona agreements**, independently reached: (1) Developer Evangelist and Technical Writer both diagnosed the actual cause of "not very digestible" as structural, not tonal — the exercise buried under five headers of framing, with an internal review-panel citation and workshop-internal jargon leaking into learner-facing prose; (2) AI/ML Practitioner and Instructional Designer both flagged that the module's central claim ("a naive prompt drops the edge cases") had only ever been tested with the polished prompt, never a naive one, so the module's core discriminator was asserted, not demonstrated.
- **Closed the evidence gap for real, not just with a word change**: ran the missing counterfactual, a deliberately naive prompt (no named edge cases, no scope constraint) through three fresh, independent sessions against the same fixture, independently reverified the same way the original dry run was. **It also passed 3-for-3.** Root cause, confirmed by inspection: the fixture's own docstring already lists all four edge cases, so a reasonably diligent agent finds them regardless of what the prompt says. The module's central claim was rewritten to say what was actually shown (reproducibility and explicit scope control are the demonstrated advantages; edge-case-dropping wasn't) rather than keep the unsupported original. New "Counterfactual" section in `runs/2026-07-03-module-01-dry-run/README.md` has the full method and result.
- **Found and fixed a real functional bug**: `SPEC.md`'s "Running it" section hardcoded `cd fixtures/receipts` in every variant copy, including `variants/unimplemented/`, where Module 01 actually runs. A learner following the module's own pointer into SPEC.md and then following its literal instructions would land in the wrong fixture entirely. Fixed in all four copies (base plus three variants) to be directory-relative instead of hardcoded, and to note that the CLI demo command needs sample data most variants don't ship.
- **Restructured `modules/01-prompt-engineering/README.md`**: exercise now appears second, right after the framing question, instead of five headers deep; the internal citation to the prior review-panel report removed from learner-facing prose; "Required to advance" and "Stop condition" merged (they restated each other almost verbatim); Takeaway moved to the very end with an explicit "don't read this before attempting" note, closing a real spoiler issue the End-User/Learner persona caught (reading the page in order handed you the winning structure before you'd tried anything); terminology standardized on "one prompt."
- **Fixed rubric criterion 2's gate-vs-scored contradiction** (tagged "(scored)" while the rest of the page treated it as absolute) and **added a line** addressing the Security-Conscious Reviewer's finding that the module states "green isn't proof" in prose but never asks the learner to actually look at the diff.
- **Softened `.claude/commands/spec-impl.md`'s overclaiming**, per the Skeptical Critic: "tried and failed during validation" (no ablation was ever run), "the single biggest lever" (an unranked claim, and now actually contradicted by the counterfactual), and "catches its own near-misses" (none occurred) all reworded to what the evidence actually supports.
- **Updated the panel's own definition in `~/hekton`**: checked off the "re-run once real content exists" follow-up action, with a summary of this run's outcome. See that repo's own session log for the matching entry.

### Decisions Made

See `docs/decisions.md`, 2026-07-03 "Ran the Workshop Review Panel against Module 01, its first run against real content" entry.

### Validation

- All seven persona critiques independently produced, none generic, none empty; two genuine cross-persona agreements, five single-persona findings, all logged with a status (fixed, or honestly deferred with why).
- The wrong-directory bug was confirmed by direct inspection before being called a bug, not just asserted from a persona's claim.
- The counterfactual's result was independently reverified the same way as the original dry run (diffed the test file for tampering, reran the suite directly), not trusted from the subagents' self-reports.
- `scripts/check-brand-lint.sh`: clean (23 files in scope; caught and fixed one em dash introduced during the Module 01 restructure).
- `scripts/verify-project.sh`: clean.
- Confirmed the shipped `variants/unimplemented/` fixture is still in its pristine, unimplemented state after all the verification work (still `errors=5` against the original stub).

### Risks / Open Items

- One finding (rubric criterion 3, edge-case coverage, is gameable since the exercise text already lists the cases verbatim) was logged as an honest, acknowledged limitation rather than fixed — it's a structural property of the exercise's original design in `docs/coachgremlin-implementation-plan.md`, not something introduced during authoring, and fixing it properly means redesigning the exercise, which is bigger than a content pass.
- The same "internal citation leaks into learner content" pattern the Technical Writer flagged in Module 01 also exists in Module 04's README (noted as a house habit, not a one-off). Not fixed here to keep this pass scoped; a candidate for a small cross-module pass or an explicit `docs/brand.md` rule.
- This is the panel's second real run. Its own follow-up actions call for reviewing whether all seven personas are pulling their weight after 2-3 runs, ideally across different workshops; not due yet, and this run gave no reason to think any persona is dead weight (all seven produced distinct, real findings again).

### Next Actions

- Consider whether Modules 02, 03, 05 should get the same scoped panel treatment, especially since Module 02 directly inherits Module 01's task and might inherit the corrected claim's implications.
- If external research + panel persona/instruction maturation is still wanted independent of this run's outcome, that's a distinct next step, not triggered by this pass (the panel performed well; nothing here argues for redesigning it yet).
- Same standing next actions as before: coderturtle review, push once reviewed.

## 2026-07-03 - Ran the review panel against Modules 02, 03, 04, and 05: two real fixture bugs, one rubric-vs-evidence inconsistency, three closed evidence gaps

Continued straight through the rest of the arc: coderturtle asked to do the remaining modules the same way Module 01 just got done. Same process each time (seven personas, independent and parallel, against that module's real content and evidence), and the same pattern held across all four: at least one structural digestibility defect Module 01's fix hadn't been retroactively applied to, and at least one claim that had been asserted rather than tested, closed with a real new experiment, not a rewrite.

### What changed, by module

- **Module 02 (context engineering).** Real, serious finding: the bloated fixture's noise self-announced itself (files literally labeled "red herring," "historical bloat," "unrelated to the receipts CLI's current scope"), letting the exercise be solved by `grep` instead of the curation judgment it claims to teach. Fixed with real engineering, not a word change: rewrote `scripts/generate-bloated-variant.py` to remove every tell, regenerated the fixture (9,286 lines), reverified the whole pipeline end to end. Also restructured the module, merged overlapping rubric criteria, added a security carve-out to the takeaway Skill (auth/validation code shouldn't be cut just because a specific test doesn't touch it), and made the cumulative hook to Module 01 mechanically real (bring your saved prompt forward) instead of just asserted.
- **Module 03 (harness engineering).** The richest run of the four: three personas independently converged on the same unproven central claim ("the second session can only complete the task by reading the state the first one left behind"). Ran the missing negative control for real: reconstructed the phase-1 checkpoint, withheld the notes file, reran phase 2. **It succeeded anyway**, using code and test investigation alone, contradicting the original claim. Rewrote the module to say what was actually shown. Also added real enforcement to the sub-agent definition (a `tools:` restriction, guidance to verify rather than blindly trust the persistent-state file, a ban on notes containing a finished copy-pasteable answer instead of genuine state), closed an asymmetric-verification gap, and added a "context reset" row plus an enforcement-parity caveat to the harness translation table.
- **Module 04 (loop engineering).** Already had the deepest prior treatment (Coachgremlin's actual first dry run) — this run tested whether that depth prevented drift. It didn't, fully: the panel caught a **real, confirmed factual error**, a rubric criterion asserting a behavior ("a terminal state firing on a test file... does not count") that the module's own grading record explicitly contradicted (the gaming attempt passed that exact criterion "on a literal reading" per `grading.md`). Removed the unsupported clause. Also fixed a legitimate-test-fix exception missing from the "test file is out of bounds" rule, corrected an overclaim about which of the four learning objectives the core exercise actually gates (two of four, honestly; the other two need unauthored extensions), closed a self-report gap in the reusable takeaway (attempt-counting now requires two logged, numbered attempts, not a narrated count), and linked the reference loop script from the README with a clarification that it's a retry-scaffold, not a claim the fix step itself should be scripted rather than agent-driven.
- **Module 05 (synthesis capstone).** Two more real fixture bugs, both caught independently by two personas each: `sabotaged-harness`'s scope referenced a `docs/` directory that didn't exist in the shipped fixture (diagnosable by directory listing alone, no isolating test needed); and the shared `background.md`/`prompt.md` files ended with self-spoiling meta-commentary ("None of the above is required to diagnose the current bug"), the identical self-announcing-noise failure Module 02's own run had just found in a different module. Fixed both: added a real, plausible `docs/contributing.md`; stripped the confessions. Also closed a real evidence gap: the loop variant's "ruled out the prompt" claim had been inferred from a hand-applied fix, never tested against an agent working from the actual prompt. Ran a fresh agent against it for real; it succeeded and reported the informal prompt caused no real difficulty. Corrected an overclaim that the capstone "composes all four layers" when only two (harness, loop) are currently live hypotheses, the other two are permanent, identical controls until the deferred prompt/context variants are built. Added two new steps to the takeaway Skill per the Security-Conscious Reviewer: check a fix didn't trade one failure for a new one, and report honestly when evidence is genuinely ambiguous instead of forcing a confident verdict.
- **`modules/README.md`**: content-status banner updated to reflect the full panel pass across all five modules, not just authoring.
- **`~/hekton/gremlins/workshop/workshop-review-panel.md`**: new "Runs 2-6" section summarizing the outcome across all five module runs (6-for-6 on producing genuinely distinct findings; flags that all six runs share one workshop, so the "different workshops" half of the panel's own maturation trigger still isn't met). See that repo's own session log for the matching entry.

### Decisions Made

See `docs/decisions.md`, four 2026-07-03 entries, one per module.

### Validation

- Every fixture change was independently reverified after the fix: the bloated variant regenerated and reconfirmed over budget with the curated set still passing; the harness reset-and-resume negative control independently reverified (diffed untouched files, reran tests directly); the sabotaged-loop agent attempt independently reverified the same way.
- `scripts/check-brand-lint.sh`: clean after all four modules (23 files in scope throughout).
- All shipped fixture variants confirmed still in their pristine, unsolved state after every verification pass, so real learners still get a genuine exercise.
- Canonical `fixtures/receipts/` reconfirmed unaffected by any of this pass's fixture edits (Module 04's seeded bug and Module 03's category stub both still present and isolated).

### Risks / Open Items

- Two of five modules' fixture bugs (Module 02's self-announcing noise, Module 05's missing `docs/` directory and self-spoiling context files) were real, shipped defects that existed for hours before an independent review caught them. Neither would have been caught by the same session re-reading its own work; both were caught by a genuinely independent pass. Worth remembering next time new fixture content ships without a review pass behind it.
- Every rubric/diagnosis across all five modules has still only ever been validated by the same session that authored and reviewed it (`docs/risks.md` RISK-0004). Six panel runs in one workshop is real repetition evidence; it is not the "different workshops" breadth the panel's own maturation trigger asks for.
- Module 04's confirmed rubric-vs-grading-evidence inconsistency was introduced during this same day's earlier humor/tightening pass and went unnoticed until this run. A useful, concrete argument for running the panel (or some independent check) closer in time to any rubric edit, not just once at authoring time.

### Next Actions

- coderturtle review of all five modules' panel reports and fixes, per the Human Gate.
- Consider running the panel against a genuinely different workshop once one exists, to test the breadth half of the panel's own maturation trigger.
- Still open: Module 04's extensions, Module 05's prompt/context variants, Module 03's agent-native manifest, all deliberately deferred.
- Push the local commits once reviewed.

## 2026-07-03 - Ran the panel against the user-facing entry-point docs (README, arc index, site guide, sample preview)

coderturtle asked to run the panel through "the rest of the user docs in the repo including the readme." Scoped this to the actual learner-facing entry points, deliberately excluding internal/maintainer docs (`docs/workshop-design.md`, `docs/brand.md`, `docs/decisions.md`, etc.) and the build-log journal, which serve a different purpose: `README.md`, `modules/README.md` (never directly reviewed before, only referenced), `site/src/pages/index.astro`, `docs/sample-attempt-preview.md`. This is the panel's 7th real-content run.

### What changed

- **Cross-document consistency was this run's real value.** Two agreements, both invisible from reading any single file: README.md and the site guide page duplicated almost entirely with no cross-linking, and actively *disagreed* on sequencing (README puts the sample preview before the runbook; the site had it after, undermining its own "before you clone anything" heading). And `modules/README.md`'s Content status blockquote reproduced the exact internal-citation-leak pattern already fixed in all five module reviews, at the arc-index level, which had never itself been reviewed.
- **A real, confirmed factual inconsistency**: Module 02's takeaway was called a "Skill" in two documents and a "checklist" in the third; Module 03's takeaway was narrowed from "sub-agent or harness-config definition" to just "sub-agent definition" on the site. Fixed by aligning to `modules/README.md` as the source of truth.
- **A stale claim three documents had inherited**: README, the arc table, and the site all still said the capstone diagnoses "which of the four" layers, contradicting Module 05's own honest scope note (added in the prior panel run) that only two of four layers currently have a built scenario. Fixed consistently across all three.
- **A genuinely broken reference**: `modules/README.md` pointed a learner at `~/hekton/gremlins/workshop/workshop-lifecycle.md`, a path on the maintainer's local machine, unresolvable for anyone who'd actually cloned the repo. Removed.
- **An unhedged outcome claim** on the site ("You get practiced judgment...") directly violated `docs/brand.md`'s own hedging rule, one section after the same page correctly hedged a different claim. Reworded to point at each module's actual evidence instead of asserting the outcome as guaranteed.
- **"Not cherry-picked" overclaimed**: the featured transcript (the successful attempt) was a choice; the text itself wasn't edited. Reworded to the true, available claim, and now explicitly discloses that a gaming attempt exists alongside it.
- Smaller fixes: added the real GitHub Pages URL to a dead-end "Build in public" mention; added a hands-on-by-design statement to the top-level README (previously only in the arc index and site); fixed Module 01's arc-table gate description to name its reproducibility requirement, not just "first try"; added real GitHub issues links where "report it" had no destination; aligned hypothesis/bet wording; named Module 04 explicitly on the site instead of "one of the modules."

### Decisions Made

See `docs/decisions.md`, 2026-07-03 "Ran the panel against the user-facing entry-point docs" entry.

### Validation

- `npx astro check` and `npm run build`: both clean after the site guide page rewrite.
- `scripts/check-brand-lint.sh`: clean.
- Verified file paths directly rather than trusting the personas' claims: confirmed the `~/hekton` path really is unresolvable from the repo, confirmed the Skill/checklist and sub-agent wording really did diverge, confirmed the new README transcript link target actually exists.

### Risks / Open Items

- The site's sample-preview link still targets `main` and will 404 until this branch merges; already a tracked "push once reviewed" item, not new.
- Whether README.md and the site guide page should be substantially differentiated, not just cross-linked and made internally consistent, is a bigger editorial call than this pass made; the fix here makes the overlap honest and navigable, not smaller.
- With this run, every piece of user-facing content in the repository (all five modules plus the four entry-point docs) has now been through an independent review pass.

### Next Actions

- coderturtle review of this run's report and fixes, per the Human Gate.
- Decide whether README.md and the site guide page should be more substantially differentiated in a future pass.
- Same standing items: push once reviewed, human-confirm first Pages deploy.
