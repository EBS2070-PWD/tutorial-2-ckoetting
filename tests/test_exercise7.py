import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise7 import remove_negatives

# Define test data
test_data = [
    ([1, -1, 2, -2, 3, -3], [1, 2, 3]),  # mixed positive and negative integers
    ([1.5, -2.5, 3.5, 0, -4.5], [1, 3]),  # mixed positive and negative floats, with zero
    ([-1, -2, -3, -4], []),              # all negative numbers
    ([], []),                             # empty list
    ([10, 20, 30], [10, 20, 30])          # all positive numbers
]

@pytest.mark.parametrize("number_list, expected", test_data)
def test_remove_negatives(number_list, expected):
    assert remove_negatives(number_list) == expected
