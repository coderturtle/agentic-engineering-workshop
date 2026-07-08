# Fixture variant: unimplemented

Used by Module 01 (prompt engineering) and, buried in noise, Module 02 (context engineering). `receipts/grouping.py`'s `group_expenses_by_month` is stubbed to `raise NotImplementedError`; every other file (parsing, the CLI, the test suite) is the same as the base fixture.

This is a different exercise than Module 04's: Module 04 fixes one bug in a working implementation, Module 01 writes the whole function from the spec in `SPEC.md`, first try, from a single prompt. Sharing a starting point that already had a plausible-looking wrong implementation would make it too easy to lean on the existing code instead of the prompt.

```bash
cd fixtures/receipts/variants/unimplemented
PYTHONPATH=. python3 -m unittest discover -s tests -v
```

All 5 tests fail via `NotImplementedError` until the function is written.
