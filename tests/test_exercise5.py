import pytest

import exercise5


# Tests for a sorting a list. In this case, list of integer and list of strings.
# Feel free to add a test for empty list, or a list with only one element, or negative values.
@pytest.mark.parametrize("unsorted_list, sorted_list", [
    ([2, 1, 3], [1, 2, 3]),
    ([2, 2, 5, 4, 1, 3], [1, 2, 2, 3, 4, 5]),
    (['a', 'c', 'b'], ['a', 'b', 'c'])
])
def test_sort_list(unsorted_list, sorted_list):
    assert exercise5.sort_list(unsorted_list) == sorted_list
