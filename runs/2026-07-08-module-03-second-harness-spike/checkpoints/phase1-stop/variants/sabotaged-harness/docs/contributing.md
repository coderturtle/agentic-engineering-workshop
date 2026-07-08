# Contributing

Small internal tool, no formal process. A few conventions worth knowing:

- Run the test suite before opening a PR: `PYTHONPATH=. python3 -m unittest discover -s tests -v`.
- Keep the CLI's default (no-flag) behavior stable; a few internal scripts call it without arguments and assume the current output format.
- New CSV columns should be additive; several downstream consumers read this format positionally in places, not just by header name.
- Prefer small, single-purpose commits. The commit history doubles as informal documentation for anyone debugging a regression later.

Questions go to the finance-tools channel.
