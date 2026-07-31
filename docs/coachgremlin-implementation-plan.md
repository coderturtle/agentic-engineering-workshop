# Content-Building Plan: Coachgremlin's First Authoring Pass Across Terminal Velocity

> Produced by an Opus-run research/planning pass (2026-07-03), reading `<hekton-machinery>/gremlins/coaching/coachgremlin.md`, `<hekton-machinery>/gremlins/workshop/workshop-lifecycle.md`, all five module READMEs plus `modules/README.md`, `docs/workshop-design.md`, `docs/review-panel/2026-07-03-initial-design.md`, `docs/agent-native-interaction-plan.md`, `docs/brand.md`, and `runs/.schema.yaml`. This is a plan, not an implementation — nothing here has been built or authored into the modules yet.

**Status:** plan, not implementation. Read-only pass.
**Scope:** author real exercise specs, rubrics, stop conditions, and takeaway-packaging instructions for all five modules, replacing the `_(rubric + terminal state defined per exercise by Coachgremlin)_` placeholders. Recommend and scope Coachgremlin's first real run.
**Altitude:** matches `docs/implementation-plan.md` and `docs/agent-native-interaction-plan.md`.

A note on where this doc lives: it is a working `docs/` planning file and so is exempt from the em-dash hard rule (`docs/brand.md`). The exercise prose it specifies is destined for published `modules/` content and must pass `scripts/check-brand-lint.sh` when actually authored. Sample exercise text quoted below is already written to that rule.

## 1. Coachgremlin's Workflow, as the frame everything hangs off

From `<hekton-machinery>/gremlins/coaching/coachgremlin.md`, the six-step Workflow (step 6 added earlier today, still unproven):

1. **Frame the exercise**: a bounded, real, harness-driven task. State the stop condition and the takeaway form up front.
2. **Set the rubric**: 3 to 6 observable, scored criteria, shared before the attempt.
3. **Observe the attempt**: read the transcript/diff/output. Do not intervene mid-attempt except on tooling.
4. **Give feedback against the rubric**: what worked, what did not, one concrete next try. No solution handed over.
5. **Confirm or loop**: rubric met, mark taught, hand back. Not met, propose a smaller/adjacent exercise, not a repeat.
6. **Package the takeaway**: shape the artifact into its stated keepable form (Skill / hook / sub-agent definition / loop template).

Two hard constraints wrap the whole thing: Coachgremlin **never lectures and never hands over the solution**, and it **never certifies external-consequence completion without a human** (the Human Gate). Its Lifecycle Phase is **Learn**, distinct from Workshop Gremlin's **Build** (`workshop-lifecycle.md`).

**How this authoring pass maps onto the Workflow.** Authoring content upfront is pre-writing steps 1, 2, and the *target shape* of 6 for each module (the frame, the rubric, the takeaway form). Steps 3, 4, 5 and the *act* of 6 are exercised live, once per learner, later. The one place all six get tested before we commit to five modules is the recommended first real run (Section 5), which is a genuine dry-run attempt driven through the full loop.

## 2. Per-module specs (arc order)

All five exercises run against **one shared fixture repo**, the cumulative spine (Section 3). The fixture is a small, deliberately-flawed CLI, `receipts`: a tool that parses expense-receipt CSV rows and prints summaries. It ships one seeded bug (timezone-naive month grouping), a thin test suite, a noisy "bloated" variant, and sabotaged variants for the capstone. It is a prerequisite deliverable (Section 6). A widely-readable small stack (Python or TypeScript, pick one and hold it) keeps diffs legible for the advanced-practitioner audience.

Language and voice for the authored prose: system/instructional register per `docs/brand.md`, treats the reader as a capable peer, no em dashes, no efficacy superlatives, no course-marketing framing.

### Module 01: Prompt Engineering

**The osmosis problem it must beat (review panel #4, Instructional Designer):** an advanced practitioner already writes decent prompts daily. The exercise has to establish a *new* capability, not review osmosis. The new capability is the shift from "get a plausible answer once" to "specify tightly enough that the output is *determined*, reproducibly, first try."

**Exercise.** Against the fixture, write a single-turn prompt that makes the learner's agent produce a correct implementation of one specified function, first try, no correction turn:

> Write one prompt that produces a correct `group_expenses_by_month(rows, tz)` from this signature and spec, passing the provided test file, on the first try with no follow-up turn. The spec names four edge cases: empty input, a receipt whose UTC timestamp crosses a month boundary in the target timezone, duplicate timestamps, and a malformed row. Run your prompt three times from a clean session. All three outputs must pass.

The hardness is the edge cases a naive prompt drops. The discriminator against osmosis is **reproducibility**: one lucky pass is a plausible output; three-for-three is a specified one.

**Rubric (observable, scored):**
1. **First-try pass (gate).** Output passes all provided tests with zero correction turns.
2. **Reproducibility (scored).** Three consecutive fresh runs of the same prompt all pass. Any flaky run costs the criterion.
3. **Edge-case coverage in the instruction (scored).** The prompt *names* the four edge cases rather than hoping the model infers them. Score is the fraction named.
4. **Constraint economy (scored).** No contradictory or dead constraints; each constraint is traceable to a specific failure it prevents.
5. **Output-shape control (scored).** Exact signature, return type, and format specified so the output is drop-in, not hand-reshaped.

**Stop condition / terminal state.** A single prompt that yields a first-try, test-passing implementation on three consecutive clean runs, no correction turn. **Valid alternate terminal:** if, after several prompt revisions, the task genuinely cannot be made first-try single-turn, the learner names *why* and classifies it as "outgrown one prompt." That is learning objective 2 firing, and it is a pass, not a failure.

**Takeaway packaging.** Lift the winning prompt into a parameterized template: mark fixed scaffolding versus fill-in-the-blank slots (`{signature}`, `{edge cases}`, `{output format}`), and annotate each constraint with the failure it prevents. Save as a real harness snippet the learner will reuse: a Claude Code slash command (`.claude/commands/spec-impl.md`), a Cursor/Codex snippet, or a plain snippet-library entry, plus a one-line "when to reach for this." Deliverable is the template, not the raw prompt.

**Harness decision: harness-agnostic.** Nothing here is Claude-Code-specific. Only the takeaway's *storage form* names per-harness options, and it lists three.

### Module 02: Context Engineering

**Cumulative hook:** same task as Module 01, now buried in noise. The lesson lands hard precisely because the learner already has a proven prompt: a perfect instruction still fails when the window is wrong or missing what it needs.

**Exercise.** The fixture's **bloated variant** dumps to roughly 12k lines (long README, CHANGELOG, an unrelated `legacy_export.py`, stale docs, a red-herring config). The learner gets a fixed budget (state it concretely, e.g. ~2,000 lines or ~8k tokens, measured by a provided `scripts/context-budget.sh`):

> Curate this repo down to the stated budget, then run the Module 01 task again inside the curated context. It must still pass. Write a short justification: what you kept verbatim, what you summarized, what you cut, and why.

The post-curation task's correctness depends on including the right slice; the distractors live in the noise.

**Rubric:**
1. **Budget met (gate).** Assembled context is at or under the stated budget, measurably.
2. **Task still correct (gate).** Output passes with the curated context.
3. **Necessary inclusion (scored).** The specific lines the task depends on are present verbatim, not summarized away.
4. **Justified exclusion (scored).** The write-up names what was cut and why; nothing load-bearing was cut.
5. **Summarize-vs-verbatim judgment (scored).** Verbatim reserved for what must be exact (the function under test, its signature); summary used for orienting material.
6. **No noise smuggled (scored).** The red-herring config and unrelated module are excluded.

**Stop condition.** Curated context at/under budget plus passing output plus a justification covering keep/summarize/cut. **Alternate terminal:** if it cannot pass under budget, the learner identifies the single inclusion that would fix it. Diagnosing the missing piece is the skill.

**Takeaway packaging.** Distill the justification into a **context-budgeting Skill**: an ordered checklist ("what to keep, what to cut, in what order") plus the keep/summarize/cut heuristic, packaged as a Claude Code `SKILL.md` (or harness equivalent) loadable in future sessions. The one-off curation becomes loadable judgment.

**Harness decision: agnostic exercise, Claude-Code-leaning takeaway with an explicit translation note.** The curation task is universal; only budget *measurement* touches tooling (ship a harness-neutral line/char counter, note token-counting per harness). The Skill packaging is shown in Claude Code's `SKILL.md` form with a "translate to your tool" pointer.

### Module 03: Harness Engineering

**Cumulative hook:** the harness *operationalizes* Modules 01 to 02. It runs the specified task repeatedly with the curated context, instead of the learner hand-driving each turn.

**Exercise.** Configure a harness for a bounded extension of the fixture, "add a `--by-category` summary to the receipts CLI," with four requirements:

> (a) Define a sub-agent or specialist with a bounded tool and file scope (it can touch `src/receipts/` and run tests, nothing else). (b) Give it persistent on-disk state, a progress/notes file it writes and re-reads. (c) Demonstrate a context reset mid-task where the agent resumes from that state rather than restarting cold. (d) Show it actually running, with a transcript. Optionally isolate the work in a git worktree.

The gate is already "a harness config that actually runs, with a transcript." The observable that separates a *real* harness from a *described* one is the reset-and-resume.

**Rubric:**
1. **Bounded reach (scored).** The config grants only the access the task needs; over-broad access (full-repo write, network) is scoped out, and the boundary is explicit.
2. **Sub-agent/specialist boundary (scored).** A named specialist with a stated single responsibility, not a monolith.
3. **Persistent state survives reset (gate + scored).** On-disk state exists; a demonstrated context reset resumes from it.
4. **Actually ran (gate).** Transcript shows the configured harness executing the task correctly, not just described.
5. **Isolation, conditional (scored).** If worktrees are used, experimental work does not collide with the main checkout.
6. **Reusable generality (scored).** The config is not hard-wired to one path in a way that cannot transfer.

**Stop condition.** A harness config that runs the task to a correct result, with a transcript that includes a mid-task context reset resumed from persistent state. The reset-and-resume is demonstrated, not asserted.

**Takeaway packaging.** The sub-agent / harness-config definition itself, generalized: a `.claude/agents/*.md` sub-agent file (or MCP server config / harness equivalent) with the fixture-specific paths parameterized out, drop-in for a real project. This is the **strongest-fit** module (artifact is nearly the takeaway); packaging is a light distillation (strip fixture specifics, add a scope/why header, save to the learner's real agents library).

**Harness decision: Claude-Code-leaning, explicitly, with a mandatory translation table.** This is where the review panel's harness-agnostic concern (#6) bites hardest: sub-agents, skills, worktrees, and MCP are Claude-Code-shaped vocabulary that does not map cleanly onto Cursor. A vague "harness-agnostic" version would be unteachable. Decision: teach it concretely in Claude Code, and require a mapping table in the module (Claude Code sub-agent to Cursor rules/modes to Codex equivalent; worktree to branch/clone; MCP to the harness's tool/plugin mechanism).

**Agent-native intersection (note, do not design here).** Per `docs/agent-native-interaction-plan.md`, Module 03 is the agent-native pilot, and that plan says the module-03 Coachgremlin content pass and the agent-native manifest "are mutually reinforcing... do them together." Two concrete intersections this content pass must respect: (1) the rubric authored here is the exact content that would fill the `rubric` field of `modules/03-harness-engineering/module.yaml`, so it should be written in the `{criterion, observable, weight}` shape that manifest expects, to avoid a later re-derivation and the two-sources-of-truth drift that plan warns about; (2) the "actually ran, with a transcript" gate is inherently machine-checkable, which is why 03 was chosen as the pilot, so the stop condition here should stay observable rather than a judgment call. Designing `module.yaml`, `AGENT.md`, or the grader persona is out of scope for this content pass.

### Module 04: Loop Engineering

**Right-sizing the four sub-concepts (review panel deferred item).** The panel flagged that Module 04 carries four sub-concepts (agent / verification / event-driven / hill-climbing) plus three named patterns on the same "one exercise" budget as every other module. Resolution: **one required core exercise plus three bounded, optional, graded extensions**, rather than four heavy exercises or a module split. The core covers the two load-bearing layers (agent loop plus verification loop) and the stop-condition skill; each extension targets one remaining sub-concept.

**Cumulative hook:** the loop runs *inside Module 03's harness* (loop is the behavioral layer on top of the structural one). This makes the arc's "a loop needs a harness to run inside" claim concrete, not narrative. For the standalone first-run dry run (Section 5), the loop may run in a default harness; the wiring to the Module 03 artifact is finalized once 03 is authored.

**Core exercise (required gate): Ticket-to-PR-Ready Loop.** The fixture ships the seeded timezone bug with a failing test. Before building, the learner writes one sentence classifying the ticket as a stable goal (worth a loop) and names one moving-target counter-example they would *not* loop-ify (the stable-goal-vs-moving-target rule). Then:

> Build and run a bounded loop: reproduce, root-cause, smallest fix, rerun tests. State both terminal states up front: success is tests green; failure is "cannot reproduce after two attempts." Submit the loop definition and a transcript showing the terminal state firing.

**Extensions (optional, graded if attempted):**
- **A. Verification loop, deepened.** Add a grading pass beyond the tests, e.g. a check that the fix is minimal and does not touch unrelated files (blast radius), sending back on failure.
- **B. Event-driven loop.** Wire the loop to an external trigger. Reuse this repo's own dogfooded precedent: the pre-push git hook that already runs `check-brand-lint.sh` (`workshop-lifecycle.md`, "Docs Consistency Loop"). Convert the manual loop into a triggered one.
- **C. Hill-climbing loop (the "ralph loop" material), taught with the mandatory gate.** Run the loop over two or three tickets, collect the transcripts, do one analysis pass that *proposes* a rewrite to the loop's own prompt/config, and gate it: the proposal must pass the existing tests (regression-free) **and** get an explicit human review before adoption. The deliverable is a proposed diff plus the review-gate note, never an auto-applied change. This directly closes the AI/ML plus Security reviewer finding (#2) that a learner must not copy auto-apply as the default.

**Rubric (core):**
1. **Stop condition stated before running (gate).** Both terminal states named up front.
2. **Terminated correctly (gate).** Transcript shows the terminal state firing, not an infinite loop or a manual kill.
3. **Verification is external (scored).** The loop trusts the test result, not the agent's own "I fixed it."
4. **Smallest-fix discipline (scored).** Blast radius bounded; unrelated code not rewritten to pass.
5. **Decision rule applied (scored).** Ticket correctly classified as loop-worthy; a moving-target counter-example given.
6. **Review gate present, conditional (gate if extension C attempted).** Any proposed self-rewrite is a reviewed, verification-gated proposal, never auto-applied.

**Stop condition.** Loop definition plus a transcript where a real terminal state fires (green tests, or the two-attempt reproduce-failure state). Observable: the loop stopped itself.

**Takeaway packaging.** Generalize the loop into a **reusable loop template** in the Ticket-to-PR-Ready style (a slash command / script / documented pattern), carrying its stop condition and verification step named explicitly. If extension C was done, the template must carry the review-gate requirement inline, not just the mechanism.

**Harness decision: agent-loop mechanics agnostic; concrete build Claude-Code-leaning with translation notes.** The loop *concept* is universal. The required build (slash command, hook) is shown in Claude Code with a mapping note; extension B's git hooks are agnostic and already modeled in-repo.

### Module 05: Synthesis Capstone

**The genuine-ambiguity requirement (review panel #5 plus Instructional Designer risk):** the scenario must be constructed so the bottleneck could plausibly be *any* of the four layers, and it must not reuse Module 04's "build a loop that terminates" shape. Two design techniques enforce this:

1. **Layer-neutral surface symptom.** The learner sees something like "the agent's fixes keep failing review" or "the loop never reaches done," a symptom that any of the four layers could cause.
2. **The obvious culprit is not the real one, and the real one varies across variants.** Ship two to four sabotaged variants of a full agent setup (prompt plus context plus harness plus loop, all provided) whose *true* bottleneck differs by variant (one context, one harness, one prompt, one loop). The prompt looks a little sloppy (tempting prompt fix) and the context looks bloated (tempting context fix), but in a given variant the real bottleneck is elsewhere, e.g. the verifier sub-agent cannot reach the test command (harness), or success is checked wrong so the stop condition never becomes true (loop). The learner does not know which variant they got, so they cannot pattern-match the answer. Because the setup is *diagnosis of a provided system* rather than *construction of a loop*, it does not collapse into Module 04.

**Cumulative hook:** each variant is a deliberately-sabotaged assembly of the same four artifact types the learner built in Modules 01 to 04. Diagnosis is literally "find which of the four things you learned to build is the one broken here."

**Exercise.**
> Here is a broken agent task, harness and prompt and context and loop all provided, that fails its goal. Instrument it. Form a hypothesis about which single layer is the bottleneck. Confirm with evidence: isolate by fixing one layer in a throwaway and seeing whether the failure moves. Apply the minimal fix to that layer only. Write a defense: why this layer, not the other three, citing the evidence that ruled each out.

**Rubric:**
1. **Correct layer identified (gate).** The diagnosed bottleneck is the actual one.
2. **Evidence, not guess (scored, heavily weighted).** Diagnosis is backed by an isolating test (changed one variable, observed the failure move or stay), not the most obvious symptom.
3. **Ruled out the other three (scored).** The defense explicitly says why each other layer was not the bottleneck, with evidence.
4. **Minimal fix (scored).** Fixed the diagnosed layer without shotgun-correcting the other three.
5. **Fix works (gate).** After the fix, the task succeeds.
6. **Layer attribution articulated (scored).** The defense attributes the fix to the layer's definition ("a harness problem, not a prompt problem, because the tool could not reach X").

**Stop condition.** Correct diagnosis plus working minimal fix localized to one layer plus a written defense that rules out the other three with evidence. The defense must survive the "why not the other three" test.

**Takeaway packaging.** The **personal diagnostic playbook**, as a Skill: a symptom to suspect-layer to how-to-confirm to how-to-fix checklist compressing all four layers into one repeatable method (`.claude/skills/diagnose-agent-failure/SKILL.md` or equivalent). Built by generalizing the isolating-test method the learner just used plus the "rule out the other three" discipline. The workshop's single most reusable artifact.

**Harness decision: diagnostic method agnostic; shipped scenario Claude-Code-shaped with translation notes.** Diagnosis is a mental method and fully portable. The broken scenario is a concrete harness, which is Claude-Code-shaped because Module 03 established that; provide it in Claude Code form with translation notes. The playbook takeaway is fully agnostic.

## 3. How the modules were made cumulative, and why

The review panel's deferred item said: design exercises as cumulative across modules, not independent silos, if "the sequence really builds" is to hold. Concretely:

- **One shared fixture (the `receipts` CLI)** threads all five modules. A learner works the same small domain throughout, so cognitive load stays on the *concept per module*, not on re-learning a new toy problem five times.
- **02 reuses 01's exact task, now buried in noise.** The learner already holds a proven prompt from 01, so 02's lesson ("a perfect instruction still fails on the wrong context") is felt, not told. This is the strongest single cumulative link: it turns the arc's abstract "prompt is necessary but insufficient" claim into a concrete experience.
- **03's harness operationalizes 01 to 02.** The harness runs the specified task with the curated context repeatedly, instead of hand-driving. The learner sees the manual work of the first two modules become structural.
- **04's loop runs inside 03's harness.** This makes the arc's load-bearing dependency claim ("you cannot design a loop for a harness you have not defined") concrete: the loop literally uses the sub-agent and persistent state from 03.
- **05 is a sabotaged assembly of the four artifact types from 01 to 04.** Diagnosis is "find which of the four things you built is broken here," so the capstone composes the prior four rather than introducing a fifth topic.
- **The takeaways compound too.** The 01 prompt template becomes the prompt inside the 03 harness and the 04 loop; the 02 context Skill informs what the harness loads. A learner finishing the arc holds a small kit whose parts fit together.

**Guard against the coupling's downside:** ship a *reference artifact* for each module so a learner who skips one, or whose earlier attempt was weak, can still enter the next module cold. Version the fixture so a fixture change does not silently break four modules.

## 4. Harness-agnostic vs. Claude-Code-leaning, per module

| Module | Decision | Why |
|---|---|---|
| 01 Prompt | Agnostic | Prompting is universal. Only the takeaway's storage form names per-harness options. |
| 02 Context | Agnostic exercise, CC-leaning takeaway plus translation note | Curation is universal; only budget measurement and the `SKILL.md` packaging touch tooling. |
| 03 Harness | CC-leaning, explicit, with a mandatory mapping table | Sub-agents / skills / worktrees / MCP are CC-shaped and do not map cleanly onto Cursor. A vague agnostic version is unteachable. Table maps CC to Cursor to Codex. |
| 04 Loop | Concept agnostic; core build CC-leaning plus notes; event-driven extension agnostic (git hooks) | Loop mechanics port; the concrete slash-command build does not. |
| 05 Capstone | Method agnostic; shipped scenario CC-shaped plus notes | Diagnosis is portable; the broken harness inherits 03's shape. |

The through-line: agnosticism tracks the workshop's own structural-vs-behavioral seam. The atomic-craft modules (01, 02) are portable; the structural module (03) and the things built on it (04, 05) lean Claude Code and pay it back with explicit translation tables. This is the same seam the agent-native plan found (agent-native fit is strongest at 03/04/05), which is a good internal-consistency signal.

## 5. Coachgremlin's first real run

**Recommendation: Module 04's Ticket-to-PR-Ready core.**

This is Coachgremlin's real "first run," the way `terminal-velocity` was Workshop Gremlin's. Coachgremlin is `draft`, has never run, and its two least-proven Workflow steps are step 3 (**observe the attempt**) and step 6 (**package the takeaway**, added only today). A first run should exercise both meaningfully, cheaply, and against a case where success is easy to judge.

**Why 04 core over the cheaper alternatives:**
- **It has the clearest observable terminal state of any module:** "tests green, or cannot reproduce after two attempts." Step 3 (observe) is exactly grading against an attempt; if Coachgremlin can grade *this*, the observe step is proven on the easiest-to-judge case, and if it cannot, we learn that before authoring four more modules.
- **Its takeaway is a real transformation** (a one-off loop generalized into a template carrying its stop condition), so step 6, the newest and least-proven step, gets a genuine test. Modules 01 and 03 under-test step 6 because their artifact is nearly the takeaway already.
- **It is grounded in a named source pattern** (Ticket-to-PR-Ready), so Coachgremlin frames rather than invents. Lower authoring risk for a first run.
- **It forces the shared fixture to be built first** (seeded bug plus failing test), which every other module reuses, so the first run also de-risks the cumulative spine. The fixture cost is not sunk; it is leverage.
- **It exercises the Human Gate and the no-handover rule for real:** there is a live temptation to just show the fix, and a real (external-consequence-free) completion to certify.

**Why not the cheaper Module 01.** 01 is genuinely cheaper (no fixture harness needed, just a spec and a test file), and is a reasonable alternative. It is not the pick because its observe step is the simplest kind (read a prompt and an output) and its takeaway packaging is the thinnest of the five (a template with little distillation). It would validate that Coachgremlin *runs*, but tell us little about whether its two riskiest steps hold. Cheapness that skips the risky steps is a weak first run.

**Note on the agent-native pilot.** `docs/agent-native-interaction-plan.md` recommends Module 03 as the agent-native pilot and says to co-produce it with 03's Coachgremlin content pass. That is a different question (validating an agent-native manifest, not validating the authoring Workflow). Recommendation: Coachgremlin's first *content* run is 04 core; **03 is the second content pass**, co-produced with the manifest, so both efforts still converge on 03 for the agent-native work. The two do not compete for "first."

**What success looks like for this dry run** (this is the go/no-go before authoring the other four):
- Coachgremlin can **frame** 04 core from the module README's gate, takeaway, and Ticket-to-PR-Ready pointer, without inventing an unrelated scenario.
- Given a **deliberately good** attempt and a **deliberately weak / rubric-gaming** attempt (a loop that "passes" by deleting the failing test, or by an unbounded fix), the rubric **discriminates** and Coachgremlin **catches the weak one**. This is the direct test of review-panel finding #7 (grader trust asserted, not shown).
- Coachgremlin's **feedback references the actual transcript**, gives one concrete next try, and **never hands the fix over** (checked against its Completion Checklist).
- The **terminal state is observed firing** in the transcript, not asserted.
- Step 6 produces a **loop template that actually helps on a second, different ticket** (drop-in test), not just a file that was written.
- The **Human Gate holds:** completion is a recommendation with `human_confirmed: false` in a `runs/` entry, not a self-certified "complete."

If the dry run fails any of the first three, that is a finding about *Coachgremlin*, not the module, and it should feed a revision of `coachgremlin.md` before the other four are authored. Coachgremlin stays `draft` until it has 3+ real runs (its own Review Trigger; `workshop-lifecycle.md` deliberately declined to loop-ify the Gremlin-revision cycle until then).

## 6. Sequencing and dependencies for the full pass

Authoring order differs from learner (arc) order. It is driven by the shared fixture and the first-run choice.

0. **Build the shared fixture repo** (prerequisite for 02, 03, 04, 05). The `receipts` CLI plus signature/spec for `group_expenses_by_month` plus a 3-test suite with one seeded-bug failure plus the bloated-context variant plus the sabotaged capstone variants. Keep it minimal; a first-run fixture does not need to be large. This is the single highest-leverage deliverable.
1. **Author Module 04 core, which is Coachgremlin's first real run plus dry run plus retro** (Section 5). Gate the rest of the pass on the dry-run outcome.
2. **Apply the retro's lessons to `coachgremlin.md` if step 3/6 surfaced gaps.** Then author **Module 01** (cheap, atomic; validates the simplest observe case; reuses the fixture's function spec).
3. **Author Module 02** (reuses 01's task under the fixture's bloat; needs the bloated variant from step 0).
4. **Author Module 03**, co-produced with the agent-native manifest per `docs/agent-native-interaction-plan.md` (schema, then grader persona, then `module.yaml`, then `AGENT.md`). Write the rubric in the manifest's `{criterion, observable, weight}` shape to avoid drift.
5. **Author Module 04's extensions** (verification-deepen, event-driven, hill-climbing) now that core is proven and 03's harness exists for the "loop runs inside the harness" cumulative link.
6. **Author Module 05 last**, because it composes sabotaged versions of the 01 to 04 artifacts and cannot be built before they exist.
7. **Re-run the Workshop Review Panel on real content** (per `docs/next-actions.md`), verifying each module's exercise satisfies its gate *and* produces its takeaway, not just that both are written.

**Dependency summary:**
- Fixture feeds 01, 02, 03, 04, 05.
- 01's task/spec feeds 02 (same task under noise).
- 03's harness feeds 04 extensions plus 04's cumulative link (soft: 04 core can dry-run in a default harness).
- 01 to 04 artifacts feed 05 (sabotaged into variants).
- 03 content pass and the agent-native manifest are co-produced.
- 04-core dry-run retro gates authoring of 01, 02, 03, 05 and Coachgremlin's own draft to v0 trigger.

## 7. Verification: how you'd know each module's content actually works

"Written" is not "works." For each module, run a real dry-run attempt through Coachgremlin's full Workflow and check:

- **Attemptable end to end.** An agent-literate learner can complete it in bounded time without needing content that does not exist yet.
- **The rubric discriminates (the load-bearing check).** Run a deliberately strong attempt *and* a deliberately weak / rubric-gaming attempt; the rubric must score them differently and Coachgremlin must catch the weak one. This is the concrete answer to review-panel finding #7 (grader trust). Do it per module, not once.
- **The stop condition fires observably.** 01: three-for-three reproducibility. 02: budget met plus pass. 03: reset-and-resume shown. 04: terminal state fires in the transcript. 05: fix localized to one layer, task passes.
- **The takeaway is genuinely reusable.** Drop the packaged artifact into a *different* task and confirm it helps. A file that exists is not the bar; "the learner leaves with something usable" is.
- **No lecture, no handover.** Coachgremlin's feedback references the actual attempt and never hands the solution (its Completion Checklist).
- **The cumulative link holds.** The prior module's artifact actually plugs into this one (01's prompt into 03's harness; 02's task under 03's harness; 03's harness under 04's loop; 01 to 04 into 05's scenario).
- **Brand-clean.** Published exercise prose passes `scripts/check-brand-lint.sh` (no em dashes, no banned phrases) and reads as a competent peer, not a course-marketing page.
- **No manifest drift (03).** README prose and `module.yaml` agree on gate and question (the `check-mirror-drift.sh`-class check the agent-native plan calls for).

Aggregate gate: the Workshop Review Panel re-run (Section 6, step 7) is the whole-pass verification, and per its own charter it can only meaningfully evaluate *content that exists*, which is why it runs after authoring, not before.

## 8. Risks

- **Grader trust / rubric gaming (panel #7).** A machine-readable rubric an agent optimizes to the letter while missing the point. Mitigation: an adversarial (rubric-gaming) attempt in every module's dry run; keep criteria observable but resist over-formalizing into a mechanical checklist; lean on the human attestation for spirit-of-the-rubric judgment. This is also Coachgremlin's own open question and its path from draft to v0.
- **Cumulative coupling brittleness.** A fixture change breaks four modules; a learner who skips one cannot start the next. Mitigation: ship a reference artifact per module for cold entry; version the fixture.
- **The osmosis problem (01) (panel #4).** Advanced learners find 01 trivial and disengage. Mitigation: the reproducibility / "predictable not plausible" twist and the first-try-no-correction constraint raise the bar past daily use; the alternate "outgrown one prompt" terminal keeps it honest.
- **Harness lock-in (panel #6).** CC-leaning modules exclude Cursor/Codex users. Mitigation: mandatory translation tables in 03, 04, 05; agnostic cores; the static-manifest base layer (agent-native plan) any harness can consume.
- **Capstone telegraphing (panel #5 plus Instructional Designer).** Learner pattern-matches the answer or the capstone collapses into Module 04's shape. Mitigation: multi-variant scenarios with differing true bottlenecks, obvious-culprit-is-not-the-real-one, diagnosis-not-construction task type, evidence-required rubric weighting.
- **Module 04 scope creep.** Four sub-concepts overwhelm one exercise. Mitigation: required core plus optional graded extensions, budget proportional to the sub-concepts.
- **Hill-climbing unsafe default (panel #2).** A learner copies auto-apply. Mitigation: the review gate is a scored gate criterion in 04, and the loop template must carry it inline.
- **Coachgremlin itself is unproven, and step 6 is one day old.** The first run may reveal Workflow gaps. Mitigation: 04-core-first dry run as the deliberate probe; do not author all five before the retro; Coachgremlin stays draft until 3+ runs (its own Review Trigger).
- **Human Gate erosion under agent-native (03/04).** An agent submits, a human rubber-stamps, nobody learns (learning theatre). Mitigation: the attestation-of-understanding and per-module non-delegation clause from `docs/agent-native-interaction-plan.md`; if the pilot cannot show the human did the load-bearing thinking, that is a valid disproving outcome, not a paper-over.
- **Fixture stack choice excludes some learners.** Mitigation: a small, widely-readable stack, language-agnostic diffs, keep it tiny.

## Critical files referenced

- `<hekton-machinery>/gremlins/coaching/coachgremlin.md` (the six-step Workflow this pass authors content against, and the Human Gate the dry run must not violate)
- `modules/04-loop-engineering/README.md` (the first-real-run module; its gate, takeaway, and Ticket-to-PR-Ready pointer are the raw material for Section 5)
- `docs/workshop-design.md` (arc reasoning, loop taxonomy, sourced patterns, stable-goal-vs-moving-target rule that every module's spec draws on)
- `docs/review-panel/2026-07-03-initial-design.md` (the "Deferred to the content-building phase" constraints this plan must satisfy)
- `runs/.schema.yaml` (the ledger that records each dry run with `human_confirmed`, the concrete form the Human Gate and the first-run success record take)
