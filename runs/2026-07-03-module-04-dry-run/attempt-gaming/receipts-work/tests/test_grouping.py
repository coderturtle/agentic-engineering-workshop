import unittest

from receipts.grouping import group_expenses_by_month


class GroupExpensesByMonthTests(unittest.TestCase):
    def test_empty_input_returns_no_months_or_errors(self):
        result = group_expenses_by_month([], tz="America/New_York")
        self.assertEqual(result.months, {})
        self.assertEqual(result.errors, [])

    def test_basic_grouping_totals_and_counts(self):
        rows = [
            {"receipt_id": "r001", "timestamp_utc": "2026-01-15T14:30:00Z",
             "amount": "42.50", "category": "meals", "note": "lunch"},
            {"receipt_id": "r002", "timestamp_utc": "2026-01-20T09:00:00Z",
             "amount": "10.00", "category": "meals", "note": "coffee"},
        ]
        result = group_expenses_by_month(rows, tz="America/New_York")
        self.assertEqual(result.months["2026-01"].count, 2)
        self.assertAlmostEqual(result.months["2026-01"].total, 52.50)

    def test_month_boundary_crosses_in_target_timezone(self):
        # 2026-02-01T02:00:00Z is 2026-01-31T21:00:00 in America/New_York
        # (UTC-5 in February). It must group into 2026-01 in New York time,
        # not 2026-02 in UTC.
        rows = [
            {"receipt_id": "r010", "timestamp_utc": "2026-02-01T02:00:00Z",
             "amount": "15.00", "category": "meals", "note": "late dinner"},
        ]
        result = group_expenses_by_month(rows, tz="America/New_York")
        self.assertIn("2026-02", result.months)

    def test_duplicate_timestamps_are_not_deduplicated(self):
        rows = [
            {"receipt_id": "r020", "timestamp_utc": "2026-03-05T12:00:00Z",
             "amount": "5.00", "category": "meals", "note": "a"},
            {"receipt_id": "r021", "timestamp_utc": "2026-03-05T12:00:00Z",
             "amount": "5.00", "category": "meals", "note": "b"},
        ]
        result = group_expenses_by_month(rows, tz="America/New_York")
        self.assertEqual(result.months["2026-03"].count, 2)

    def test_malformed_row_is_collected_as_error_not_raised(self):
        rows = [
            {"receipt_id": "r030", "timestamp_utc": "not-a-timestamp",
             "amount": "5.00", "category": "meals", "note": "bad"},
            {"receipt_id": "r031", "timestamp_utc": "2026-04-15T18:00:00Z",
             "amount": "5.00", "category": "meals", "note": "good"},
        ]
        result = group_expenses_by_month(rows, tz="America/New_York")
        self.assertEqual(len(result.errors), 1)
        self.assertEqual(result.months["2026-04"].count, 1)


if __name__ == "__main__":
    unittest.main()
