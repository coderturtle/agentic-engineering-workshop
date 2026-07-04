# Module 03 manifest pilot: first real dry run

This is the first real harness run against Module 03's agent-native manifest pilot
(`modules/03-harness-engineering/module.yaml` + `AGENT.md` + `coachgremlin/grader.md`), which
`modules/03-harness-engineering/README.md`'s status line said was "schema-valid and drift-checked
... but not yet dry-run verified." This run is that verification.

**Honesty note per `AGENT.md`/`coachgremlin/grader.md`'s own instruction:** this is my agent (the
orchestrating session) running the grader persona locally and orchestrating a bounded sub-agent.
Nothing here is "the workshop grading me" — it's a self-assessment against `module.yaml`'s rubric,
recorded in `runs/` for a human to review.

## Starting state found on disk (before this run)

This worktree had a prior, partial attempt already on disk when this run began:

- `fixtures/receipts/receipts/grouping.py` modified: `group_expenses_by_category` implemented.
- `fixtures/receipts/.receipts-category-progress.md` (untracked): a progress-notes file claiming
  Phase 1 (the function) was done, Phase 2 (CLI wiring) deliberately deferred, and giving the exact
  verify command and its expected output.
- `modules/03-harness-engineering/AGENT.md`, `module.yaml`, and `coachgremlin/grader.md` referenced
  by this task did **not** exist in this worktree's checkout (this worktree branched before the
  commit that added them upstream, on `agent/claude/workshop-design-docs`). They were brought in
  verbatim (`git show agent/claude/workshop-design-docs:<path>`, same object database, no content
  invented) so the manifest pilot could actually be exercised. `runs/.schema.yaml` was extended the
  same way, adding the `exercise` task type and the `module_id` / `attempt_driver` / `rubric_scores`
  / `coachgremlin_assessment` fields it needed.

**The notes file's claims were independently re-verified, not trusted:** ran
`PYTHONPATH=. python3 -m unittest tests.test_by_category -v` from `fixtures/receipts` before doing
anything else. Result matched the notes exactly: the function test passed, the CLI test errored with
`unrecognized arguments: --by-category` (the flag not yet wired). `git status --porcelain` also
confirmed nothing outside `fixtures/receipts/receipts/grouping.py` plus the untracked notes file had
been touched — Phase 1's own bounded-reach claim held up too.

A snapshot of this exact stopping point was saved to `checkpoints/phase1-stop/` for later diffing.

## Method

Used the reference sub-agent, `.claude/agents/receipts-category-summary.md` (already defined in
this repo, scope: `receipts/` plus running only `tests/test_by_category.py`), invoked twice as two
genuinely separate agent sessions — not narrated, actual fresh contexts with zero conversation
history from the orchestrating session or from each other.

- **Phase 2, real run (notes file present).** Spawned a fresh `receipts-category-summary` sub-agent
  with a minimal prompt: check for on-disk progress state, re-verify its claims yourself, then get
  both tests passing without leaving `receipts/` (except the notes file) or breaking default CLI
  behavior. No implementation detail was given away. The sub-agent read the notes file, re-ran the
  verify command itself, then wired `--by-category` into `receipts/cli.py` (import, flag, branch,
  a `month` → `key` loop-variable rename with the print format unchanged), updated the progress file,
  and reported both tests passing.
- **Independent re-verification (orchestrator, not the sub-agent's own claim):** reran the test
  command myself — `OK`, both tests pass. Confirmed the CLI's default (no-flag) output is byte-for-
  byte the same shape as before (`2026-01: 2 receipt(s), total $52.50` etc.). Confirmed via
  `git status --porcelain` (whole worktree, not just the fixture) that only `receipts/cli.py`,
  `receipts/grouping.py`, and the notes file changed inside `fixtures/receipts/` — nothing in
  `tests/`, `SPEC.md`, `data/`, or `variants/`.
- Saved this result to `checkpoints/phase2-with-notes/`.

## Negative control: does Phase 2 actually need the notes file?

Per `AGENT.md`'s explicit instruction not to skip this because the first pass succeeded: reverted
the working fixture to the exact Phase 1 stopping point (`checkpoints/phase1-stop/cli.py` restored,
`grouping.py` already identical, notes file moved aside so it genuinely does not exist on disk),
independently re-confirmed via diff and a rerun of the test command that this reproduced the original
failure exactly.

Then ran a **third, independent fresh sub-agent session**, same sub-agent definition, same prompt
verbatim (the prompt never claimed a notes file would or wouldn't exist — it just said "check
whether it exists"), so the only difference from the real Phase 2 run was that the file genuinely
wasn't there to find.

**Result: it also succeeded.** The sub-agent reported finding no notes file, read `grouping.py` and
confirmed it already correct, read `cli.py` and confirmed the flag was missing, and wired it the same
way. `PYTHONPATH=. python3 -m unittest tests.test_by_category -v` → `OK`, both tests pass, independently
re-run by the orchestrator. Default CLI behavior unchanged. The resulting `cli.py` differs from the
real Phase 2 run's `cli.py` in exactly one line: the `--by-category` flag's `help=` text wording
("group by the row's category field instead of by month" vs. "group by receipt category instead of
by calendar month") — a cosmetic difference with no behavioral effect. Saved to
`checkpoints/negative-control-without-notes/`.

**Honest interpretation, matching the original 2026-07-03 reference dry run's finding
(`runs/2026-07-03-module-03-dry-run/README.md`):** the notes file was not load-bearing for this
specific task. The remaining work (wire one CLI flag, given an already-passing function and a
failing test that names exactly what's missing) is fully reconstructable from the code and the test
alone. This does not mean persistent state is useless in general — it means this particular task's
state happens to be fully recoverable without it. A task with a real dead end, a rejected approach,
or a partial external operation from Phase 1 would need the notes file in a way this one didn't.

## Final on-disk state

Restored the real Phase 2 (with-notes) result as the canonical fixture state, since that's the
actual designed flow (persistent state present, as the sub-agent's own definition requires), not the
negative-control side experiment. Final verify, from `fixtures/receipts`:

    PYTHONPATH=. python3 -m unittest tests.test_by_category -v
    test_cli_by_category_flag_prints_category_totals ... ok
    test_group_expenses_by_category_totals_and_counts ... ok
    Ran 2 tests in 0.000s
    OK

`git status --porcelain` (whole worktree) at the end of this run shows changes confined to:
`fixtures/receipts/receipts/cli.py`, `fixtures/receipts/receipts/grouping.py` (modified),
`fixtures/receipts/.receipts-category-progress.md` (untracked, in-fixture notes file), plus the
manifest infrastructure this run had to add to make the pilot runnable at all
(`coachgremlin/grader.md`, `modules/.manifest.schema.yaml`,
`modules/03-harness-engineering/{AGENT.md,module.yaml}`, `runs/.schema.yaml`'s extension, and this
`runs/2026-07-04-module-03-manifest-dry-run/` directory). Nothing outside `fixtures/receipts/` was
touched by the actual exercise work; the manifest files are required plumbing, not exercise output.

## What this validates, against `module.yaml`'s rubric

See `coachgremlin-assessment.md` in this directory for the full self-assessment. Summary: bounded
reach, sub-agent boundary, persistent-state mechanism, and "actually ran" are all directly
demonstrated and independently re-verified in this run (not just claimed by the sub-agent). Worktree
isolation was not used (a plain checkout was sufficient, as the reference run also found). Reusable
generality: the sub-agent definition is not hard-wired to this fixture's absolute path.
