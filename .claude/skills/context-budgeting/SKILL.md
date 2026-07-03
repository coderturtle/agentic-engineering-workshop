---
name: context-budgeting
description: Curate a large or noisy codebase down to a fixed context budget without losing what a task actually depends on. Use before starting agentic work in an unfamiliar or bloated repo, when a session is about to exceed a context window, or when a "just include everything" approach has already produced a wrong or distracted output.
---

# Context budgeting

The Module 02 takeaway: the curation judgment from a real exercise (`runs/2026-07-03-module-02-dry-run/`), made loadable instead of one-off. A perfect instruction still fails when the window is wrong or missing what it needs; this is the checklist for making sure it has what it needs and nothing else.

## Checklist, in order

1. **Name the task first, before touching the repo.** What does "done" look like, and what does the check that verifies it actually read? (A test file, a schema, a spec, a golden output.) Everything below is filtered against this, not against "what looks important."
2. **Find what the check depends on.** Trace forward from the verification step: what does it import, call, or assert against? That set is verbatim-required, not summarizable. In the Module 02 exercise, that was the function under test, its signature, and its existing helpers, nothing else.
3. **Cut anything the check doesn't touch.** Not "summarize it down," cut it. A CHANGELOG, a long README, an unrelated module, stale docs: if nothing in the verification path reads them, they're not context, they're noise wearing context's clothes.
4. **Watch for red herrings specifically.** Some noise looks load-bearing (a config file with plausible-sounding values near the task's domain) without being read by anything in the check path. Confirm with a real search (grep for the import, the call site, the reference), not a skim.
5. **Measure before trusting a feeling.** `scripts/context-budget.sh <path>` (or your harness's own token counter; line/char counts are the portable proxy, exact token counts vary by tokenizer). "Feels smaller now" is not a budget.
6. **If it still doesn't fit, cut before you summarize.** Summarizing something that shouldn't have been in scope at all wastes budget on a worse version of something that should have been zero. Only summarize what's genuinely orienting material the task needs some awareness of but not exact text.
7. **Write down what you cut and why**, one line each. Not for ceremony: the write-up is what catches a load-bearing file you cut by mistake, before the task fails and you have to guess why.

## Keep / summarize / cut, the actual heuristic

- **Keep verbatim:** anything the verification step directly reads, calls, or asserts against. Exact text matters; a summary here is a silent edit to the spec.
- **Summarize:** orienting material a task benefits from being aware of but doesn't need word-for-word (a brief note that other modules exist, a one-line description of surrounding architecture).
- **Cut:** everything else. Default to cut, not summarize, for anything not in the verification path. Summarizing is still spending budget.

## When to reach for this

Any time a repo is bigger than what one task needs, which is most of the time. Not needed for a task that's already scoped to a small, isolated file set; the judgment call here only matters once there's real noise to cut through.
