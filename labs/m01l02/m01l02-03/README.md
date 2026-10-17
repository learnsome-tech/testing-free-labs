# m01l02-03 · The three phases, separated by blank lines

**Lesson:** [Arrange, Act, Assert](https://learnsome.tech/learn/testing-course/m01l02) (lesson 1.2, module 1: What A Test Is For) · Free  
**Check:** Graded

## Goal

You can write a test in three visible phases, and you can show that the phases make the failure report easier to read than a one line test.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/pricing.py`](starter/pricing.py)
- [`starter/test_pricing.py`](starter/test_pricing.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-03/starter`
2. Read `test_pricing.py`.
3. Notes from the lesson:
   - Line 5: Arrange: the basket, and nothing else this test does not need
   - Line 9: Assert: one comparison, against a number you worked out by hand
4. Run it: `python3 -m pytest -q test_pricing.py`.
5. Check it from the repository root: `./check m01l02-03`.

## Expected output

```text
.                                                                      [100%]
1 passed in 0.00s
```

## How to check

`./check m01l02-03` copies `starter/` into a scratch directory and runs `python3 -m pytest -q test_pricing.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
