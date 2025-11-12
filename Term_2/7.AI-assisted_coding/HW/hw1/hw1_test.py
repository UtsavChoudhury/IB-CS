import pytest
from hw1 import powersort

def test_basic_sort():
    assert powersort([123, 99, 12, 45, 100, 7]) == [100, 12, 123, 7, 45, 99]

def test_same_digit_sum():
    # 12 (1+2=3), 21 (2+1=3), 30 (3+0=3)
    assert powersort([21, 30, 12]) == [12, 21, 30]

def test_negative_numbers():
    # -12 (1+2=3), 21 (2+1=3), -30 (3+0=3)
    assert powersort([-12, 21, -30]) == [-30, -12, 21]

def test_empty_list():
    assert powersort([]) == []

def test_single_element():
    assert powersort([42]) == [42]

def test_large_numbers():
    # 1000 (1), 100 (1), 10 (1), 1 (1)
    assert powersort([1000, 1, 10, 100]) == [1, 10, 100, 1000]