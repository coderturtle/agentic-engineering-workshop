"""Group expense receipts by calendar month.

Full spec: fixtures/receipts/SPEC.md. Summary:

    group_expenses_by_month(rows, tz) -> GroupResult

    rows: an iterable of raw CSV-row dicts with keys
        receipt_id, timestamp_utc, amount, category, note
    tz: an IANA timezone name (e.g. "America/New_York"). Grouping happens
        on the calendar month in this timezone, not in UTC.

    Returns a GroupResult with:
        months: dict[str, MonthSummary] keyed "YYYY-MM" in `tz`
        errors: list[RowError] for rows that could not be parsed

    Required edge cases:
        1. empty input -> months == {}, errors == []
        2. a receipt whose UTC timestamp crosses a month boundary once
           converted to `tz` groups into the local month, not the UTC one
        3. duplicate timestamps are independent receipts, never merged
        4. a malformed row (bad timestamp or non-numeric amount) is
           collected in `errors`, excluded from `months`, and does not
           stop the remaining rows from being processed
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from zoneinfo import ZoneInfo


@dataclass
class RowError:
    row: dict
    reason: str


@dataclass
class MonthSummary:
    total: float = 0.0
    count: int = 0
    receipt_ids: list = field(default_factory=list)


@dataclass
class GroupResult:
    months: dict
    errors: list


def _parse_row(row: dict):
    receipt_id = row.get("receipt_id", "")
    ts_raw = row.get("timestamp_utc", "")
    amount_raw = row.get("amount", "")

    try:
        ts = datetime.fromisoformat(str(ts_raw).replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None, RowError(row=row, reason=f"unparseable timestamp: {ts_raw!r}")

    try:
        amount = float(amount_raw)
    except (ValueError, TypeError):
        return None, RowError(row=row, reason=f"unparseable amount: {amount_raw!r}")

    return (receipt_id, ts, amount), None


def group_expenses_by_month(rows, tz: str) -> GroupResult:
    months: dict[str, MonthSummary] = defaultdict(MonthSummary)
    errors: list[RowError] = []

    for row in rows:
        parsed, err = _parse_row(row)
        if err is not None:
            errors.append(err)
            continue
        receipt_id, ts, amount = parsed
        local_ts = ts.astimezone(ZoneInfo(tz))
        key = local_ts.strftime("%Y-%m")

        summary = months[key]
        summary.total += amount
        summary.count += 1
        summary.receipt_ids.append(receipt_id)

    return GroupResult(months=dict(months), errors=errors)
