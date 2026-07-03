"""Command-line entry point: summarize an expense-receipt CSV by month."""

from __future__ import annotations

import argparse
import csv
import sys

from receipts.grouping import group_expenses_by_category, group_expenses_by_month


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="receipts",
        description="Summarize expense receipts by month.",
    )
    parser.add_argument("csv_path", help="path to a receipts CSV file")
    parser.add_argument(
        "--tz",
        default="UTC",
        help="IANA timezone the month grouping is computed in (default: UTC)",
    )
    parser.add_argument(
        "--by-category",
        action="store_true",
        help="group receipts by category instead of by calendar month",
    )
    args = parser.parse_args(argv)

    with open(args.csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if args.by_category:
        result = group_expenses_by_category(rows)
    else:
        result = group_expenses_by_month(rows, tz=args.tz)

    for key in sorted(result.months):
        summary = result.months[key]
        print(f"{key}: {summary.count} receipt(s), total ${summary.total:.2f}")

    if result.errors:
        print(f"\n{len(result.errors)} row(s) skipped:", file=sys.stderr)
        for err in result.errors:
            print(f"  {err.reason}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
