# Background

> Carried over from an earlier project phase, written by the original author before the CLI rewrite.

## History

This tool started as an internal script for one team's monthly expense reconciliation and grew into a small shared CLI. The original author left detailed notes on the reasoning behind the CSV format, most of which is no longer relevant to the current bug.

## Design notes (historical)

- Timestamps are stored in UTC in the source system, per an early integration decision with the upstream expense-capture tool.
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

## Glossary

- **Receipt**: one expense line item submitted by an employee.
- **Grouping**: the process of bucketing receipts by some key (month, category) for a summary.
- **Malformed row**: a CSV row that fails timestamp or amount parsing.

Kept here for onboarding purposes; not curated per ticket.
