# Spec: `group_expenses_by_month`

This is the authoritative spec for `receipts.grouping.group_expenses_by_month`, the function every module in this workshop's arc exercises in some form (Module 01 prompts against it directly; Module 02 buries it in noise; Module 03's harness runs it; Module 04's core exercise fixes the seeded bug in it; Module 05 sabotages the system around it). Keep this file as the single source of truth: don't restate the spec differently inside a module README.

Every codebase has a timezone bug in it somewhere, discovered or not. This one just has the courtesy to ship with a failing test attached.

## Signature

```python
def group_expenses_by_month(rows: list[dict], tz: str) -> GroupResult:
    ...
```

- `rows`: an iterable of raw CSV-row dicts, each with keys `receipt_id`, `timestamp_utc`, `amount`, `category`, `note`. `timestamp_utc` is an ISO 8601 string ending in `Z`.
- `tz`: an IANA timezone name (for example `"America/New_York"`). The grouping boundary is the calendar month **in this timezone**, not in UTC.
- Returns a `GroupResult` with two fields:
  - `months`: `dict[str, MonthSummary]` keyed `"YYYY-MM"` in `tz`. `MonthSummary` has `total` (float), `count` (int), `receipt_ids` (list[str]).
  - `errors`: `list[RowError]` for rows that could not be parsed, each with `row` (the original dict) and `reason` (str).

## Required edge cases

1. **Empty input.** `rows == []` returns `months == {}` and `errors == []`.
2. **Month-boundary crossing.** A receipt whose UTC timestamp falls in one calendar month but whose local time in `tz` falls in the adjacent month must group into the **local** month, not the UTC one. This is the workshop's seeded bug: see below.
3. **Duplicate timestamps.** Two receipts with the identical `timestamp_utc` are independent and both counted; never deduplicated or merged.
4. **Malformed rows.** A row with an unparseable timestamp or a non-numeric amount is collected into `errors` (not raised as an exception) and excluded from `months`. It does not stop the remaining rows in the batch from being processed.

## The seeded bug

`receipts/grouping.py` currently keys each receipt by `ts.strftime("%Y-%m")` on the raw UTC timestamp, never converting to `tz`. This satisfies edge cases 1, 3, and 4, but fails edge case 2: a receipt near a month boundary lands in the wrong bucket whenever `tz` isn't UTC. Whoever wrote this function tested it in UTC and moved on, which is also how most of these bugs get written.

`tests/test_grouping.py::test_month_boundary_crosses_in_target_timezone` is the one failing test that demonstrates it. Everything else in the suite passes against the current code, which is exactly the shape a real bug report takes: one specific thing is wrong, the rest of the system is fine, and the fix does not require rewriting anything you didn't come here to rewrite.

The fix is a conversion to `tz` before formatting the key (Python's `zoneinfo.ZoneInfo` is stdlib and sufficient), applied only where the key is computed. It does not require touching parsing, error handling, or the CLI. If your fix touches any of those, you have found a different bug, written a new one, or given up and started negotiating with the test file. Only the first of those is progress.

## Running it

This file is copied verbatim into every fixture variant (`variants/unimplemented/`, `variants/bloated/`, and so on), so these commands are written to run from **whichever directory contains this copy of `SPEC.md`**, not a hardcoded path. `cd` into that directory first, then:

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -v
```

The CLI demo below needs `data/sample_receipts.csv`, which only the base fixture (`fixtures/receipts/`) ships; most variants exist to exercise `receipts/grouping.py` and its tests directly and don't include sample data. Skip it if `data/` isn't present in the directory you're in:

```bash
PYTHONPATH=. python3 -m receipts.cli data/sample_receipts.csv --tz America/New_York
```

No external dependencies: stdlib only (`unittest`, `zoneinfo`, `argparse`, `csv`).

## Variants (built when the module that needs them is authored)

- **Bloated variant** (Module 02): this same package with noise added (a long README, a CHANGELOG, an unrelated module, stale docs, a red-herring config) to roughly the module's stated budget. Not yet built; build it as part of authoring Module 02, per `docs/coachgremlin-implementation-plan.md` §6 step 3.
- **Sabotaged capstone variants** (Module 05): two to four full agent setups (prompt + context + harness + loop, all provided) whose true bottleneck differs by variant. Not yet built; build as part of authoring Module 05, per plan §6 step 6.
