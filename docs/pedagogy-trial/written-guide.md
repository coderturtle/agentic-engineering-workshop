# Module 04, written guide (trial arm B)

You are reading this because you were randomly assigned to the written-guide arm of a small
comparison study. The other arm gets Module 04 the normal way: driving a coding-agent harness
through the exercise, with Coachgremlin grading the attempt. You get the same material, the same
worked example, and the same underlying skill, but as prose instead. After this guide, you will get
a short transfer task and a follow-up conversation. Full study context: `docs/pedagogy-trial/README.md`.

Do not open `modules/04-loop-engineering/README.md`, any file under `runs/`, or this repo's other
docs while working through this guide or the transfer task that follows it. This guide contains
everything you need.

## What loop engineering is

A prompt gets one turn to do the right thing. Context engineering decides what that turn can see.
Neither one asks what happens *after* the first turn, when the task takes more than one attempt to
get right. That is loop engineering's job: deciding when an agent's work stops, how you know it
stopped correctly, and what triggers it to run again.

Four shapes of loop show up in practice, roughly in order of how much is built on top of the base
case:

1. **Agent loop.** The base case: the model calls tools repeatedly until it decides a task is
   complete. Nothing checks that decision.
2. **Verification loop.** An external check is added: the agent's output is graded against a
   rubric or a test suite, and sent back if it fails. The agent's own opinion that it is "done" is
   no longer the thing that ends the loop.
3. **Event-driven loop.** The loop is triggered by something outside the conversation (a webhook, a
   schedule, a git push), not run by hand each time.
4. **Hill-climbing loop.** The frontier case: an outer process analyzes traces from real runs and
   proposes changes to the *inner* loop's own prompt or configuration. This must always be gated by
   a human review and a regression check before a proposed change is adopted; an unreviewed
   self-editing loop is a liability, not a feature.

This guide's worked example and the transfer task after it both live at level 2: a verification
loop. The core move is simple to state and easy to get wrong in practice: **the loop's "done" signal
has to come from something outside the agent's own judgment, and that external check has to stay
honest.** A test suite works because it is a fixed, external question ("do these assertions hold")
that does not bend to match whatever the agent produced. If the agent (or a learner under time
pressure) edits the test to agree with a wrong answer, the loop still reports success, but the
verification was never real. Spotting that gap, in your own work and in someone else's, is most of
what this module is trying to teach.

## Before you build a loop: is it worth it?

Not every task deserves a loop. The rule this workshop uses: a **stable goal** (the definition of
"done" will not change while you are working on it) is worth building a loop for. A **moving
target** (the goal itself is still being worked out, or changes based on what you learn) is better
left a manual, prompt-driven task, at least until it stabilizes. A loop's setup cost (writing the
stop condition, wiring the verification step, deciding what "retry" means) only pays for itself when
the success criteria hold still long enough to use them more than once.

**Quick check before you continue:** is "does this specific test suite pass" a stable goal or a
moving target? (It is stable: the test suite's assertions are fixed before the loop runs and do not
change based on what the agent tries. That is exactly why a test suite makes a good verification
signal and a vague goal like "make the code better" does not.)

## Worked example: the Ticket-to-PR-Ready loop

Here is the ticket this guide's example is built from, taken directly from the shared `receipts`
fixture (`fixtures/receipts/`, full spec in `fixtures/receipts/SPEC.md`):

> `receipts --tz America/New_York` reports totals that look wrong near a month boundary.
> `tests/test_grouping.py::test_month_boundary_crosses_in_target_timezone` is failing; every other
> test in the suite passes.

The loop shape for a ticket like this has four steps, repeated until a terminal state fires:
**reproduce, root-cause, smallest fix, rerun.** Before running anything, both terminal states get
written down:

- **Success:** the full test suite passes, including the one named test.
- **Failure:** after two genuine attempts to reproduce or root-cause the bug, it still cannot be
  pinned down. This is a valid stop, not a failed exercise: it means the loop correctly recognized
  it was not converging, instead of thrashing indefinitely.

Writing the terminal states first matters because it is the only thing standing between "the loop
stops when it's actually done" and "the loop stops when someone gets bored watching it, or when a
plausible-looking diff shows up." Deciding what counts as done, after you have already seen an
attempt at a fix, is much easier to get wrong. You already want that attempt to have worked.

### Step 1: reproduce

Run the suite as-is and confirm the failure is real and specific:

```
$ PYTHONPATH=. python3 -m unittest discover -s tests -v
test_basic_grouping_totals_and_counts ... ok
test_duplicate_timestamps_are_not_deduplicated ... ok
test_malformed_row_is_collected_as_error_not_raised ... ok
test_month_boundary_crosses_in_target_timezone ... FAIL
```

One test fails, the rest pass. That is the shape a real, isolated bug takes: not "everything is
broken," one specific thing is wrong and the rest of the system already works.

### Step 2: root-cause

Reading `receipts/grouping.py`, the month key is computed as:

```python
key = ts.strftime("%Y-%m")
```

`ts` here is the receipt's timestamp parsed from UTC and never converted to the caller's `tz`
argument. A receipt logged at `2026-02-01T02:00:00Z` (2am UTC on February 1st) is actually
`2026-01-31T21:00:00` in `America/New_York` (UTC-5 in February): 9pm on January 31st, local time.
The function keys it `"2026-02"` because it never looked at anything but the UTC clock. The ticket's
own wording ("wrong near a month boundary") is the diagnosis, once you notice the code never touches
`tz` when computing the key at all.

### Step 3: smallest fix

The fix converts the timestamp to the target timezone before formatting the key, and touches nothing
else:

```python
from zoneinfo import ZoneInfo

# before
key = ts.strftime("%Y-%m")

# after
local_ts = ts.astimezone(ZoneInfo(tz))
key = local_ts.strftime("%Y-%m")
```

Notice what this fix does *not* touch: row parsing, error handling, the CLI, or the test file. A
"fix" that also refactors `_parse_row` or renames a field is no longer the smallest fix for this
ticket, whatever else it might improve. Keeping the diff bounded to what the bug actually requires
is what makes a fix reviewable and what makes "this is the fix for this ticket" a claim someone else
can check in thirty seconds instead of re-reading the whole file.

### Step 4: rerun, and let the terminal state actually fire

```
$ PYTHONPATH=. python3 -m unittest discover -s tests -v
test_basic_grouping_totals_and_counts ... ok
test_duplicate_timestamps_are_not_deduplicated ... ok
test_malformed_row_is_collected_as_error_not_raised ... ok
test_month_boundary_crosses_in_target_timezone ... ok

OK
```

All tests pass, including the one named in the success condition written down before any of this
started. The loop stops here, in the state it said it would stop in. That last part matters more
than it sounds: a loop that keeps going after its own stated success condition is met (one more
"let me also clean this up" pass) is not following the terminal state it declared, it is drifting
past it.

### The shortcut this loop must not take

There is a faster way to make the suite pass: open `tests/test_grouping.py` and edit the failing
assertion until it agrees with the buggy output, instead of fixing `grouping.py`. Nothing in a shell
stops this. The suite goes green either way. The difference is entirely in what the diff touches: a
fix confined to `grouping.py` changed the code to match reality; an edit to the test file changed
reality's description to match the (still wrong) code. The bug is still there afterward regardless
of what the terminal printed. This is why "the suite passed" is not, by itself, verification: you
also have to check that the suite itself was not the thing that got changed to make that happen.
Reading the diff's target files, not just its exit code, is what catches this.

## Check your understanding

Before moving on to the transfer task, answer these for yourself (nobody is grading this part, but
skipping it will make the transfer task harder):

1. In the worked example above, which specific line in the "smallest fix" would you flag as *out of
   scope* if a fix had also included it: for example, a change to how `_parse_row` handles malformed
   amounts? Why would that be a different bug, not part of this one?
2. Suppose a second ticket said: "make the CLI's output formatting look nicer." Is that a stable
   goal or a moving target, by this guide's own rule? What would make you change your answer?
3. If you were writing the two terminal states for a *different* ticket before starting work on it,
   what is one concrete signal (not "it looks right") you would use for success, and one for when to
   give up and call it unreproducible?

## What is next

You will get a short transfer task: a new ticket, on a fixture you have not seen, with its own
seeded bug. Treat it the same way this guide treated the timezone ticket: state your terminal states
before you start, verify externally, keep the fix minimal. Afterward, a short conversation will ask
you to explain your reasoning in your own words. There is no trick in the transfer task; the bug is
real, it lives in one place, and the discipline this guide just walked through is the whole point,
not incidental to it.
