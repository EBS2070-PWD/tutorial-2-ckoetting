import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise4 import (
    check_voting_age,
    check_years_until_retirement,
    check_years_until_pre_retirement,
    calculate_retirement_percentage,
    check_legal_drinking_age
)


def test_check_voting_age():
    assert not check_voting_age(16)
    assert check_voting_age(18)
    assert check_voting_age(21)
    assert check_voting_age(70)


def test_check_years_until_retirement():
    assert check_years_until_retirement(16) == 49
    assert check_years_until_retirement(18) == 47
    assert check_years_until_retirement(50) == 15
    assert check_years_until_retirement(65) == 0
    assert check_years_until_retirement(70) == 0


def test_check_years_until_pre_retirement():
    assert check_years_until_pre_retirement(55) == 5
    assert check_years_until_pre_retirement(60) == 0
    assert check_years_until_pre_retirement(65) == 0


def test_calculate_retirement_percentage():
    assert calculate_retirement_percentage(55) == 0
    assert calculate_retirement_percentage(60) == 60
    assert calculate_retirement_percentage(62) == 76
    assert calculate_retirement_percentage(65) == 100
    assert calculate_retirement_percentage(70) == 100


def test_check_legal_drinking_age():
    assert not check_legal_drinking_age(17)
    assert check_legal_drinking_age(18)
    assert check_legal_drinking_age(21)
    assert check_legal_drinking_age(50)
