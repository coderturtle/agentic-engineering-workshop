# Transfer task (both arms)

Given to every participant after their arm's learning experience, whether that was driving a
harness through Module 04's core exercise or reading `docs/pedagogy-trial/written-guide.md`. Same
task, same instructions, same fixture, regardless of arm. This is what gets scored; the learning
experience itself is not scored, only what the participant does with it here.

## Setup (facilitator)

1. Give the participant a fresh, unsolved copy of the transfer fixture. Never point them at the
   copy in this repo directly; stage a scratch copy so a re-run with a different participant starts
   clean:
   ```
   SCRATCH=$(mktemp -d)
   cp -r fixtures/receipts/variants/pedagogy-trial-transfer/* "$SCRATCH/"
   ```
2. Tell the participant: "You may use whatever tools you'd normally use for this, including your own
   coding agent. Nobody is testing which tool you pick; we're testing how you use it." This keeps
   the comparison about the taught discipline, not about who did or didn't have tool access. Both
   arms get to use an agent here if they want one.
3. Do not mention Module 04, the written guide, or which arm the participant was in. Do not answer
   questions about what the "right" concepts are until after the explain-back interview.

## The task, as given to the participant

You've been handed a ticket:

> `receipts --by-week` reports totals that grow across separate runs in the same process (for
> example, a batch job that calls this once per uploaded file). One test is failing.
> `SPEC.md` in this directory has the full function contract if you want it, but you do not need to
> read it to do this task; the failing test already tells you what's wrong.

Before you start work:

1. **Write down, in your own words, both terminal states for this ticket** (what "done" looks like,
   and what "give up and call it unreproducible" looks like), before you run anything. Save this to
   a file or say it out loud to the facilitator, timestamped before you begin.
2. Then do the work: reproduce the failure, find the cause, apply the smallest fix, and rerun the
   suite until a terminal state fires.
3. Stop when a terminal state fires. Show the facilitator the terminal state firing (the test run
   that confirms it), not just a diff.

There is a 45-minute time box. If you have not reached a terminal state by then, stop anyway; where
you stopped is itself useful information for this study, not a failure to be embarrassed about.

## What gets collected

- The stated terminal states (verbatim, from before work started).
- The final diff (`git diff` or equivalent against the scratch copy's starting state).
- The test output showing the terminal state firing (or, if the 45 minutes ran out first, the state
  of the suite at that point).
- Elapsed time to terminal state (or to the 45-minute cutoff).

## Explain-back interview (immediately after, same session)

Ask these in order, in conversation, not as a written quiz. Write down the participant's answers in
their own words; do not paraphrase them toward the "correct" answer while transcribing.

1. "Walk me through what you did, in order." (Tests whether they can narrate reproduce, root-cause,
   fix, rerun as a sequence, not just that they arrived at a diff.)
2. "Why did you write your terminal states down before starting, instead of after?" (Tests whether
   they understand the failure mode this guards against, not just that they followed an
   instruction.)
3. "How do you know your fix is correct, beyond 'the tests passed'?" (Tests whether they understand
   that the test suite itself has to stay honest, i.e. they didn't change what the test was
   checking to make it agree with the code.)
4. "If I told you the test suite itself had a bug in it, would that change how you'd have approached
   this? How would you have caught that?" (Tests understanding of external verification's own
   limits, not rote trust in "the tests are always right.")
5. "Was there a point where you considered a bigger fix than what you ended up submitting? What made
   you not do that?" (Tests the smallest-fix discipline as a decision they made, not an accident of
   what they happened to try first.)
6. "How would you decide whether a *different* task deserves this kind of loop at all, versus just
   doing it by hand?" (Tests the stable-goal-vs-moving-target rule, applied to a task they were not
   given in advance.)

Do not reveal the "right" answers or the study's hypothesis until after this interview is fully
recorded.

## Handing off to grading

Package per participant: stated terminal states, final diff, test output, elapsed time, and the six
explain-back answers verbatim. Strip anything that identifies which arm the participant was in
(harness or guide) before handing this to the grader; see `docs/pedagogy-trial/grading-rubric.md`
for the blind-grading procedure this feeds into.
