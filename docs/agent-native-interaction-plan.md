# Agent-Native Workshop Interaction: Design Options and a Scoped Pilot

> Produced by an Opus-run research pass (2026-07-03), reading `<hekton-machinery>/gremlins/workshop/workshop-gremlin.md`'s "Future Direction: Agent-Native Workshop Interaction", `<hekton-machinery>/gremlins/coaching/coachgremlin.md`, the `modules/` skeleton, `docs/workshop-design.md`'s "Backlogged" section, and `<hekton-machinery>/gremlins/workshop/workshop-review-panel.md`. This is research and a recommendation, not an implementation. Nothing here has been built. Read-only pass; draws on `workshop-gremlin.md`, `coachgremlin.md`, `workshop-review-panel.md`, this project's `docs/workshop-design.md`, all five module READMEs, `docs/implementation-plan.md`, and the existing `runs/` ledger + Astro Content-Layer plumbing already in the repo.

One load-bearing fact discovered during exploration that reframes everything below: **Coachgremlin is an agent (a Tier-3 Gremlin), not a running service.** There is no "Coachgremlin server" to call unless someone builds and hosts one. For a self-paced public workshop with no facilitator, the realistic grader is the *learner's own agent*, primed by a Coachgremlin persona file plus a machine-readable rubric. That single fact is what makes a static manifest the strong default and pushes the live-service options into "optional enhancement" territory rather than "required interface."

A second asset the repo already has: `runs/.schema.yaml` is a machine-readable ledger with `human_confirmed: boolean` and `human_notes` fields, and `site/src/content/config.ts` already ships a machine-readable schema (`glob` loader) alongside human-readable Markdown without duplicating it. Both are direct precedent: the "structured spec beside the prose, one source of truth" pattern is proven in this exact repo, and the Human Gate already has a data field waiting for it.

## 1. The two flavors, and why they compose rather than compete

The backlog names two flavors:

- **Flavor 1: Machine-consumable workshop structure.** Each module's question, gate, rubric-shape, and stop-condition exist as a parseable spec (schema TBD) *alongside* the human-readable README, so an agent acts on declared intent instead of inferring it from prose.
- **Flavor 2: Learner connects via their own agent as primary interface.** The learner points their Claude Code/Codex session at the repo; the agent fetches the current module, runs the exercise, and submits for grading, with the human directing and reviewing rather than hand-driving each step.

They are not alternatives; Flavor 1 is the **data layer** Flavor 2 needs to exist. Flavor 2 without Flavor 1 is what the repo has today (an agent guessing at intent from README prose), which is exactly the "inferring intent from prose" failure the backlog note calls out. Flavor 1 without Flavor 2 is a well-specified manifest nobody's harness consumes, useful documentation, no behavior change. The pilot should deliver a thin slice of *both*: a manifest for one module (Flavor 1) plus a demonstrated end-to-end run where a real harness consumes it and submits (Flavor 2). Delivering only one proves nothing the backlog is asking about.

## 2. Technical options compared

| Option | Build cost | Static / running | Effect on the Human Gate | What the learner's harness does differently |
|---|---|---|---|---|
| **A. Machine-readable manifest** (`module.yaml` per module: question, gate, rubric-shape, stop-condition, expected artifacts, submission target) | **Low.** YAML + a JSON/YAML schema. Squarely inside proven repo capability (`runs/.schema.yaml`, the Astro glob schema). | **Fully static/offline.** No process. | **Unchanged and trivially intact.** The manifest *declares* the gate; nothing certifies. `human_confirmed: false` already exists in the runs ledger. | Parses `module.yaml` instead of scraping README prose; knows the exact artifact to produce and where to drop it. |
| **B. MCP server** (`get_current_module`, `submit_attempt`, `get_feedback`) | **High.** A real server (stdio or HTTP), per-learner progress state, and, critically, an *LLM behind `submit_attempt`* to actually grade, since Coachgremlin is an agent not code. Local stdio keeps it offline-ish; hosted is a real service plus trust boundary shift. | **Requires a running service** (local stdio is the least-bad form). | **Hardest to keep honest.** If `submit_attempt` can return "complete," an agent will treat it as certification. Contract must never emit a terminal certified state, only "rubric provisionally met, awaiting human." | Speaks MCP to a local/remote server. **Thematically perfect**, module 03 *teaches* MCP, so the interface doubles as teaching content, but it's the heaviest lift and the biggest trust shift. |
| **C. CLI contract** (`tv module current`, `tv submit <artifact>`, `tv confirm`) | **Medium.** A local script. Deterministic parts (which module, validate artifact exists, write a run-ledger entry) are code; grading stays a Coachgremlin *invocation* (a persona prompt the learner's agent runs), not something the CLI does itself. | **Fully offline.** Just a script in the repo. | **Clean mapping.** `tv submit` writes a ledger entry with `human_confirmed: false`; `tv confirm` is a separate human-only command. | Shells out to `tv`, which is *literally what module 03 teaches* (tool access, shelling out). The natural middle ground between static manifest and live server. |
| **D. GitHub Action on PR-like submission** | **Medium-high.** CI + an LLM API key in CI to grade. Public repo means key/cost/abuse exposure. Couples to GitHub, not harness-agnostic. | Requires CI (hosted). | **PR review *is* a human gate**, merge is the confirmation, a genuinely nice property. But it centralizes grading cost on the maintainer and ties the workshop to one forge. | Opens a PR with the artifact under `runs/`. Good for a cohort with a maintainer; wrong for self-paced plus public plus "bring your own harness." |
| **E. Local file-drop convention** (agent writes a run-ledger entry under `runs/` per schema; grading happens when a Coachgremlin persona is next run over it) | **Lowest.** It's essentially Option A's manifest plus the existing runs ledger plus a naming convention. | Fully static/offline. | Via the existing `human_confirmed` field. | Follows the drop convention; no new surface to learn. Effectively the base case Options C/B build ergonomics on top of. |

**Reading of the table.** A and E are the same base layer viewed from two ends (A is the spec the agent reads; E is the record the agent writes); together they are a complete, static, offline, harness-agnostic, Human-Gate-preserving pilot with near-zero new infrastructure. C is the first worthwhile ergonomic upgrade and is meta-consistent with module 03. B is the most thematically satisfying and the best *teaching artifact*, but it is a real service with the sharpest trust-boundary risk and should not be first, building a server before the manifest is proven inverts the backlog's own "pilot one module before generalizing" instruction. D is a cohort/facilitated pattern that fights the self-paced/public/BYO-harness framing and puts an API key in a public CI.

**Direct answer to "callable interface vs. manifest enough":** For this workshop's format, **a manifest plus a loadable grader persona is enough**, for the pilot and arguably for the whole self-paced public product, precisely because there is no hosted Coachgremlin to call; the grader is the learner's own agent. A callable interface (C then B) is an ergonomics-and-teaching upgrade, not a correctness requirement. Claiming otherwise would overclaim a live service that doesn't exist (the Skeptical-Critic lens).

## 3. The three open questions, answered

**Q1: Does this dilute or strengthen "the harness is the classroom"?**
**Strengthens it for the structural/behavioral skills (harness, loop, synthesis); genuinely threatens it for the atomic-craft skills (prompt, and partly context)**, and the resolution is to scope it per-module, not to answer globally. The thesis is "you learn by doing it inside a harness." Making the workshop itself an agent-reachable artifact turns the workshop into a worked harness-engineering example the learner reads, drives, and extends, that is the thesis, intensified. The real dilution risk is concrete and must be named: if the learner's agent *does the exercise for them* (agent writes the prompt, agent grades it, human rubber-stamps), the human learns nothing and the workshop becomes learning-theatre. So the honest answer is "strengthens, conditional on a non-delegation rule per module," which is Q3.

**Q2: Does an agent-submitted completion claim need a stricter Human Gate than a human doing the same submission?**
**Yes, same authority, higher evidentiary bar, plus a non-delegation clause.** Coachgremlin's existing gate ("never certify external-consequence completion without human confirmation") already holds in principle; what changes with an agent submission is the *risk profile*, so the gate needs three concrete additions:
1. **Evidence, not a claim.** Because the human may not have watched the attempt, the run-ledger entry must carry the actual transcript/artifact, not just an assertion that it happened. (`output_artifact` already exists in the schema; add the transcript.)
2. **An explicit driver field.** Add `attempt_driver: human | agent | mixed` to the run entry. The gate reads differently depending on who drove.
3. **Attestation of understanding, not of existence.** For an agent-driven attempt, `human_confirmed: true` must mean "I can explain why this passes," not "an artifact exists and looks done." That is the specific defense against an agent producing a plausible artifact that games the rubric.

And a per-module **non-delegation clause**: for module 01, the human must have *authored* the prompt even if an agent runs and submits it, otherwise the module's entire skill is bypassed. Concretely, the gate is not a different approver; it is a stricter *record* (transcript attached, driver named) plus a stricter *meaning* of the human's click (understanding, not sighting).

**Q3: All five modules uniformly, or some more than others?**
**Not uniform.** Map it onto the structural/behavioral split the workshop already teaches:

- **01 Prompt: weakest fit, nearly a counter-example.** The skill *is* the human writing the instruction. Agent-native should be limited to submission/logging here, never authoring. Keep it essentially human-only.
- **02 Context: partial fit.** Deciding what to cut is human craft; the agent can legitimately assemble and measure the budget. Agent assists, human judges.
- **03 Harness: strongest fit.** The exercise is literally "configure what an agent can reach"; an agent-native interface *is* a harness-engineering artifact, and its gate already demands a machine-checkable config plus real run transcript. Maximum meta-consistency.
- **04 Loop: strong fit.** Loops are agent-driven by nature; a bounded loop that terminates is exactly what an agent runs and reports, and the verification-loop concept maps 1:1 onto submit → grade → feedback. This is also where the Human-Gate question bites hardest ("agent submits without a human watching"), so it's the best *stress test* of Q2.
- **05 Capstone: fits as orchestration**, but the written diagnosis-defense must stay human-authored.

So the feature belongs to **03, 04, and 05 in descending strength, explicitly not to 01, and only partially to 02**, which is itself a satisfying result, because it means agent-native interaction follows the same structural-vs-behavioral seam the workshop is built on.

## 4. Recommended pilot module: 03, Harness Engineering

Pick module 03. Reasons, strongest first:

1. **The medium is the message.** Module 03 teaches MCP, plugins/connectors, sub-agents, skills, worktrees, and CLI tool access, the exact vocabulary an agent-native interface is *built out of*. A learner whose harness consumes a manifest, or shells out to a `tv` CLI, or (later) speaks to a local MCP server is practicing the module's own content by using the workshop. This is the "real asset, not just narrative" the framing flags, and no other module gets it for free.
2. **Its gate is already machine-checkable.** The stated gate is "a harness config that actually runs, with a transcript," an artifact that is inherently agent-producible and observable, unlike module 01's "a good prompt," which is a judgment call an agent can't cleanly submit-and-prove.
3. **Lowest dilution risk among the strong-fit modules.** Designing a harness is an orchestration skill, precisely the kind that benefits from agent assistance without the human skipping the learning, and "a working harness plus transcript" is hard to fake in a way that games a rubric.
4. **The pilot artifact becomes teaching content.** Whatever manifest/CLI/persona the pilot produces can be shown *inside* module 03 as a worked example of a harness the learner can inspect. The infrastructure pays double.

**Acknowledged alternative: module 04.** Loop is even more agent-native by nature and stress-tests the Human Gate harder (unattended submission is the loop module's whole premise). It's a defensible pick. Module 03 leads because (a) 04 depends on 03 in the arc, (b) 03's target artifact (config plus transcript) is cleaner and less variable than 04's (loop definition plus terminal-state transcript), and (c) building the interface at 03 lets 04 reuse it as an immediate fast-follow. **Recommendation: pilot 03, fast-follow 04**, and use 04's follow-on specifically to pressure-test the stricter Human Gate from Q2.

## 5. Pilot implementation plan

Written at the altitude of `docs/implementation-plan.md`. This is a **static-first** pilot (Options A + E), with the CLI (Option C) staged as an explicit phase 2 and the MCP server (Option B) as phase 3 / a module-03 teaching artifact. Scope: **module 03 only**. This is a plan, not an implementation.

### Dependency note up front

The *real* rubric content for module 03 is a Coachgremlin content-building output that does not exist yet (`docs/next-actions.md` lists it as pending). The pilot therefore has a sequencing choice: (a) run Coachgremlin's module-03 content pass first and build the manifest around a real rubric, or (b) build the plumbing now against a rubric-*shape* placeholder consistent with the existing gate, and fill the rubric when content lands. **Recommendation: do them together**, the agent-native pilot and the module-03 Coachgremlin content pass are mutually reinforcing, and a manifest with a placeholder rubric only half-proves the concept. If they must be separated, ship the plumbing (b) first; it is independently verifiable.

### Files the pilot produces (repo-relative)

1. **`modules/.manifest.schema.yaml`**, the machine-readable schema for a module manifest, in the same style and location convention as `runs/.schema.yaml`. Fields: `schema_version`, `module_id`, `question`, `arc_position` (prior/next/hinge), `gate` (the "required to advance" line, structured), `rubric` (list of `{criterion, observable, weight}`, shape, filled from Coachgremlin content), `stop_condition`, `expected_artifacts` (list of `{kind, description}`, e.g. `harness-config`, `run-transcript`), `submission` (`{ledger_dir: runs/, id_prefix: AEW, driver_field: attempt_driver}`), and `human_gate` (the non-delegation clause plus attestation requirement for this module).
2. **`modules/03-harness-engineering/module.yaml`**, the module-03 instance of that schema. The single machine-readable source; the README stays the human-readable prose beside it (the exact "spec beside prose, don't duplicate" pattern already used by `site/src/content/config.ts`).
3. **`modules/03-harness-engineering/AGENT.md`**, the agent-facing entry point (counterpart to `README.md`): how a learner's harness consumes `module.yaml`, runs the exercise, and submits, and the explicit instruction that the agent must stop at a submitted run entry and never self-certify. Harness-neutral prose (no Claude-Code-only assumptions, directly honoring the review panel's End-User/Learner "harness-agnostic" finding for module 03).
4. **`coachgremlin/grader.md`** (new top-level dir), the Coachgremlin teaching loop (frame → rubric → observe → feedback → confirm/loop) distilled from the canonical `<hekton-machinery>/gremlins/coaching/coachgremlin.md` into a persona/subagent prompt the learner's own agent loads. Contains the hard rule: **output a rubric assessment and a recommended next step; never output a terminal "complete"/"certified" state; completion is only the human flipping `human_confirmed`.** Placed at repo top level (not inside module 03) because it is reused by every future module's pilot.
5. **`runs/.schema.yaml`**, extend (do not replace) with `task_type: exercise`, and add `attempt_driver: "human | agent | mixed"`, `module_id`, `rubric_scores`, and `coachgremlin_assessment` fields. `human_confirmed` and `human_notes` already exist and carry the gate.
6. **Phase 2 (staged, not core): `scripts/tv` (or `bin/tv`)**, a thin local CLI: `tv module show 03` (prints/validates the manifest), `tv submit <artifact> --module 03 --driver agent` (writes a `runs/run-YYYYMMDD-AEW-NNN.yaml` entry with `human_confirmed: false`), `tv confirm <run-id>` (human-only; flips the flag, prompts for `human_notes`). No grading inside the CLI, grading stays a `coachgremlin/grader.md` invocation. Document it as the middle-ground upgrade, ship after the static pilot verifies.
7. **Phase 3 (teaching artifact, not required): a local stdio MCP server** exposing `get_current_module` / `submit_attempt` / `get_feedback`, built *as part of module 03's own content* so the learner inspects a real MCP harness. Explicitly gated on the static pilot and CLI proving out first.

### Sequencing

1. **Schema first**, `modules/.manifest.schema.yaml` plus the `runs/.schema.yaml` extension. No dependencies; everything else references them.
2. **Grader persona**, `coachgremlin/grader.md`, distilled from canonical Coachgremlin. Parallelizable with step 1.
3. **Module-03 manifest**, `modules/03-harness-engineering/module.yaml`, ideally co-produced with the Coachgremlin module-03 content pass so the rubric is real. Needs steps 1-2.
4. **Agent entry point**, `modules/03-harness-engineering/AGENT.md`. Needs step 3 (points at the manifest).
5. **Dry-run verification** (see below), the load-bearing step; this is what turns a manifest into a proven pilot.
6. **Human-confirmation exercised once**, a real `human_confirmed` flip with an attestation note.
7. **Review-panel re-run, scoped**: Instructional Designer (does the gate survive an agent driving it?) plus Security-Conscious Reviewer (does agent-submitted-without-watching model an unsafe habit?) plus Skeptical Critic (are we overclaiming a "Coachgremlin interface" that's really the learner's own agent?). A scoped 3-persona re-run, not the full seven, per the panel's own "scoped re-run" guidance.
8. **Only then** decide whether to build phase 2 (`tv` CLI) and phase 3 (MCP), informed by what the dry run revealed.

### Verification (how you'd know it worked)

- **Schema valid:** `module.yaml` validates against `.manifest.schema.yaml` (a YAML-schema check, same class as the existing `verify-project.sh` / `check-mirror-drift.sh` checks).
- **End-to-end, real harness:** point an actual Claude Code (and, if available, a second harness to prove agnosticism) session at `modules/03-harness-engineering/`, have it parse `module.yaml`, produce a real harness-config plus run transcript, and write a `runs/` entry with `attempt_driver: agent`, `human_confirmed: false`. The *observed behavior*, not the file's existence, is the proof, this is the "drive the flow" bar, not a typecheck.
- **Human Gate holds:** confirm the agent stops at the submitted entry and never emits "complete"; confirm nothing downstream treats `human_confirmed: false` as passed; then exercise one human confirmation and check the attestation note is required, not optional.
- **Non-delegation honored:** confirm the module-03 gate can't be satisfied by the agent alone in a way that skips the human's understanding, i.e. the `human_notes` attestation is load-bearing.
- **No drift:** README prose and `module.yaml` agree on the gate and question (a drift check in the spirit of `check-mirror-drift.sh`, the "stale prose survived the rename" failure the panel already caught once must not recur across two sources of truth).
- **Harness-agnostic:** the `AGENT.md` contract contains no single-harness-only assumption; a second harness can consume it.

## 6. Risks and what goes wrong if built carelessly

- **Learning-theatre / delegation.** The sharpest risk: the agent does the exercise, the human clicks confirm, nobody learned anything. Mitigation: the per-module non-delegation clause (Q3) plus attestation-of-understanding gate (Q2). If the pilot can't demonstrate the human still did the load-bearing thinking, it has *disproven* the feature for that module, which is a valid and useful pilot outcome, don't paper over it.
- **Human-Gate erosion by terminal states.** If any interface (manifest field, CLI output, MCP response) can emit "complete"/"certified," agents will latch onto it. Mitigation: the grader contract forbids terminal completion; only `human_confirmed` flips state, and only a human can flip it. This must be tested, not just documented.
- **Rubric gaming.** A machine-readable rubric an agent optimizes to the letter, producing artifacts that pass the checklist but miss the point. Mitigation: keep rubric criteria observable but resist over-formalizing them into a mechanical checklist; lean on the human attestation for the spirit-of-the-rubric judgment.
- **Harness lock-in, the self-inflicted wound.** An MCP-only or CLI-only path breaks the workshop's "bring your own harness" promise and directly contradicts the review panel's existing harness-agnostic finding for module 03. Mitigation: the static manifest is always the base layer that any harness can consume; CLI and MCP are strictly optional enhancements, never the only door.
- **Public repo plus CI grading equals key/cost/abuse exposure.** Option D would put an LLM API key in a public GitHub Action. Mitigation: don't. Local grading by the learner's own agent keeps cost and secrets on the learner's side and is why the static pilot is preferred.
- **Building the service before proving the manifest.** Jumping to the MCP server first inverts the backlog's explicit "scoped pilot before generalizing" instruction and spends the highest-cost, highest-trust-risk option before the cheapest one has earned it. Mitigation: the phased sequencing above; MCP is phase 3 and doubles as module-03 teaching content, not the entry point.
- **Two sources of truth drifting.** README prose and `module.yaml` describing the same gate can diverge, the exact "stale prose survived a find-replace" defect the panel caught in the first review. Mitigation: a drift check, and a rule that the manifest is validated against (or generated with) the README, not maintained independently.
- **Overclaiming a "Coachgremlin interface."** Calling `submit_attempt → get_feedback` a live Coachgremlin service when it's really the learner's own agent role-playing a persona file is precisely the hedge-free overclaiming the Skeptical Critic exists to catch. Mitigation: name it honestly in `AGENT.md` and `coachgremlin/grader.md`, "your agent runs the grader persona locally," not "the workshop grades you."

## Critical files referenced

- `runs/.schema.yaml` (extend for exercise attempts plus `attempt_driver`; already carries `human_confirmed`)
- `modules/03-harness-engineering/README.md` (the module whose gate the manifest must mirror without drift)
- `<hekton-machinery>/gremlins/coaching/coachgremlin.md` (source to distill into the loadable `coachgremlin/grader.md` persona; owns the Human Gate)
- `site/src/content/config.ts` (the proven in-repo "machine-readable schema beside prose, no duplication" pattern to imitate for the manifest)
- `docs/implementation-plan.md` (the altitude/format template this pilot plan was written up against)
