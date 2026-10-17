# m01l01-05 · The test catches it

**Lesson:** [The Cost And Value Of A Test](https://learnsome.tech/learn/testing-course/m01l01) (lesson 1.1, module 1: What A Test Is For) · Free  
**Check:** Graded

## Goal

You can say what a test buys you and what it costs to keep, and you can watch a test catch a regression the moment somebody introduces it.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/lastfailed`](starter/.pytest_cache/v/cache/lastfailed)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/cart.py`](starter/cart.py)
- [`starter/command.txt`](starter/command.txt)
- [`starter/test_cart.py`](starter/test_cart.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-05/starter`
2. Read `test_cart.py`.
3. Run it: `python3 -m pytest -q --tb=short test_cart.py`.
4. Check it from the repository root: `./check m01l01-05`.

## Expected output

```text
F                                                                      [100%]
================================== FAILURES ==================================
___________________________ test_two_lines_add_up ____________________________
test_cart.py:5: in test_two_lines_add_up
    assert total([(250, 2), (125, 4)]) == 1000
E   assert 900 == 1000
E    +  where 900 = total([(250, 2), (125, 4)])
========================== short test summary info ===========================
FAILED test_cart.py::test_two_lines_add_up - assert 900 == 1000
 +  where 900 = total([(250, 2), (125, 4)])
1 failed in 0.01s
```

## How to check

`./check m01l01-05` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --tb=short test_cart.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
