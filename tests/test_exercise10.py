import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise10 import align_lists
# Define test data
test_data = [
    ([1, 2, 3, 4], ['a', 'b', 'c', 'd'], ['z', 'y', 'x', 'w'], [(1, 'a', 'z'), (2, 'b', 'y'), (3, 'c', 'x'), (4, 'd', 'w')]),
    ([], [], [], []),
    ([1], ['a'], ['z'], [(1, 'a', 'z')]),
    (['one', 'two'], ['alpha', 'beta'], ['A', 'B'], [('one', 'alpha', 'A'), ('two', 'beta', 'B')])
]

@pytest.mark.parametrize("list1, list2, list3, expected", test_data)
def test_align_lists(list1, list2, list3, expected):
    assert align_lists(list1, list2, list3) == expected
