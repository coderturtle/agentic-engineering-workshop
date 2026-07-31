# Retro: Coachgremlin's first real dry run (Module 04 core)

Go/no-go against `docs/coachgremlin-implementation-plan.md` §5's "what success looks like" checklist, before authoring Modules 01, 02, 03, 05.

## Checklist, checked against evidence

**Coachgremlin can frame 04 core from the module README's gate, takeaway, and Ticket-to-PR-Ready pointer, without inventing an unrelated scenario.**
Yes. The exercise built (`modules/04-loop-engineering/README.md`'s Exercise section) is the module's own stated gate and takeaway, applied to the shared `receipts` fixture the plan specified, not a substitute scenario.

**Given a deliberately good attempt and a deliberately weak/rubric-gaming attempt, the rubric discriminates and Coachgremlin catches the weak one.**
Yes, but not for free. See `grading.md`: two of the five rubric criteria, read literally, would have passed the gaming attempt (it does state terminal states up front, and it does terminate). The rubric only discriminates because criteria 3 and 4 require inspecting *which file* the diff touches, not just whether the suite went green. That gap is now closed directly in the rubric text (criterion 4 names the test file as an explicit hard boundary, not an inference), so a future, more literal grading pass doesn't get to make the same mistake. This is the direct, concrete answer to review-panel finding #7: grader trust was asserted before this run, and is now shown, once, with the gap it exposed fixed in the artifact itself.

**Coachgremlin's feedback references the actual transcript, gives one concrete next try, and never hands the fix over.**
Yes. Both feedback blocks in `grading.md` point at specific transcript/diff evidence (which file changed, what the root-cause step actually said versus what it should have said) rather than a generic answer key. Neither states the real fix; the gaming attempt's feedback asks a question that leads back to `receipts/grouping.py` without naming the mechanism or the line.

**The terminal state is observed firing in the transcript, not asserted.**
Yes, for both attempts, genuinely: `attempt-good/transcript.txt` and `attempt-gaming/transcript.txt` are real command output, not narrated. Building this exposed a real bug in the loop harness itself, a `pipefail` interaction that silently misreported a genuinely reproduced failure as "could not reproduce." A loop-engineering exercise breaking its own loop before it taught anyone else to build one is, at minimum, thematically appropriate. Fixed before either transcript was captured for real. Worth remembering: even a "just check the exit code" verification step needs its own verification, all the way down.

**Step 6 produces a loop template that actually helps on a second, different ticket, not just a file that was written.**
Yes. `.claude/commands/ticket-to-pr-ready.md` was applied, step by step, to an unrelated bug (`takeaway-validation/`, an off-by-one slice in a word-frequency function, nothing to do with timezones). It found the bug, fixed it in one line, left the test file alone, terminal state fired. See `takeaway-validation/transcript.txt`.

**The Human Gate holds: completion is a recommendation with `human_confirmed: false` in a `runs/` entry, not a self-certified "complete."**
Yes. `runs/run-20260703-AEW-001.yaml` records this as `status: done` (the dry run itself finished) with `human_confirmed: false` (the recommendation is not certified). Nothing in this session marks the exercise, the module, or Coachgremlin itself as complete on its own authority.

## Go/no-go

**Go.** All six checks hold, with one real finding along the way (the rubric-gaming gap in criteria 3/4), which is exactly the kind of thing this dry run was built to surface before four more modules got authored on the same rubric-writing pattern. The alternative was finding this gap on module five, in front of an actual learner, which is a strictly worse place to learn it. Proceeding to Module 01 next, per the plan's authoring order (`docs/coachgremlin-implementation-plan.md` §6, step 2).

## Revision fed back

Two artifacts, both real edits made during this run, not just findings written down:

1. `modules/04-loop-engineering/README.md`'s rubric: criterion 4 now names the test-file boundary explicitly as a hard rule, not an inferred one; criterion 3 states that self-modified verification doesn't count as external, whatever the transcript shows.
2. `<hekton-machinery>/gremlins/coaching/coachgremlin.md`: added a line to the Workflow's "observe" and "give feedback" steps, and a Completion Checklist item, generalizing this run's lesson past Module 04 specifically: before trusting a green terminal state on any verification-loop exercise, check which files the diff touches, not just whether the check suite passed. See that file's own session log / decisions for the exact diff (edited in `<hekton-machinery>`, outside this project's repo, per Coachgremlin being a cross-project Gremlin).

## Toward Coachgremlin's Review Trigger

This is run 1 of the 3+ (across 2+ workshops) `coachgremlin.md` names before its contract counts as stable enough for v0. It stays `draft`. Whether this run counts toward that total is coderturtle's call, not self-certified here (Human Gate again): flagged in `runs/run-20260703-AEW-001.yaml`'s `human_notes`.

## What's still open

- Extensions A/B/C for Module 04 (verification-deepened, event-driven, hill-climbing) are intentionally not authored yet; they wait on Module 03's harness per the plan's own sequencing.
- The bloated and sabotaged fixture variants (Modules 02 and 05) are intentionally not built yet; `fixtures/receipts/SPEC.md` notes where they'll land.
- This dry run used one grader (this session, playing Coachgremlin) grading its own two constructed attempts. A stronger future test would have an independent pass grade the same transcripts blind, to check whether the "catch" above depended on already knowing which attempt was supposed to be weak.
