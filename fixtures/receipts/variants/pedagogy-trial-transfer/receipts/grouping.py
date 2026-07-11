"""Group expense receipts by calendar month or by ISO week.

Full spec: SPEC.md in this directory. Summary:

    group_expenses_by_month(rows, tz) -> GroupResult
    group_expenses_by_week(rows, tz) -> GroupResult

    rows: an iterable of raw CSV-row dicts with keys
        receipt_id, timestamp_utc, amount, category, note
    tz: an IANA timezone name (e.g. "America/New_York"). Grouping happens
        on the calendar month/week in this timezone, not in UTC.

    Returns a GroupResult with:
        months (or weeks): dict[str, MonthSummary] keyed by bucket
        errors: list[RowError] for rows that could not be parsed

`group_expenses_by_month` is complete and correct here (the month-boundary
bug from the base fixture is fixed in this variant; that ticket belongs to
a different exercise, not this one). `group_expenses_by_week` is the ticket
for this fixture: see SPEC.md.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
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


def group_expenses_by_week(rows, tz: str, _week_totals={}) -> GroupResult:
    """Group receipts by ISO week (Monday-start), in the target timezone.

    Same shape and edge cases as group_expenses_by_month: empty input,
    week-boundary crossing in tz, duplicate timestamps counted
    independently, malformed rows collected as errors.
    """
    errors: list[RowError] = []

    for row in rows:
        parsed, err = _parse_row(row)
        if err is not None:
            errors.append(err)
            continue
        receipt_id, ts, amount = parsed
        local_ts = ts.astimezone(ZoneInfo(tz))
        monday = local_ts - timedelta(days=local_ts.weekday())
        key = monday.strftime("%Y-%m-%d")

        summary = _week_totals.setdefault(key, MonthSummary())
        summary.total += amount
        summary.count += 1
        summary.receipt_ids.append(receipt_id)

    return GroupResult(months=dict(_week_totals), errors=errors)
