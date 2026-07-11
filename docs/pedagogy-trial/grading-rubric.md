# Blind grading rubric

Applied to each participant's transfer-task package (`docs/pedagogy-trial/transfer-task.md`'s
output: stated terminal states, diff, test output, elapsed time, six explain-back answers), by a
grader who does not know which arm (harness or written guide) that participant was in.

## Blinding procedure

1. Before grading starts, strip anything from each package that could reveal the arm: tool names in
   transcripts (a Claude Code or Codex CLI session log names itself; a written-guide participant's
   package will not have one), file paths containing session or tool identifiers, and any
   facilitator notes about which arm was assigned.
2. Assign each package a random ID (not sequential, not tied to sign-up order) before grading.
3. The grader should ideally not be the same person who ran the sessions or knows the participants
   personally. If only one facilitator is available for a small pilot, that person should grade all
   packages in a single sitting, in randomized order, without looking up which ID maps to which arm
   until every package is scored.
4. Record every score before unblinding. Do not revisit a score after the arm is revealed.

## Artifact criteria (adapted from `modules/04-loop-engineering/README.md`'s rubric)

1. **Stop condition stated before running (gate).** Both terminal states are present in the
   package, dated or timestamped before the diff's own timestamp. Pass or fail; no partial credit,
   since this is a binary fact about ordering, not a matter of degree.
2. **Terminated correctly (gate).** The test output shows a terminal state actually firing (tests
   green, or the participant genuinely stopped after reporting the ticket unreproducible). A
   45-minute timeout with no terminal state reached is recorded honestly as a non-terminating
   attempt, not scored as a pass or a fail; note it and move on.
3. **Verification is external (scored 0-2).** 0: the fix touched `tests/test_grouping.py` to make
   it agree with the bug. 1: the fix did not touch the test file, but the explain-back answers show
   no real understanding of why that matters (question 3 or 4 answered with "the tests passed" and
   nothing further). 2: the fix did not touch the test file, and the explain-back answers show the
   participant understands the test suite itself has to stay honest for a green result to mean
   anything.
4. **Smallest-fix discipline (scored 0-2, hard boundary at 0).** 0: the diff touches anything beyond
   `group_expenses_by_week` (parsing, `group_expenses_by_month`, the test file). 1: the diff is
   confined correctly, but the explain-back answers show the boundary was accidental (question 5
   answered with no real reasoning about why a bigger fix was avoided). 2: confined correctly, and
   the participant can articulate why they stopped where they did.
5. **Decision rule applied (scored 0-2).** Based on explain-back question 6 only, since the transfer
   task itself doesn't include a second ticket to classify. 0: no real answer or a restatement of
   "always use a loop." 1: names the stable-goal-vs-moving-target distinction but can't apply it to
   a concrete hypothetical. 2: applies it correctly to a genuinely new scenario, in their own words.

## Explain-back scoring (0-2 per question, six questions, `docs/pedagogy-trial/transfer-task.md`)

Score each of the six explain-back answers independently on understanding, not eloquence: 0 (no real
grasp, restates the question or gives a non-answer), 1 (partial, gets the shape of the idea but
misses the reasoning behind it), 2 (correct and reasoned in their own words, not recited language
from anything they read or were shown).

## Combining scores

Report each participant's scores as a simple table, artifact criteria 1-5 plus the six explain-back
scores, arm still blinded. Do not compute a single combined number across participants and do not
run a significance test: with an expected n of 4-6, any such number would overstate the precision
this pilot can actually support. Report scores per participant, then unblind and look at whether one
arm's scores cluster differently from the other's. Treat any difference as a directional signal for
whether a larger trial is worth running, not as proof either way; see
`docs/pedagogy-trial/README.md`'s analysis-plan section for how this is meant to be read and reported.
