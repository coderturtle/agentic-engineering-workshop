import importlib
import unittest

import receipts.grouping as grouping


class GroupExpensesByWeekTests(unittest.TestCase):
    def setUp(self):
        # Reload the module before every test so each test method starts
        # from a clean slate, regardless of whether group_expenses_by_week
        # happens to hold state between calls in its current implementation.
        # This does not touch what happens *within* a single test method,
        # which is exactly where the ticket's own test needs to catch the
        # bug (two calls inside one test sharing state).
        importlib.reload(grouping)
        self.group_expenses_by_week = grouping.group_expenses_by_week

    def test_empty_input_returns_no_weeks_or_errors(self):
        result = self.group_expenses_by_week([], tz="America/New_York")
        self.assertEqual(result.months, {})
        self.assertEqual(result.errors, [])

    def test_basic_grouping_totals_and_counts(self):
        rows = [
            {"receipt_id": "r001", "timestamp_utc": "2026-01-06T14:30:00Z",
             "amount": "42.50", "category": "meals", "note": "lunch"},
            {"receipt_id": "r002", "timestamp_utc": "2026-01-08T09:00:00Z",
             "amount": "10.00", "category": "meals", "note": "coffee"},
        ]
        result = self.group_expenses_by_week(rows, tz="America/New_York")
        week_key = "2026-01-05"  # Monday of that week, in America/New_York
        self.assertEqual(result.months[week_key].count, 2)
        self.assertAlmostEqual(result.months[week_key].total, 52.50)

    def test_duplicate_timestamps_are_not_deduplicated(self):
        rows = [
            {"receipt_id": "r020", "timestamp_utc": "2026-03-05T12:00:00Z",
             "amount": "5.00", "category": "meals", "note": "a"},
            {"receipt_id": "r021", "timestamp_utc": "2026-03-05T12:00:00Z",
             "amount": "5.00", "category": "meals", "note": "b"},
        ]
        result = self.group_expenses_by_week(rows, tz="America/New_York")
        week_key = "2026-03-02"
        self.assertEqual(result.months[week_key].count, 2)

    def test_malformed_row_is_collected_as_error_not_raised(self):
        rows = [
            {"receipt_id": "r030", "timestamp_utc": "not-a-timestamp",
             "amount": "5.00", "category": "meals", "note": "bad"},
            {"receipt_id": "r031", "timestamp_utc": "2026-04-15T18:00:00Z",
             "amount": "5.00", "category": "meals", "note": "good"},
        ]
        result = self.group_expenses_by_week(rows, tz="America/New_York")
        self.assertEqual(len(result.errors), 1)
        week_key = "2026-04-13"
        self.assertEqual(result.months[week_key].count, 1)

    def test_independent_calls_do_not_leak_totals_into_each_other(self):
        # This is the ticket: `receipts --by-week` reports totals that grow
        # across separate runs in the same process (e.g. a batch job calling
        # this function once per uploaded file). Two independent calls with
        # disjoint data must produce independent results -- the second
        # call's report should reflect only the second call's rows.
        first_rows = [
            {"receipt_id": "r100", "timestamp_utc": "2026-05-04T12:00:00Z",
             "amount": "100.00", "category": "meals", "note": "batch 1"},
        ]
        second_rows = [
            {"receipt_id": "r200", "timestamp_utc": "2026-05-11T12:00:00Z",
             "amount": "7.00", "category": "meals", "note": "batch 2"},
        ]
        self.group_expenses_by_week(first_rows, tz="America/New_York")
        second_result = self.group_expenses_by_week(second_rows, tz="America/New_York")

        first_week_key = "2026-05-04"
        second_week_key = "2026-05-11"
        self.assertNotIn(
            first_week_key, second_result.months,
            "second call's result includes a week from the first call's "
            "rows -- state is leaking between independent calls",
        )
        self.assertEqual(second_result.months[second_week_key].count, 1)
        self.assertAlmostEqual(second_result.months[second_week_key].total, 7.00)


if __name__ == "__main__":
    unittest.main()
