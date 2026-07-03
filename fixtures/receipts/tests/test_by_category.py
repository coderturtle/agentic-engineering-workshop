import io
import unittest
from contextlib import redirect_stdout

from receipts.cli import main
from receipts.grouping import group_expenses_by_category


class GroupExpensesByCategoryTests(unittest.TestCase):
    def test_group_expenses_by_category_totals_and_counts(self):
        rows = [
            {"receipt_id": "r001", "timestamp_utc": "2026-01-15T14:30:00Z",
             "amount": "42.50", "category": "meals", "note": "lunch"},
            {"receipt_id": "r002", "timestamp_utc": "2026-01-20T09:00:00Z",
             "amount": "120.00", "category": "travel", "note": "taxi"},
            {"receipt_id": "r003", "timestamp_utc": "2026-01-22T09:00:00Z",
             "amount": "10.00", "category": "meals", "note": "coffee"},
        ]
        result = group_expenses_by_category(rows)
        self.assertEqual(result.months["meals"].count, 2)
        self.assertAlmostEqual(result.months["meals"].total, 52.50)
        self.assertEqual(result.months["travel"].count, 1)

    def test_cli_by_category_flag_prints_category_totals(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            main(["data/sample_receipts.csv", "--by-category"])
        output = buf.getvalue()
        self.assertIn("meals:", output)


if __name__ == "__main__":
    unittest.main()
