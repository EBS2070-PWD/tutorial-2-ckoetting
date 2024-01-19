import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise6 import find_numbers

# Test data format: (number, expected_in_list)
test_data = [
    (2002, True),  # divisible by 7, not a multiple of 5
    (2000, False),  # not divisible by 7
    (2030, False),  # divisible by 7 but also a multiple of 5
    (2107, True),  # divisible by 7, not a multiple of 5
    (3199, True),  # divisible by 7, not a multiple of 5
    (3200, False),  # divisible by 7 but also a multiple of 5
]


@pytest.mark.parametrize("number, expected", test_data)
def test_find_numbers(number, expected):
    result = find_numbers()
    assert (number in result) == expected
