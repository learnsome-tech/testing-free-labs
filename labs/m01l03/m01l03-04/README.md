# m01l03-04 · Three claims in three tests

**Lesson:** [One Assertion Per Reason](https://learnsome.tech/learn/testing-course/m01l03) (lesson 1.3, module 1: What A Test Is For) · Free  
**Check:** Graded

## Goal

You can split a test so that each one fails for exactly one reason, and you can explain why the first failing assertion hides every assertion after it.

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

1. Go to the starter: `cd labs/m01l03/m01l03-04/starter`
2. Read `test_pricing.py`.
3. Run it: `python3 -m pytest -q --tb=no test_pricing.py`.
4. Check it from the repository root: `./check m01l03-04`.

## Expected output

```text
.FF                                                                    [100%]
========================== short test summary info ===========================
FAILED test_pricing.py::test_the_default_rate_is_twenty - assert 1175 == 1200
 +  where 1175 = with_vat(1000)
FAILED test_pricing.py::test_vat_rounds_to_the_penny - assert 1173 == 1199
 +  where 1173 = with_vat(999)
2 failed, 1 passed in 0.00s
```

## How to check

`./check m01l03-04` copies `starter/` into a scratch directory and runs `python3 -m pytest -q --tb=no test_pricing.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
