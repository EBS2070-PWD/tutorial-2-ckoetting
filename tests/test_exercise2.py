import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise2 import check_voting_age, check_years_until_retirement


def test_check_voting_age():
    assert check_voting_age(16) == False
    assert check_voting_age(18) == True
    assert check_voting_age(21) == True
    assert check_voting_age(70) == True


def test_check_years_until_retirement():
    assert check_years_until_retirement(16) == 49
    assert check_years_until_retirement(18) == 47
    assert check_years_until_retirement(50) == 15
    assert check_years_until_retirement(65) == 0
    assert check_years_until_retirement(70) == 0
