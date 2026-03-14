import pytest
from hw import equal_sum_partitions

def test_no_partition_possible():
    assert equal_sum_partitions([1, 2, 3]) == []

def test_simple_partition():
    result = equal_sum_partitions([1, 1])
    assert ([1], [1]) in [(tuple(a), tuple(b)) for a, b in result] or ([1], [1]) in [(tuple(b), tuple(a)) for a, b in result]

def test_multiple_partitions():
    result = equal_sum_partitions([1, 2, 3, 4])
    expected = [
        ([1, 4], [2, 3]),
    ]
    found = False
    for a, b in result:
        if sorted(a) == [1, 4] and sorted(b) == [2, 3]:
            found = True
        if sorted(b) == [1, 4] and sorted(a) == [2, 3]:
            found = True
    assert found

def test_empty_list():
    assert equal_sum_partitions([]) == []

def test_single_element():
    assert equal_sum_partitions([5]) == []

def test_duplicates():
    result = equal_sum_partitions([2, 2, 2, 2])
    expected = [
        ([2, 2], [2, 2]),
    ]
    found = False
    for a, b in result:
        if sorted(a) == [2, 2] and sorted(b) == [2, 2]:
            found = True
    assert found