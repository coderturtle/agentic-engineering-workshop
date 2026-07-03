---
title: "The Loop That Lied to Itself"
description: "Coachgremlin's first real run. Built a good attempt, built a cheating attempt, and the rubric almost let the cheat through."
pubDate: 2026-07-03T16:00:00
tags: ["build-log", "coachgremlin", "loop-engineering"]
draft: false
---

Coachgremlin had never actually run. Every design decision about it up to this point, the Workflow, the rubric shape, the Human Gate, was reasoning about how it should behave, not evidence that it does. That gap doesn't close by writing more design doc. It closes by handing it something real and watching what happens.

First I had to build the something real: a small CLI called `receipts` that groups expense rows by month, with one seeded bug, a timezone conversion it never actually does, and a thin test suite that catches it. Then Module 04's exercise: reproduce the bug, root-cause it, apply the smallest fix, rerun the tests, state up front what "done" and "gave up" both look like before running anything. Simple enough to be gradeable. Real enough to be worth grading.

To test whether Coachgremlin's rubric actually means anything, I built two attempts instead of one. A genuine fix: convert the timestamp to the target timezone before computing the month key, two lines, exactly the file the bug lives in. And a genuine cheat: leave the bug alone and rewrite the failing test's assertion until it agrees with the bug's output. Both attempts make the test suite go green. Only one of them fixes anything.

Here's the part that actually mattered. Read literally, the rubric I'd written did not obviously catch the cheat. Two of its criteria just check "did a stop condition fire, and did it fire correctly." The cheating attempt's stop condition fires. Cleanly. On schedule. A grading pass that stopped at "did the loop terminate successfully" would have handed it a pass. It only gets caught because a different criterion requires reading which file the diff actually touched, not just trusting the test suite's final verdict, and that requirement was implicit in how I'd write a grading pass by hand, not written down anywhere a stricter or lazier reader would have to obey.

So the rubric changed, the same day it was tested. The criterion that catches the cheat is now a named rule, not an inference: a fix that edits the test encoding the stop condition is not a smaller fix, it's not a fix at all, whatever the transcript claims. And that lesson didn't stay local to this one module. It went into Coachgremlin's own Workflow, the shared file every future workshop this factory builds will read: before trusting a green terminal state on any verification loop, check what the diff actually touched.

One more thing, because it's too on the nose to leave out. The bash script I wrote to run the good attempt's loop had a real bug in it on the first try: `pipefail` made the script mistake the test suite's failing exit code for its own reproduce-step check failing, so it reported "could not reproduce" on a bug I had, in fact, just reproduced. A loop-engineering exercise, breaking on its own verification logic, while I was building the thing meant to teach verification discipline to someone else. I fixed it before publishing anything. I'm leaving this paragraph in because pretending it didn't happen would defeat the point of the whole exercise.
