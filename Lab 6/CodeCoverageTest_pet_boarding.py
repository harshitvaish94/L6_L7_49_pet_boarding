"""Lab 6 - Code (line) coverage tests for pet_boarding.py
Author: Harshit Vaish | SRN: PES1UG24AM116

Run:
    coverage run -m pytest CodeCoverageTest_pet_boarding.py
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
