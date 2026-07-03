# Fixture: `receipts`

The shared fixture for Terminal Velocity's five-module arc (`docs/coachgremlin-implementation-plan.md` §2-3). A small, deliberately-flawed CLI that parses expense-receipt CSV rows and prints monthly summaries. It is, in other words, every internal tool ever written for the finance team: small, useful, and wrong near the edges in a way nobody noticed until now.

- Spec and seeded bug: `SPEC.md`.
- Code: `receipts/` (`grouping.py`, `cli.py`).
- Tests: `tests/test_grouping.py`, one test failing against the current code by design.
- Sample data: `data/sample_receipts.csv`.

This is a workshop fixture, not workshop-published prose, so it is out of `scripts/check-brand-lint.sh`'s scope (published content only, per `docs/brand.md`). Code comments here follow ordinary engineering conventions, not the brand voice rules.

Stdlib only, no install step:

```bash
cd fixtures/receipts
PYTHONPATH=. python3 -m unittest discover -s tests -v
```
