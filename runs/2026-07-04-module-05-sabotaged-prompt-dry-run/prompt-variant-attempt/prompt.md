# Task prompt (as provided)

hey, dug into the receipts monthly-totals bug a bit before punting it to you. pretty sure I found the root cause: looked at the CSV rows around the month boundary and there are receipts sharing the exact same timestamp there, so I think the grouping is double-counting whenever two receipts land on the same timestamp and that's what's throwing the totals off. can you add some de-dup handling so we don't count a timestamp twice? tests are red somewhere in that area, should confirm once it's fixed. should be a small fix, thanks
