In `receipts/grouping.py`, implement `group_expenses_by_month(rows, tz)` to satisfy `SPEC.md`. Do not modify any other file, including the test file.

Signature: `group_expenses_by_month(rows: list[dict], tz: str) -> GroupResult`, using the `MonthSummary`, `GroupResult`, `RowError`, and `_parse_row` already defined in that file. Call `_parse_row(row)` for each row; it returns `(parsed_tuple, None)` on success, where `parsed_tuple` is `(receipt_id, ts, amount)`, or `(None, RowError)` on failure.

Group by the calendar month in `tz` (use `zoneinfo.ZoneInfo`), not in UTC. Handle exactly these four cases:

1. Empty `rows` returns `GroupResult(months={}, errors=[])`.
2. A receipt whose UTC timestamp falls in one calendar month but whose local time in `tz` falls in the adjacent month groups into the local month, not the UTC one.
3. Two receipts with an identical timestamp are both counted independently; never merge or deduplicate them.
4. A row `_parse_row` cannot parse is appended to `errors` and excluded from `months`; keep processing the remaining rows.

When you are done, run `PYTHONPATH=. python3 -m unittest discover -s tests -v` from this directory and confirm all 5 tests pass before reporting done.
