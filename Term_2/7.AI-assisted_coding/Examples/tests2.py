import pytest
from two_largest import two_largest as find_two_largest

def test_two_largest_with_valid_list():
    assert find_two_largest([10, 20, 30, 40]) == (40, 30)
    assert find_two_largest([5, 1, 3, 2]) == (5, 3)
    assert find_two_largest([100, 50]) == (100, 50)

def test_two_largest_with_duplicates():
    assert find_two_largest([10, 10, 20, 20]) == (20, 20)
    assert find_two_largest([5, 5, 5, 5]) == (5, 5)

def test_two_largest_with_negative_numbers():
    assert find_two_largest([-10, -20, -30, -40]) == (-10, -20)
    assert find_two_largest([-5, -1, -3, -2]) == (-1, -2)

def test_two_largest_with_mixed_numbers():
    assert find_two_largest([-10, 20, 0, 15]) == (20, 15)
    assert find_two_largest([0, -1, 1, -2]) == (1, 0)

def test_two_largest_with_invalid_list():
    with pytest.raises(ValueError):
        find_two_largest([10])  # Less than 2 numbers
    with pytest.raises(ValueError):
        find_two_largest([])  # Empty list