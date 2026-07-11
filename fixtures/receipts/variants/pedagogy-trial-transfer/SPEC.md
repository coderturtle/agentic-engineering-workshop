# Spec: `group_expenses_by_week`

Ticket for this fixture variant, `pedagogy-trial-transfer`. Not part of the workshop's own module
arc — used only as the shared **transfer task** in `docs/pedagogy-trial/`, the trial testing
whether harness-driven exercise teaches loop-engineering discipline better than a written guide
(see `docs/pedagogy-trial/README.md`). Deliberately new: neither trial arm has seen this bug
before, so solving it measures whether the taught skill (verification loop discipline, stated stop
conditions, minimal fixes) transfers, not whether either arm memorized the base fixture's own
already-solved timezone bug.

## Signature

```python
def group_expenses_by_week(rows: list[dict], tz: str) -> GroupResult
```

Same row shape and `GroupResult` shape as `group_expenses_by_month` (see the base fixture's
`SPEC.md`), grouped by ISO week (Monday-start) instead of calendar month, keyed `"YYYY-MM-DD"` (the
Monday of that week, in `tz`).

## Required edge cases

1. Empty input returns no weeks and no errors.
2. Week-boundary crossing: a receipt whose UTC timestamp falls in one ISO week but whose local time
   in `tz` falls in the adjacent week groups into the local week.
3. Duplicate timestamps are independent receipts, never merged.
4. A malformed row is collected into `errors`, excluded from `weeks`, and does not stop the rest of
   the batch from being processed.
5. **Two independent calls to `group_expenses_by_week` must not leak totals into each other.** A
   batch job that calls this function once per uploaded file must see each call's report reflect
   only that call's own rows.

`group_expenses_by_month` in this variant is already correct (that ticket belongs to a different
exercise); only `group_expenses_by_week` is live here.

## The seeded bug

`group_expenses_by_week` accumulates into a dict passed as a default argument value
(`_week_totals={}`), which Python evaluates exactly once, at function-definition time, and reuses
across every call that doesn't pass its own value explicitly — a real, common bug class (a mutable
default argument), not specific to this codebase. Edge cases 1-4 all pass, because each of those
tests only calls the function once. Edge case 5 fails: a second call's report includes totals left
over from the first call, because both calls are silently sharing the same dict.

`tests/test_grouping.py::test_independent_calls_do_not_leak_totals_into_each_other` is the one
failing test that demonstrates it (each test method reloads the module first, in `setUp`, so tests
are isolated from each other regardless of whether the bug is fixed; the two calls *inside* that one
test method are what still shares state).

The fix: change the default to `None`, and create a fresh dict inside the function body when the
caller didn't pass one (`if _week_totals is None: _week_totals = {}`). It does not require touching
parsing, error handling, or `group_expenses_by_month`. A fix that touches either of those has found
a different bug, written a new one, or started negotiating with the test file.

## Running it

```bash
cd fixtures/receipts/variants/pedagogy-trial-transfer
PYTHONPATH=. python3 -m unittest discover -s tests -v
```

No external dependencies: stdlib only (`unittest`, `zoneinfo`, `datetime`, `collections`,
`dataclasses`).
