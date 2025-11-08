import pytest
from hw2 import bin_search

# pytest way to list used parameters to test function
@pytest.mark.parametrize('target, list_in, expected', [
    (5, [1, 5, 6], 1),  # typical case: target is in the list
    (4, [1, 2, 3], -1),  # target not in the list
    (5, [], -1),  # empty list
    (0, [0], 0),  # single element, target is present
    (3, [3, 7, 10, 31], 0),  # sorted list, target is the first element
    ('Bob', ['Amy', 'Bob', 'Carl'], 1),  # strings
    (5.0, [1.0, 2.0, 5.0, 7.0], 2),  # floats
    (-10, [-10, 0, 100], 0),  # negative, zero, and positive values
])

def test_bin_search(target, list_in, expected):  # test function
    result = bin_search(target, list_in)  # Flip the order of arguments
    assert result == expected  # match against expected