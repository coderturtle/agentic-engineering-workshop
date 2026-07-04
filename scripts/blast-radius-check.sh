#!/usr/bin/env bash
# blast-radius-check.sh: verify a fix's diff touches only the files it's allowed to.
#
# This is Module 04's Extension A (verification loop, deepened): the core exercise's
# rubric already requires a human/Coachgremlin grader to eyeball a diff's target files
# (see runs/2026-07-03-module-04-dry-run/grading.md, criterion 4). This script turns
# that manual check into an automated grading pass a loop can run itself, after tests
# go green but before declaring the terminal state SUCCESS: green tests plus an
# out-of-bounds diff is not a pass, so blast radius gets its own check rather than
# being folded silently into "tests passed."
#
# Reusable, not receipts-specific: takes the allowed path glob(s) as arguments, so any
# Ticket-to-PR-Ready-style loop can drop this in with its own scope.
#
# Usage:
#   blast-radius-check.sh --diff <patch-file> <allowed-glob> [<allowed-glob> ...]
#   blast-radius-check.sh --git  <allowed-glob> [<allowed-glob> ...]   # git diff --name-only, cwd
#
# Exit 0: every touched file matched an allowed glob (PASS).
# Exit 1: at least one touched file matched no allowed glob (FAIL); violators are listed.
#
# Network: none. Pure local file/diff inspection.
set -uo pipefail

mode="${1:-}"
case "$mode" in
  --diff)
    patch_file="${2:-}"
    shift 2 || { echo "usage: blast-radius-check.sh --diff <patch-file> <allowed-glob>..." >&2; exit 2; }
    if [[ -z "$patch_file" || ! -f "$patch_file" ]]; then
      echo "blast-radius-check: patch file not found: $patch_file" >&2
      exit 2
    fi
    # Unified-diff "+++ b/path" (or a bare "+++ path") lines name the touched file.
    # Strip a leading "a/" or "b/" prefix if present (git-style); otherwise take the
    # path as-is (this fixture's diffs use plain relative paths, not a/ b/ prefixes).
    touched="$(grep -E '^\+\+\+ ' "$patch_file" | sed -E 's#^\+\+\+ (b/)?##' | sed -E 's/\t.*//')"
    ;;
  --git)
    shift 1
    touched="$(git diff --name-only; git diff --cached --name-only)"
    touched="$(echo "$touched" | sort -u | grep -v '^$' || true)"
    ;;
  *)
    echo "usage: blast-radius-check.sh --diff <patch-file> <allowed-glob>... | --git <allowed-glob>..." >&2
    exit 2
    ;;
esac

if [[ "$#" -eq 0 ]]; then
  echo "blast-radius-check: no allowed-glob patterns given" >&2
  exit 2
fi

allowed_globs=("$@")

if [[ -z "$touched" ]]; then
  echo "blast-radius-check: no changed files detected — nothing to check."
  exit 0
fi

violations=()
while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  match=false
  for glob in "${allowed_globs[@]}"; do
    # shellcheck disable=SC2053 -- intentional unquoted glob match
    # Match the pattern exactly, or as a suffix after any path prefix (so an
    # allowlist of "receipts/grouping.py" matches that path however it's rooted:
    # "receipts/grouping.py", "receipts-work/receipts/grouping.py", etc.)
    if [[ "$f" == $glob || "$f" == */$glob ]]; then
      match=true
      break
    fi
  done
  if [[ "$match" == false ]]; then
    violations+=("$f")
  fi
done <<< "$touched"

echo "Changed files:"
echo "$touched" | sed 's/^/  /'
echo "Allowed pattern(s): ${allowed_globs[*]}"

if [[ "${#violations[@]}" -gt 0 ]]; then
  echo ""
  echo "=== BLAST RADIUS: FAIL. Out-of-bounds file(s): ==="
  printf '  %s\n' "${violations[@]}"
  exit 1
fi

echo ""
echo "=== BLAST RADIUS: PASS. All changes within allowed scope. ==="
exit 0
