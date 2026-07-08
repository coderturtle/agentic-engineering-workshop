# Module 04 Extension B (event-driven loop): the pre-push hook's check, verified live

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

`.git/hooks/pre-push` (already installed in this repo) runs this check automatically on every
`git push`, warn-only: a violation prints a warning but does not block the push. Confirmed by
actually triggering it, not just reading the hook file: `git push --dry-run` still runs
`pre-push` (git fires the hook before the network operation, dry-run or not), and running it for
real produced:

```
$ git push --dry-run origin agent/claude/module-03-agent-native-pilot
-- Mirror drift check --------------------------------------------------
  ...
-- Brand lint (published content only) ----------------------------------
  files checked: 24

  OK: no em dashes in published content
  OK: no banned phrases in published content

Brand lint clean.
To github.com-coderturtle:coderturtle/terminal-velocity.git
 * [new branch]      agent/claude/module-03-agent-native-pilot -> agent/claude/module-03-agent-native-pilot
```

The hook ran both checks (mirror-drift and brand-lint) automatically, with no separate command
for either. A human choosing to run `scripts/check-brand-lint.sh` by hand, as done earlier in this
same session, is the identical loop, manually triggered; the only difference extension B teaches
is removing that manual trigger, and this confirms the automatic path genuinely works, not just
that the hook file exists.

## Result

Real on both counts: the check found three genuine violations in content this session had just
written (via manual invocation), was fixed, and reran clean; separately, the event trigger itself
(a real `git push` tripping `.git/hooks/pre-push`) was observed actually firing and running the
same check automatically, not merely confirmed to exist as a file.

## What "converting a manual loop into an event-driven one" means, generalized

Any bounded, externally-verified loop (the Ticket-to-PR-Ready shape: a fixed check, a pass/fail
terminal state) can gain an event trigger the same way: wrap the check in a hook script (git
hook, CI job, file-watcher, whatever the harness supports) that runs it automatically on the
relevant event and reports pass/fail, without changing the check itself. The check stays
identical; only who/what invokes it changes. `scripts/setup-hooks.sh`'s pattern (install once,
warn-only, never silently block) is the concrete reference other loops in this workshop can copy.
