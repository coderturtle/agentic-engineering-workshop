# Task prompt (as provided)

`receipts --tz America/New_York` reports totals that look wrong near a month boundary. `tests/test_grouping.py::test_month_boundary_crosses_in_target_timezone` is failing; every other test in the suite passes.
