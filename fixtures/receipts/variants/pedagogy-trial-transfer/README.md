# Fixture variant: pedagogy-trial-transfer

Not part of the workshop's own module arc. Used only as the shared **transfer task** in the
minimum-viable pedagogy trial (`docs/pedagogy-trial/`) testing whether harness-driven exercise
teaches loop-engineering discipline better than a well-structured written guide (RISK-0007).

`group_expenses_by_month` here is already correct. `group_expenses_by_week` is new (added for this
variant only) and carries its own seeded bug: a mutable-default-argument state leak between
independent calls, a genuinely different bug shape from Module 04's timezone bug, so a participant
succeeding here demonstrates the taught process (stated stop condition, external verification,
minimal fix), not memorization of a specific answer. Full ticket: `SPEC.md`.

```bash
cd fixtures/receipts/variants/pedagogy-trial-transfer
PYTHONPATH=. python3 -m unittest discover -s tests -v
```

Verified 2026-07-11: the seeded bug reproduces (exactly one test fails,
`test_independent_calls_do_not_leak_totals_into_each_other`; all other tests pass in the buggy
state, including the empty-input test that a naive first draft of this fixture had briefly and
incorrectly broken via cross-test pollution, fixed by reloading the module in `setUp` rather than
resetting internal state the buggy implementation happens to expose); a minimal fix (`None` default
plus a lazy-created dict) passes all 5/5 tests, touching only `group_expenses_by_week`. This fixture
ships in the unsolved (buggy) state, per this project's standing policy of never shipping a fixture
solved.
