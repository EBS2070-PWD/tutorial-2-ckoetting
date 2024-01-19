import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise8 import generate_dict

# Define test data
test_data = [
    (1, {1: 1}),  # Test with n = 1
    (2, {1: 1, 2: 4}),  # Test with n = 2
    (3, {1: 1, 2: 4, 3: 9}),  # Test with n = 3
    (5, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}),  # Test with n = 5
    (0, {}),  # Test with n = 0 (edge case)
    (8, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64})  # Test with n = 8 (original example)
]


@pytest.mark.parametrize("n, expected", test_data)
def test_generate_dict(n, expected):
    assert generate_dict(n) == expected
