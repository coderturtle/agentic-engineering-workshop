#!/usr/bin/env bash
# Bounded loop: reproduce -> root-cause -> smallest fix -> rerun tests.
# Terminal states: success = tests green | failure = cannot fix after 2 attempts
set -uo pipefail
cd "$(dirname "$0")"

MAX_ATTEMPTS=2
attempt=1

echo "=== Loop: receipts date-grouping bug ==="
while [ "$attempt" -le "$MAX_ATTEMPTS" ]; do
  echo "--- Attempt $attempt ---"
  PYTHONPATH=. python3 -m unittest discover -s tests -v > /tmp/sabotaged-harness-run.log 2>&1
  status=$?
  cat /tmp/sabotaged-harness-run.log
  if [ "$status" -eq 0 ]; then
    echo "=== TERMINAL STATE: SUCCESS. Tests green. ==="
    exit 0
  fi
  echo "Still failing after attempt $attempt."
  attempt=$((attempt + 1))
done

echo "=== TERMINAL STATE: FAILURE. Could not fix after $MAX_ATTEMPTS attempts. ==="
exit 1
