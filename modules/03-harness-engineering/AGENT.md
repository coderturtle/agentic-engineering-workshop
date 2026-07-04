# Module 03, agent entry point

Counterpart to `README.md`, for a learner whose harness (Claude Code, Codex CLI, Cursor, or
equivalent) is doing some or all of the driving. If you're a human working through this module
directly with no agent involved, you don't need this file: `README.md` is complete on its own.

This is the pilot for `docs/agent-native-interaction-plan.md`: a machine-readable manifest
(`module.yaml`) plus this harness-agnostic instruction sheet, not a live Coachgremlin service.
There is nothing to call. Your own agent, loaded with `../../coachgremlin/grader.md`, is the
grader. Say so honestly in anything you write about this attempt: "my agent ran the grader
persona locally," never "the workshop graded me."

## What to read, in order

1. `module.yaml` (this directory): the machine-readable question, gate, rubric, and stop
   condition. Parse this instead of scraping `README.md`'s prose.
2. `README.md`: the exercise task itself, the "Why this is hard" section, and the harness
   translation table. `module.yaml` mirrors this file's gate and question; if you find them
   disagreeing, stop and flag it rather than trusting either silently. **Skip the "Takeaway"
   section on this first read**: it opens with its own warning not to read it before a first
   attempt, because it names the reference implementation directly. Come back to it only after
   you've completed and submitted your own attempt.
3. `../../coachgremlin/grader.md`: load this as your grading persona before you assess your own
   (or the learner's) attempt.
4. `../../runs/.schema.yaml`: the ledger schema your submission must conform to.

## What to do

1. Parse `module.yaml`'s `expected_artifacts` and `stop_condition`. Build the harness config it
   describes (a bounded sub-agent/specialist, persistent on-disk state, a demonstrated context
   reset) against the `--by-category` task in `fixtures/receipts/`, exactly as `README.md`
   describes it. Put the persistent-state/progress file at the fixture root (e.g.
   `fixtures/receipts/.receipts-category-progress.md`), a sibling of `receipts/` and `tests/`, not
   inside `receipts/` itself: the exercise requires this artifact to exist, so writing it is not a
   violation of "touch `receipts/`, nothing else," but it isn't part of the CLI package either.
2. Run it for real. A described config is not a run config: `module.yaml`'s `Actually ran`
   criterion is a gate, not a nice-to-have. Produce the run-transcript artifact as you go, not as
   a summary written after the fact.
3. Demonstrate the reset-and-resume for real, per `README.md`'s instructions, including the second
   check (rerunning phase 2 once more with the notes file withheld), and don't skip it because the
   first pass succeeded.
4. Load `coachgremlin/grader.md` and self-assess against `module.yaml`'s `rubric`. Write the
   assessment honestly, including where a criterion looks staged rather than earned.
5. Write a `runs/` entry per `runs/.schema.yaml`: `task_type: exercise`, `module_id:
   03-harness-engineering`, `attempt_driver` set to whoever actually drove (`human`, `agent`, or
   `mixed`, not who's reviewing), `rubric_scores`, `coachgremlin_assessment`, and
   `human_confirmed: false`.
6. **Stop there.** Do not set `human_confirmed: true` yourself, do not tell the learner they've
   passed, and do not advance to Module 04 on the strength of your own self-assessment. That flip
   is a human decision, and per `coachgremlin/grader.md`'s attestation rule, it means "I reviewed
   this and understand why it passes," not "an artifact exists." If you are drafting `human_notes`
   for a human to review, leave the field itself for them to write in their own words; don't
   ghostwrite the attestation you're supposed to be attesting to.

## Non-delegation

Module 03's skill is orchestration and verification (what to scope in/out, where state lives, how
a reset is actually confirmed), not typing a config file. If a human asks you to "just build the
harness," build it, but make the scoping and verification decisions visible in the transcript
(what you excluded and why, how you actually confirmed the reset) so a human reviewing it later can
tell judgment happened, not just that a file got written. See `module.yaml`'s
`human_gate.non_delegation_clause`.

## Harness-agnostic by design

Nothing above assumes Claude Code specifically. `README.md`'s translation table maps sub-agents,
worktrees, MCP servers, and skills across Claude Code, Cursor, and Codex CLI: use whichever
mechanism your harness actually enforces, and note in your transcript whether the boundary you
declared is genuinely enforced by your harness or just requested of it (the table's own
"Enforcement isn't equivalent across the row" warning). A CLI or MCP-server pilot may exist for this
module later (`docs/agent-native-interaction-plan.md` §5, phases 2-3); this manifest is the base
layer any of those would sit on top of, not a bet on one harness.
