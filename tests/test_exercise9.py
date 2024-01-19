import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise9 import get_values_and_positions
# Define test data
test_data = [
    (['a', 'b', 'c', 'd'], "a, 1\nb, 2\nc, 3\nd, 4"),
    ([], ""),
    (['x'], "x, 1"),
    ([1, 2, 3], "1, 1\n2, 2\n3, 3"),
    (['hello', 'world'], "hello, 1\nworld, 2")
]

@pytest.mark.parametrize("lst, expected", test_data)
def test_get_values_and_positions(lst, expected):
    assert get_values_and_positions(lst) == expected
