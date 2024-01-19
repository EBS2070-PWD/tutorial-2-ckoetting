import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise11 import count_matching_strings
# Define test data
test_data = [
    (['abc', 'xyz', 'aba', '1221'], 2),
    ([], 0),
    (['a', 'bb', 'cc', 'ddd', 'eeee'], 4),
    (['python', 'php', 'cpp', 'java'], 1),
    (['aa', 'ab', 'ba', 'bb'], 2)
]

@pytest.mark.parametrize("strings, expected", test_data)
def test_count_matching_strings(strings, expected):
    assert count_matching_strings(strings) == expected
