import pytest

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise5 import bubble_sort


# Tests for a sorting a list. In this case, list of integer and list of strings.
# Feel free to add a test for empty list, or a list with only one element, or negative values.
@pytest.mark.parametrize("unsorted_list, sorted_list", [
    ([2, 1, 3], [1, 2, 3]),
    ([2, 2, 5, 4, 1, 3], [1, 2, 2, 3, 4, 5]),
    (['a', 'c', 'b'], ['a', 'b', 'c']),
    ([],[])
])
def test_bubble_sort(unsorted_list, sorted_list):
    assert bubble_sort(unsorted_list) == sorted_list
