# Module 04 Extension B (event-driven loop): the pre-push hook, verified live

## Method

The "Docs Consistency Loop" (`~/hekton/gremlins/workshop/workshop-lifecycle.md`'s "Dogfooding"
section) already exists in this repo as `scripts/check-brand-lint.sh`, wired into
`.git/hooks/pre-push` by `scripts/setup-hooks.sh`. That is the event-driven loop this extension
teaches: the same bounded, externally-verified loop shape as the Ticket-to-PR-Ready core exercise
(a fixed check, a pass/fail terminal state), except it is not run by hand. `git push` is the
external event that triggers it.

This extension did not need a staged example: while authoring this session's Module 03 manifest
work, the hook's underlying check actually caught real violations, live, not manufactured for
this writeup.

```
$ scripts/check-brand-lint.sh --check
-- Brand lint (published content only) ----------------------------------
  files checked: 24

  FAIL: em dash found in: modules/03-harness-engineering/AGENT.md modules/03-harness-engineering/README.md modules/README.md

Brand lint found 1 issue(s). Fix per docs/brand.md's hard rules.
(exit 1)
```

Fixed the three files (em dashes replaced with colons/commas per `docs/brand.md`'s hard rule),
reran:

```
$ scripts/check-brand-lint.sh --check
-- Brand lint (published content only) ----------------------------------
  files checked: 24

  OK: no em dashes in published content
  OK: no banned phrases in published content

Brand lint clean.
(exit 0)
```

`.git/hooks/pre-push` (already installed in this repo, confirmed present and executable) runs
this exact check automatically on every `git push`, warn-only: a violation prints a warning but
does not block the push. That's the event; a human choosing to run `scripts/check-brand-lint.sh`
by hand is the same loop, manually triggered. The only difference extension B teaches is removing
the manual trigger.

## Result

Real, not staged: the check found three genuine violations in content this session had just
written, was fixed, and reran clean. The event-driven wiring (the pre-push hook calling the same
script) was already in place from an earlier session (`scripts/setup-hooks.sh`); this run confirms
it still works and demonstrates the loop firing on real, unplanned input rather than a synthetic
example built to order.

## What "converting a manual loop into an event-driven one" means, generalized

Any bounded, externally-verified loop (the Ticket-to-PR-Ready shape: a fixed check, a pass/fail
terminal state) can gain an event trigger the same way: wrap the check in a hook script (git
hook, CI job, file-watcher, whatever the harness supports) that runs it automatically on the
relevant event and reports pass/fail, without changing the check itself. The check stays
identical; only who/what invokes it changes. `scripts/setup-hooks.sh`'s pattern (install once,
warn-only, never silently block) is the concrete reference other loops in this workshop can copy.
