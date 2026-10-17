# m01l02-06 · The same test, all on one line

**Lesson:** [Arrange, Act, Assert](https://learnsome.tech/learn/testing-course/m01l02) (lesson 1.2, module 1: What A Test Is For) · Free  
**Check:** Graded

## Goal

You can write a test in three visible phases, and you can show that the phases make the failure report easier to read than a one line test.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/lastfailed`](starter/.pytest_cache/v/cache/lastfailed)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/pricing.py`](starter/pricing.py)
- [`starter/test_pricing.py`](starter/test_pricing.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-06/starter`
2. Read `test_pricing.py`.
3. Run it: `python3 -m pytest -q --tb=short test_pricing.py`.
4. Check it from the repository root: `./check m01l02-06`.

## Expected output

```text
F                                                                      [100%]
================================== FAILURES ==================================
_____________________ test_vat_is_added_to_the_subtotal ______________________
test_pricing.py:5: in test_vat_is_added_to_the_subtotal
    assert with_vat(subtotal([(250, 2), (125, 4)])) == 1200
E   assert 1250 == 1200
E    +  where 1250 = with_vat(1000)
E    +    where 1000 = subtotal([(250, 2), (125, 4)])
========================== short test summary info ===========================
FAILED test_pricing.py::test_vat_is_added_to_the_subtotal - assert 1250 == 1200
 +  where 1250 = with_vat(1000)
 +    where 1000 = subtotal([(250, 2), (125, 4)])
1 failed in 0.01s
```

## How to check

`./check m01l02-06` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --tb=short test_pricing.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
