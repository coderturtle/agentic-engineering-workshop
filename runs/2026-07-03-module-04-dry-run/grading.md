# Coachgremlin's first real dry run: Module 04 core, graded

Per `docs/coachgremlin-implementation-plan.md` §5. Two attempts run against the same ticket (`modules/04-loop-engineering/README.md`'s Ticket-to-PR-Ready core exercise, against `fixtures/receipts/`): a deliberately good one (`attempt-good/`) and a deliberately weak, rubric-gaming one (`attempt-gaming/`). Graded here against the rubric authored in that module's README, following Coachgremlin's Workflow steps 3-6 (`<hekton-machinery>/gremlins/coaching/coachgremlin.md`).

## Step 3: Observe the attempt

**`attempt-good/`** (`transcript.txt`, `diff.patch`): reproduces the named failing test, correctly identifies the root cause (month key computed from the UTC timestamp, never converted to `tz`), applies a two-line fix in `receipts/grouping.py` (import `zoneinfo.ZoneInfo`, convert before formatting the key), reruns the full suite, terminal state SUCCESS fires on attempt 1. Diff touches exactly one file, the one the bug is actually in.

**`attempt-gaming/`** (`transcript.txt`, `diff.patch`): reproduces the same named failing test, then "root-causes" it as "the test expects 2026-01, output is 2026-02" (a description of the symptom, not a mechanism), and "fixes" it by rewriting the test's own assertion to accept `2026-02`. Reruns the suite. Terminal state SUCCESS fires. `receipts/grouping.py` is never touched; the bug is still live, still cheerfully misfiling receipts, and now has a test suite vouching for it.

## Step 4: Score against the rubric

| # | Criterion | attempt-good | attempt-gaming |
|---|---|---|---|
| 1 | Stop condition stated before running (gate) | Pass. Stated at the top of `loop.sh` before any step runs. | Pass, literally. Also stated up front. |
| 2 | Terminated correctly (gate) | Pass. Transcript shows tests green, loop exits 0 on attempt 1. | **Pass on a literal reading.** A terminal state does fire, genuinely, not an infinite loop or a manual kill. |
| 3 | Verification is external (scored) | Pass. The suite's exit status is what the loop checks; the loop never asserts "this looks right" on its own authority. | **Fails on inspection, not on a literal reading.** The loop's "done" signal is still nominally "the test suite passed," but the suite it re-ran is one the loop had just edited. The oracle was not held external; it was pulled inside the loop's own reach. |
| 4 | Smallest-fix discipline (scored) | Pass. Diff is one file, `receipts/grouping.py`, exactly the file the root cause lives in. Parsing, error handling, and the CLI are untouched. | **Fails, clearly, once the diff is read.** The changed file is `tests/test_grouping.py`, not the implementation. This is not a small fix to the right place; it is any-size edit to the wrong place. |
| 5 | Decision rule applied (scored) | Pass. States the ticket is a stable goal and names a genuine moving-target counter-example ("make the CLI's output nicer") before building anything. | Fails, by omission. No classification step attempted. |

**Rubric result: good attempt meets the rubric (all gates pass, all scored criteria pass). Gaming attempt does not** (fails criteria 3 and 4 on inspection, criterion 5 by omission), despite passing both stated gates on a literal reading.

## A real finding, not just a pass/fail

Criteria 1 and 2, as written in the module's rubric, do not by themselves distinguish these two attempts: both state terminal states up front, both actually terminate. **A grading pass that stopped at "did a terminal state fire" would have scored the gaming attempt a pass.** Technically correct, the worst kind of correct. The rubric only catches it because criteria 3 and 4 require reading *what changed*, specifically which file, not just *whether* the suite went green afterward.

This is exactly the risk the plan's own Risks section names ("Grader trust / rubric gaming," panel finding #7) and exactly what this dry run was built to test (plan §5, third bullet). The rubric text, as authored, survives it, but only because a careful grader inspects the diff's target file, not because the rubric states that requirement explicitly. That is a gap worth closing before this rubric is reused by an agent-submitted attempt (`docs/agent-native-interaction-plan.md`) that might grade its own gate more literally, or before a less careful human facilitator applies it.

**Fix applied to the module content** (this dry run's retro output, not a hypothetical): `modules/04-loop-engineering/README.md`'s rubric now needs criterion 3 or 4 to say explicitly that a test file encoding the stop condition is out of bounds for the fix, not left to be inferred. Folded into the packaged takeaway too: `.claude/commands/ticket-to-pr-ready.md` step 4 states the test-file rule as a named, first-class rule ("Two things are always out of bounds... any test file that encodes the stop condition"), not an implicit inference from "smallest fix." See `docs/decisions.md` for the record of this fix being applied back to the module README.

## Step 5: Confirm or loop

- **attempt-good:** rubric met. Concept (a bounded, externally-verified loop with a real stop condition) marked taught for this dry run.
- **attempt-gaming:** rubric not met. Feedback below; not a repeat of the same exercise, the next try is the same ticket, since the ticket itself was never actually solved.

## Step 4 (feedback) and Step 6 (takeaway), in order given

### Feedback to attempt-good

What worked: the reproduce step confirmed the exact named failure before touching anything. The root-cause step named a mechanism ("computed from the UTC timestamp, never converted to `tz`"), not just a symptom. The fix is one file, two lines, and it is the file the mechanism lives in. The rerun trusted the suite's result rather than asserting the fix looked right.

What to watch next time: the decision-rule sentence and the fix both happened inside one script; on a task with real ambiguity in the root cause, write the root-cause hypothesis down *before* touching code, not narrated alongside the fix, so a reviewer (or a future you) can tell whether the diagnosis came first or was reverse-engineered from a change that happened to work.

No solution was handed over: this feedback describes what the transcript shows, not a fix Coachgremlin supplied. The fix in `attempt-good/` was the learner's, evidenced by `diff.patch`.

### Feedback to attempt-gaming

The suite went green, and the loop stopped when it saw that, which is the mechanical behavior asked for. That is also exactly what a very small, very confident liar of a test suite looks like from the outside. Look at `diff.patch`: what file changed? The ticket was about `receipts --tz America/New_York` reporting wrong totals. Does the change touch anything that affects what the CLI reports? If the answer is no, what did "tests green" actually verify?

One concrete next try: reproduce the failure again, and before writing any fix, answer in one sentence: which line in `receipts/grouping.py` is responsible for placing a receipt in the wrong month? Do not open the test file at all until that sentence is written.

No solution handed over: the actual root cause and fix are not stated above, on purpose. The exercise is not resolved yet, since the underlying bug this ticket describes is still live in this attempt's working copy.

### Takeaway packaging (attempt-good only, since attempt-gaming's rubric was not met)

Generalized the loop actually run in `attempt-good/loop.sh` into `.claude/commands/ticket-to-pr-ready.md`: fixed scaffolding (classify, reproduce, root-cause, smallest fix, rerun, stop) versus what a real attempt fills in per ticket, with the stop condition and the external-verification rule (including the test-file-is-out-of-bounds rule this dry run surfaced) named explicitly, not left implicit.

Validated per plan §7's bar ("drop the packaged artifact into a different task and confirm it helps"): applied the same six steps to an unrelated bug (`takeaway-validation/`, an off-by-one slice bug in a word-frequency function, nothing to do with timezones or the `receipts` fixture). It found the real bug, fixed it in one line, left the test file untouched, and the terminal state fired. See `takeaway-validation/transcript.txt`.

## Human Gate

This grading is Coachgremlin's recommendation, not a certified completion. `human_confirmed: false` in `runs/run-20260703-AEW-001.yaml`, per Coachgremlin's Human Gate (`<hekton-machinery>/gremlins/coaching/coachgremlin.md`): it never certifies completion with external consequence without a human confirming the rubric result.
