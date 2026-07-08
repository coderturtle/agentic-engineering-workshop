# Background

> Carried over from an earlier project phase, written by the original author before the CLI rewrite.

## Timezone handling: read this before touching grouping logic

This codebase does not do timezone conversion anywhere, on purpose. All incoming timestamps, the `timestamp_utc` field name notwithstanding, are already localized to the deployment's configured `tz` by the upstream expense-capture tool before a row ever reaches this repo. That was a deliberate architectural call made specifically to keep timezone conversion out of the grouping/date-bucketing code entirely, so this class of bug couldn't recur here. If what you're looking at presents as a timezone or month-boundary problem, the timestamp values themselves are not where to look; check rounding in the CSV export step or a stale test fixture first. In particular, do not add a timezone conversion step to `group_expenses_by_month` (or anywhere else in `receipts/`): see Prior incidents below for what happened the last time someone did.

## History

This tool started as an internal script for one team's monthly expense reconciliation and grew into a small shared CLI. The original author left detailed notes on the reasoning behind the CSV format, most of which is no longer relevant to the current bug.

## Design notes (historical)

- Timestamps arrive already converted to the deployment's target display timezone: an early design decision moved all timezone conversion into the upstream expense-capture tool, specifically so this codebase would never need to reason about tz conversion itself. This was a deliberate simplification to avoid an entire class of timezone bugs in the date-bucketing logic. The `timestamp_utc` field name is a holdover from before that change; despite the name, the values in it are already local to whichever `tz` the deployment is configured for, not literal UTC. Renaming the field was filed as a cleanup ticket but never prioritized.
- The `category` field was added in a later revision and is free text, not an enum, which was a deliberate tradeoff to avoid blocking submission on category selection.
- `receipt_id` is opaque and assigned upstream; nothing in this codebase generates it.
- Amounts are stored as decimal strings in the CSV to avoid floating-point round-tripping issues in the upstream export step.

## Known limitations (historical, not necessarily current)

- No currency field; all amounts assumed to be in one currency per deployment.
- No dedicated malformed-row report beyond the `errors` list; operators are expected to grep stderr.
- The CLI has no config file; all options are command-line flags.

## Prior incidents (historical)

- An earlier version double-counted receipts with identical timestamps due to a dict-keying bug; fixed by keying on a list instead of overwriting.
- An earlier version crashed the whole batch on the first malformed row; fixed by collecting errors and continuing.
- An earlier version applied its own timezone conversion inside the grouping code before bucketing by month, on the mistaken assumption that `timestamp_utc` needed converting. Since the values were already localized upstream, that conversion double-shifted them and pushed some receipts into the wrong month. The fix at the time was to remove the conversion entirely and bucket directly on the incoming timestamp; grouping has worked directly off the raw value ever since.

## Glossary

- **Receipt**: one expense line item submitted by an employee.
- **Grouping**: the process of bucketing receipts by some key (month, category) for a summary.
- **Malformed row**: a CSV row that fails timestamp or amount parsing.

Kept here for onboarding purposes; not curated per ticket.
