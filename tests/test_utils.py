import pytest
from mypackage.utils import greet, clamp


def test_utils_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("World") == "Hello, World!"


def test_utils_greet_empty_name():
    assert greet("") == "Hello, !"


def test_utils_clamp_within_range():
    assert clamp(5, 0, 10) == 5


def test_utils_clamp_below_min():
    assert clamp(-5, 0, 10) == 0


def test_utils_clamp_above_max():
    assert clamp(15, 0, 10) == 10


def test_utils_clamp_at_boundaries():
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10
