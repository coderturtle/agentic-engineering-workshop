# Takeaway validation: a second, different ticket

Per `docs/coachgremlin-implementation-plan.md` §7: "the takeaway is genuinely reusable... drop the packaged artifact into a different task and confirm it helps." This directory is throwaway evidence for that check, not part of the shipped `receipts` fixture: a second, unrelated bug (word-frequency ranking, not timezones) used only to confirm `.claude/commands/ticket-to-pr-ready.md`'s steps transfer past the exercise they were built against.

Ticket: `top_n_words(text, n)` in `word_stats.py` is supposed to return the `n` most frequent words, most frequent first. `test_word_stats.py::test_top_n_words_returns_n_items` fails: it returns `n - 1` words.

Result: applying the template's six steps (classify, reproduce, root-cause, smallest fix, rerun, stop) found and fixed a one-line off-by-one slicing bug (`ranked[:n-1]` should be `ranked[:n]`), untouched test file, terminal state SUCCESS fired. See `transcript.txt`.
