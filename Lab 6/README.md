# L6_L7_49 — Pet Boarding

## Lab 6: Code and Branch Coverage

**Name:** Harshit Vaish
**SRN:** PES1UG24AM116

## About
A small Python module that works out boarding fees by pet type, days and premium kennel, checks whether a pet can be admitted and reports checkout status.

## Files
| File | Description |
|---|---|
| `pet_boarding.py` | The module under test |
| `test_pet_boarding.py` | Starter test file (2 tests) |
| `CodeCoverageTest_pet_boarding.py` | Test cases for code (line) coverage — 13 tests |
| `BranchCoverageTest_pet_boarding.py` | Test cases for branch coverage — 34 tests |
| `screenshots/code_coverage_result.png` | Terminal output: code coverage analysis |
| `screenshots/branch_coverage_result.png` | Terminal output: branch coverage analysis |
| `.gitignore` | Excludes `__pycache__/`, `.coverage`, `.pytest_cache/` |

## Results
| Stage | Test file | Tests | Statements | Branches | Coverage |
|---|---|---|---|---|---|
| Baseline | `test_pet_boarding.py` | 2 | 37 (23 missed) | 26 | 38% line |
| Code coverage | `CodeCoverageTest_pet_boarding.py` | 13 | 37 (0 missed) | 26 | **100% line** |
| Branch coverage | `BranchCoverageTest_pet_boarding.py` | 34 | 37 (0 missed) | 26 (0 partial) | **100% line + branch** |

## What was done
1. **Baseline:** ran the starter tests with coverage — only 38% of `pet_boarding.py` was covered (missing lines 6, 8, 11, 15-23, 28, 30, 35-45).
2. **Code coverage:** added tests for every function — invalid pet type and negative days, premium kennel, dog/cat rates, the long-stay surcharge, senior/underage/normal admission, and all three checkout statuses (`open`, `late`, `closed`). Result: 100% line coverage. *(Commit 1)*
3. **Branch analysis:** running the same tests with `--branch` showed 98%, with one partial branch (`21->23`: the surcharge applied to a non-dog pet). This shows how line coverage can hide untested decision outcomes.
4. **Branch coverage:** added tests for the True and False outcome of every decision — the rabbit premium exception, non-dog surcharge, boundary values (`extra` 0/1/10/11, age 1, checkout cutoffs with weekend and long-stay combinations). Result: 100% branch coverage, 26/26 branches. *(Commit 2)*
5. **Cleanup:** removed generated files and added a `.gitignore`. *(Commit 3)*

## How to run
```
pip install coverage pytest

# Code (line) coverage
python -m coverage run -m pytest CodeCoverageTest_pet_boarding.py
python -m coverage report -m --include=pet_boarding.py

# Branch coverage
python -m coverage run --branch -m pytest BranchCoverageTest_pet_boarding.py
python -m coverage report -m --include=pet_boarding.py
```
Run these from inside the `Lab 6` folder.

## Commits
| # | Message |
|---|---|
| 1 | Lab 6: add code coverage tests |
| 2 | Lab 6: add branch coverage tests |
| 3 | Lab 6: remove generated files, add .gitignore |
