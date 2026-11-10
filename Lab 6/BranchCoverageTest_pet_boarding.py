"""Lab 6 - Branch coverage tests for pet_boarding.py
Author: Harshit Vaish | SRN: PES1UG24AM116

Builds on the line-coverage suite and adds the missing True/False outcome of
every decision (premium vs non-premium, rabbit exception, surcharge for
non-dog, weekend vs weekday, boundaries of each threshold).

Run:
    coverage run --branch -m pytest BranchCoverageTest_pet_boarding.py
    coverage report -m
"""
import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


# ---------- boarding_fee ----------
def test_within_included_days():
    assert boarding_fee("dog", 1, False) == 0

def test_unknown_pet_type_raises():
    with pytest.raises(ValueError, match="unknown pet type"):
        boarding_fee("hamster", 2, False)

def test_negative_days_raises():
    with pytest.raises(ValueError, match="invalid days"):
        boarding_fee("cat", -1, False)

def test_premium_dog_gets_extra_included_day():
    # dog: 2 + 1 premium = 3 included -> 3 days is free
    assert boarding_fee("dog", 3, True) == 0

def test_dog_extra_days_rate_30():
    assert boarding_fee("dog", 5, False) == 3 * 30

def test_cat_extra_days_rate_20():
    assert boarding_fee("cat", 5, False) == 2 * 20

def test_dog_long_stay_surcharge():
    # extra = 18 (>10): rate 30 + 10 + 5 = 45
    assert boarding_fee("dog", 20, False) == 18 * 45


# ---------- admission_ok ----------
def test_admission_ok():
    assert admission_ok(4, 2, False) is True

def test_senior_needs_three_vaccinations():
    assert admission_ok(10, 3, True) is True

def test_puppy_under_one_year_rejected():
    assert admission_ok(0, 5, False) is False


# ---------- checkout_status ----------
def test_checkout_long_stay_weekend_open():
    assert checkout_status(50, True, True) == "open"

def test_checkout_short_stay_weekday_late():
    assert checkout_status(10, False, False) == "late"

def test_checkout_closed():
    assert checkout_status(-5, False, False) == "closed"


# =====================  ADDITIONAL BRANCH TESTS  =====================

# ---- boarding_fee ----
def test_premium_rabbit_gets_no_extra_day():
    # `is_premium and pet_type != "rabbit"` -> True and False branch
    assert boarding_fee("rabbit", 5, True) == 1 * 20      # included stays 4

def test_non_premium_rabbit():
    assert boarding_fee("rabbit", 5, False) == 1 * 20

def test_premium_cat_gets_extra_day():
    assert boarding_fee("cat", 5, True) == 1 * 20          # included 4

def test_zero_days_is_free():
    assert boarding_fee("cat", 0, False) == 0

def test_exact_included_boundary_is_free():
    assert boarding_fee("cat", 3, False) == 0              # extra == 0

def test_one_day_over_included():
    assert boarding_fee("dog", 3, False) == 30             # extra == 1

def test_surcharge_boundary_extra_10_no_surcharge():
    assert boarding_fee("dog", 12, False) == 10 * 30       # extra == 10

def test_surcharge_boundary_extra_11_dog():
    assert boarding_fee("dog", 13, False) == 11 * 45       # extra == 11

def test_surcharge_cat_no_dog_bonus():
    # extra > 10 and pet is NOT a dog -> inner `if` False branch
    assert boarding_fee("cat", 14, False) == 11 * 30       # 20 + 10

def test_surcharge_rabbit_premium():
    assert boarding_fee("rabbit", 15, True) == 11 * 30     # included 4

def test_unknown_pet_type_case_sensitive():
    with pytest.raises(ValueError):
        boarding_fee("Dog", 1, False)

def test_zero_days_valid_not_error():
    # days < 0 is False for 0
    assert boarding_fee("dog", 0, True) == 0


# ---- admission_ok ----
def test_senior_with_too_few_vaccinations():
    assert admission_ok(12, 2, True) is False

def test_senior_ignores_age_check():
    assert admission_ok(0, 3, True) is True

def test_adult_with_too_few_vaccinations():
    assert admission_ok(4, 1, False) is False

def test_age_boundary_exactly_one_year():
    assert admission_ok(1, 2, False) is True

def test_age_just_below_one_year():
    assert admission_ok(0.9, 2, False) is False


# ---- checkout_status ----
def test_checkout_long_stay_weekday_cutoff_30():
    assert checkout_status(30, True, False) == "open"
    assert checkout_status(29, True, False) == "late"

def test_checkout_short_stay_weekend_cutoff_35():
    assert checkout_status(35, False, True) == "open"
    assert checkout_status(34, False, True) == "late"

def test_checkout_short_weekday_boundaries():
    assert checkout_status(15, False, False) == "open"
    assert checkout_status(14, False, False) == "late"
    assert checkout_status(0, False, False) == "late"      # cutoff - 15
    assert checkout_status(-1, False, False) == "closed"

def test_checkout_long_weekend_boundaries():
    assert checkout_status(50, True, True) == "open"
    assert checkout_status(49, True, True) == "late"
    assert checkout_status(35, True, True) == "late"
    assert checkout_status(34, True, True) == "closed"
