#!/usr/bin/env bash
# context-budget.sh: measure a curated context set against Module 02's
# stated budget. Harness-neutral: counts lines and characters directly from
# files, no dependency on any one coding agent's token counter. Token counts
# vary by tokenizer; line/char counts don't, which is why this is the
# portable measurement and token-counting is left to a note in the module
# README (per-harness), not this script.
#
# Usage:
#   scripts/context-budget.sh <file-or-dir> [<file-or-dir> ...]
#   scripts/context-budget.sh --limit 2000 <file-or-dir> [...]
#
# Exit status: 0 if under the line budget (default 2000), 1 if over.
set -uo pipefail

LIMIT=2000
ARGS=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    --limit) LIMIT="$2"; shift 2 ;;
    *) ARGS+=("$1"); shift ;;
  esac
done

if [[ ${#ARGS[@]} -eq 0 ]]; then
  echo "usage: context-budget.sh [--limit N] <file-or-dir> [...]" >&2
  exit 2
fi

TOTAL_LINES=0
TOTAL_CHARS=0

echo "-- Context budget (line budget: $LIMIT) --------------------------------"
for path in "${ARGS[@]}"; do
  if [[ -d "$path" ]]; then
    while IFS= read -r -d '' f; do
      lines=$(wc -l < "$f" | tr -d ' ')
      chars=$(wc -c < "$f" | tr -d ' ')
      printf '  %6d lines  %8d chars  %s\n' "$lines" "$chars" "$f"
      TOTAL_LINES=$((TOTAL_LINES + lines))
      TOTAL_CHARS=$((TOTAL_CHARS + chars))
    done < <(find "$path" -type f ! -path '*__pycache__*' -print0)
  elif [[ -f "$path" ]]; then
    lines=$(wc -l < "$path" | tr -d ' ')
    chars=$(wc -c < "$path" | tr -d ' ')
    printf '  %6d lines  %8d chars  %s\n' "$lines" "$chars" "$path"
    TOTAL_LINES=$((TOTAL_LINES + lines))
    TOTAL_CHARS=$((TOTAL_CHARS + chars))
  else
    echo "  WARN: not found: $path" >&2
  fi
done

echo ""
echo "  total: $TOTAL_LINES lines, $TOTAL_CHARS chars"
echo "  rough token estimate (chars / 4): ~$((TOTAL_CHARS / 4)) tokens"
echo ""

if [[ "$TOTAL_LINES" -le "$LIMIT" ]]; then
  echo "OK: at or under the $LIMIT-line budget."
  exit 0
else
  echo "OVER budget: $TOTAL_LINES lines exceeds the $LIMIT-line limit by $((TOTAL_LINES - LIMIT))."
  exit 1
fi
