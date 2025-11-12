import pytest
from example1 import fun

def test_gcd_positive_numbers():
    assert fun(48, 18) == 6
    assert fun(101, 103) == 1
    assert fun(56, 98) == 14

def test_gcd_with_zero():
    assert fun(0, 5) == 5
    assert fun(7, 0) == 7
    assert fun(0, 0) == 0

def test_gcd_same_numbers():
    assert fun(12, 12) == 12
    assert fun(100, 100) == 100

def test_gcd_negative_numbers():
    assert fun(-48, 18) == 6
    assert fun(48, -18) == 6
    assert fun(-48, -18) == 6

def test_gcd_one():
    assert fun(1, 99) == 1
    assert fun(99, 1) == 1
    assert fun(1, 1) == 1