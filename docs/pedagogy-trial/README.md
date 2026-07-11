# Minimum-viable pedagogy trial

Designed, not yet run. Answers `docs/next-actions.md`'s top-priority open item from the 2026-07-11
critical review (`docs/review-panel/2026-07-11-harness-hypothesis-critical-review.md`) and closes
RISK-0007 (`docs/risks.md`) if it goes well; running it is the one remaining step, and it needs real
human participants, so it cannot be executed by an agent. This document is the protocol; the actual
recruiting, scheduling, and running of sessions is `coderturtle`'s to do (or to delegate to another
human), not something to hand to a coding agent.

## What this tests

`docs/workshop-design.md`'s central bet: "the harness is the classroom," i.e. that doing a module's
exercise inside a real coding-agent harness teaches the module's concept better than reading a
well-structured written guide covering the same material would. Everything the project has done
before this (module dry runs, review panels, a rubric-gaming check, a blind judging panel, Codex and
devstral fresh-agent spikes) tested whether the exercise *mechanism* works. None of it involved a
human learner or a comparison arm. This is the first thing in the project that actually tests the
claim itself.

## Design

Randomized, between-subjects, two arms, one module (04, loop engineering):

- **Arm A (harness):** the participant does Module 04's core exercise (`modules/04-loop-
  engineering/README.md`) the normal way, driving their own coding-agent harness, Coachgremlin's
  rubric framing it up front.
- **Arm B (written guide):** the participant reads `docs/pedagogy-trial/written-guide.md` instead,
  covering the identical concept (loop engineering, stop conditions, external verification, the
  stable-goal-vs-moving-target rule) and a fully worked version of the same ticket, as prose.

Both arms then take the same **transfer task** (`docs/pedagogy-trial/transfer-task.md`): a new
ticket, on a fixture neither arm has seen (`fixtures/receipts/variants/pedagogy-trial-transfer/`,
a different bug shape from Module 04's own timezone bug), followed by a structured explain-back
interview. A blind grader scores both arms' transfer-task packages against one rubric
(`docs/pedagogy-trial/grading-rubric.md`) without knowing which arm produced which package.

Why the transfer task is what gets scored, not the learning experience itself: scoring Arm A's
actual Module 04 attempt against Arm B's guide-reading would not be a fair comparison (different
artifacts, different grading criteria). Both arms doing the identical, novel transfer task is what
makes the comparison meaningful, and it also tests the thing that actually matters: not "did you
produce the artifact this one time," but "did the discipline transfer to a ticket you have not seen
before."

## Recruitment

Target: 4-6 participants matching this workshop's stated audience (`docs/workshop-design.md`:
comfortable with git, CLI tools, and reading diffs; regular users of at least one coding
agent/harness already). This is a pilot, not a powered study; n=4-6 can show a real, honest
directional signal and nothing more. Do not oversell it as more than that in any write-up (per
`docs/brand.md`'s hypothesis rule).

Sourcing:
- The `attempt-report.yml` issue template (`.github/ISSUE_TEMPLATE/attempt-report.yml`) has a
  trial-volunteer opt-in checkbox specifically feeding this. Check for volunteers there first.
- Failing that, direct outreach to practitioners known to already use coding agents daily (the
  workshop's own stated audience), outside anyone who has seen this repo's design docs, module
  content, or prior runs.
- Do not recruit from anyone who has read `docs/workshop-design.md`, `modules/04-loop-engineering/
  README.md`, `runs/2026-07-03-module-04-dry-run/`, or this trial's own documents before their
  session. Ask directly before scheduling; a participant who has already seen the reference solution
  or the guide's worked example cannot give a clean result in either arm.

## Randomization

Before recruiting, generate a fixed assignment sequence (for example, flip a real coin per
participant, or use a pre-generated random bit sequence, not an on-the-spot judgment call once you
know who the participant is). Assign participants to arms in signup order against this
pre-generated sequence, not by hand-picking who seems like a better fit for which arm. Record the
sequence before the first session runs, so it cannot be adjusted after seeing early results.

## Session logistics

Roughly 90 minutes per participant, one participant at a time:

1. **Learning phase (~30-40 min).** Arm A: the participant does Module 04's core exercise. Arm B:
   the participant reads `written-guide.md` at their own pace. Facilitator does not intervene except
   to answer logistics questions (how to access the fixture), not concept questions.
2. **Transfer task (~45 min, timeboxed).** Both arms get the identical task, per
   `docs/pedagogy-trial/transfer-task.md`.
3. **Explain-back interview (~10-15 min).** Immediately after, same session, per the six questions
   in `transfer-task.md`.

Run participants one at a time, not in parallel, so an early participant's questions or reactions
don't leak into how later sessions are facilitated.

## Consent and privacy

This repo is public (`privacy_boundary: public` in `.hekton/project.yaml`); treat participant data
accordingly:

- Before the session, tell the participant plainly: what is being tested (a comparison between two
  ways of learning one module, not an evaluation of them personally), what gets recorded (their
  diff, test output, and their explain-back answers, not a video or audio recording unless they
  separately agree to that), and that results may be referenced in this public repo's docs in
  aggregate or anonymized form, never tied to their name without separate explicit permission.
- Get explicit agreement before the session starts. A verbal "yes, that's fine, go ahead" recorded
  in the session notes is sufficient for a pilot at this scale; a formal written consent form is not
  required but is fine to use if it makes anyone more comfortable.
- Store participant packages (diffs, transcripts, explain-back answers) without names attached once
  scoring is complete; the random ID assigned during blinding (`grading-rubric.md`) can double as
  the retained identifier.

## Analysis plan

With an expected n of 4-6, this pilot can only produce a descriptive, directional read, not a
statistically powered result. Report:

- Each participant's scores from `grading-rubric.md`, arm still blinded, then unblinded once all
  scoring is complete.
- Whether one arm's scores visibly cluster higher or lower than the other's, stated as an
  observation ("in this pilot, arm X's participants scored higher on criteria Y and Z"), not as a
  proven effect.
- Anything qualitative from the explain-back interviews that doesn't reduce to a number: a
  participant who scored well but described real confusion, or one whose scores were low but showed
  they had actually understood the core idea and misapplied it for an unrelated reason.
- An explicit statement of what this pilot cannot tell you: whether the effect (if any) would hold
  at a larger n, whether it holds for a different module, and whether it holds for a different
  fixture where the taught disciplines are more load-bearing (see RISK-0007's aggregated fixture-
  adequacy finding in the critical review, Finding 3: this fixture family is smaller and more
  self-documenting than a production codebase, which may cap how much of an effect either arm can
  show).

Write the result up honestly whichever way it comes out, including a null or mixed result, per this
workshop's own hedging rule (`docs/brand.md`): "we ran a small pilot and did not see a clear
difference" is a valid, useful finding, not a failure to report quietly.

## Documents in this trial

- `written-guide.md`: the Arm B learning material.
- `transfer-task.md`: the shared post-learning task and explain-back interview, given to both arms.
- `grading-rubric.md`: the blind-grading criteria and scoring procedure.
- `fixtures/receipts/variants/pedagogy-trial-transfer/`: the transfer task's fixture, authored and
  verified 2026-07-11 (seeded bug reproduces in isolation; a minimal fix passes all tests; ships
  unsolved).

## Status

Designed and verified (fixture reproduces and is fixable; guide content, task, and rubric written)
2026-07-11. Not yet run. Running this is a human-only next step: recruit participants, per the plan
above, and run the sessions. See `docs/next-actions.md` for how this fits the rest of the backlog.
