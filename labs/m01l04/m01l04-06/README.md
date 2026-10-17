# m01l04-06 · Choosing a layer by marker

**Lesson:** [The Test Pyramid And Where It Is Wrong](https://learnsome.tech/learn/testing-course/m01l04) (lesson 1.4, module 1: What A Test Is For) · Free  
**Check:** Graded

## Goal

You can explain what the test pyramid is really a picture of, mark the slow tests in your suite, and select or deselect them by marker.

## Files

- [`starter/.pytest_cache/.gitignore`](starter/.pytest_cache/.gitignore)
- [`starter/.pytest_cache/CACHEDIR.TAG`](starter/.pytest_cache/CACHEDIR.TAG)
- [`starter/.pytest_cache/README.md`](starter/.pytest_cache/README.md)
- [`starter/.pytest_cache/v/cache/nodeids`](starter/.pytest_cache/v/cache/nodeids)
- [`starter/command.txt`](starter/command.txt)
- [`starter/pricing.py`](starter/pricing.py)
- [`starter/pytest.ini`](starter/pytest.ini)
- [`starter/test_layers.py`](starter/test_layers.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-06/starter`
2. Read `test_layers.py`.
3. Run it: `python3 -m pytest -q -m "not slow" test_layers.py`.
4. Check it from the repository root: `./check m01l04-06`.

## Expected output

```text
.                                                                      [100%]
1 passed, 1 deselected in 0.00s
```

## How to check

`./check m01l04-06` copies `starter/` into a scratch directory and runs `python3 -m pytest -q -m "not slow" test_layers.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. The pytest report is compared by its outcome, not its text: which tests passed, failed or errored, and the final tally (warnings and timings do not count). A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/testing-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
