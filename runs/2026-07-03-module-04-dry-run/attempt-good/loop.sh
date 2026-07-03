#!/usr/bin/env bash
# Ticket-to-PR-Ready loop: reproduce -> root-cause -> smallest fix -> rerun tests.
#
# Ticket: `receipts --tz America/New_York` reports totals that look wrong
# near a month boundary. tests/test_grouping.py::test_month_boundary_crosses_in_target_timezone
# is failing; every other test in the suite passes.
#
# Terminal states, stated before running:
#   success: the full test suite passes
#   failure: cannot reproduce/root-cause after 2 attempts
#
# Decision-rule note (stable-goal-vs-moving-target): this ticket is a stable
# goal, one function has one specified bug against a fixed, described spec,
# so a bounded loop is worth building for it. A moving-target counter-example
# this would NOT be worth loop-ifying: "make the CLI's output nicer," which
# has no fixed definition of done and would keep shifting under the loop.
set -uo pipefail
cd "$(dirname "$0")/receipts-work"

MAX_ATTEMPTS=2
attempt=1

echo "=== Ticket-to-PR-Ready loop: receipts month-boundary bug ==="
echo "Terminal states: success = tests green | failure = cannot reproduce after $MAX_ATTEMPTS attempts"
echo

while [ "$attempt" -le "$MAX_ATTEMPTS" ]; do
  echo "--- Attempt $attempt: reproduce ---"
  PYTHONPATH=. python3 -m unittest tests.test_grouping -v > /tmp/receipts-good-attempt-run.log 2>&1
  cat /tmp/receipts-good-attempt-run.log
  if grep -q "FAIL: test_month_boundary_crosses_in_target_timezone" /tmp/receipts-good-attempt-run.log; then
    echo "Reproduced: test_month_boundary_crosses_in_target_timezone fails."
  else
    echo "Could not reproduce the named failure on attempt $attempt."
    attempt=$((attempt + 1))
    continue
  fi

  echo
  echo "--- Attempt $attempt: root-cause ---"
  echo "Inspecting receipts/grouping.py's month-key computation:"
  grep -n "strftime" receipts/grouping.py
  echo
  echo "Root cause: the month key is computed directly from the UTC"
  echo "timestamp (ts.strftime(\"%Y-%m\")), with no conversion to the"
  echo "target timezone. A receipt near a month boundary in tz lands in"
  echo "the UTC month instead of the local one. This matches SPEC.md edge"
  echo "case 2 exactly."

  echo
  echo "--- Attempt $attempt: smallest fix ---"
  echo "Converting ts to tz via zoneinfo before formatting the key. Not"
  echo "touching parsing, error handling, or the CLI."
  python3 - <<'PYEOF'
import pathlib

path = pathlib.Path("receipts/grouping.py")
src = path.read_text()

src = src.replace(
    "from datetime import datetime\n",
    "from datetime import datetime\nfrom zoneinfo import ZoneInfo\n",
    1,
)
src = src.replace(
    "        receipt_id, ts, amount = parsed\n        key = ts.strftime(\"%Y-%m\")\n",
    "        receipt_id, ts, amount = parsed\n        local_ts = ts.astimezone(ZoneInfo(tz))\n        key = local_ts.strftime(\"%Y-%m\")\n",
    1,
)

path.write_text(src)
print("Patched receipts/grouping.py")
PYEOF

  echo
  echo "--- Attempt $attempt: rerun tests ---"
  PYTHONPATH=. python3 -m unittest discover -s tests -v > /tmp/receipts-good-attempt-rerun.log 2>&1
  rerun_status=$?
  cat /tmp/receipts-good-attempt-rerun.log
  if [ "$rerun_status" -eq 0 ]; then
    echo
    echo "=== TERMINAL STATE: SUCCESS. Tests green. Loop stops. ==="
    exit 0
  else
    echo "Tests still failing after attempt $attempt."
    attempt=$((attempt + 1))
  fi
done

echo
echo "=== TERMINAL STATE: FAILURE. Could not fix after $MAX_ATTEMPTS attempts. ==="
exit 1
