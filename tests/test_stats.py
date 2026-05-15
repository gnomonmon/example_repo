import pytest
from mypackage.stats import Stats


@pytest.fixture
def stats():
    return Stats()


def test_mean(stats):
    assert stats.mean([1, 2, 3, 4, 5]) == 3.0
    assert stats.mean([10, 20]) == 15.0
    assert stats.mean([7]) == 7.0


def test_mean_empty(stats):
    with pytest.raises(ValueError, match="Cannot compute mean of empty list"):
        stats.mean([])


def test_median_odd(stats):
    assert stats.median([3, 1, 2]) == 2
    assert stats.median([5]) == 5


def test_median_even(stats):
    assert stats.median([1, 2, 3, 4]) == 2.5
    assert stats.median([10, 20]) == 15.0


def test_median_empty(stats):
    with pytest.raises(ValueError, match="Cannot compute median of empty list"):
        stats.median([])


def test_variance(stats):
    assert stats.variance([2, 4, 4, 4, 5, 5, 7, 9]) == pytest.approx(4.571428, rel=1e-5)
    assert stats.variance([1, 2]) == pytest.approx(0.5)


def test_variance_too_few(stats):
    with pytest.raises(ValueError, match="Variance requires at least two values"):
        stats.variance([42])
    with pytest.raises(ValueError, match="Variance requires at least two values"):
        stats.variance([])


def test_std_dev(stats):
    assert stats.std_dev([2, 4, 4, 4, 5, 5, 7, 9]) == pytest.approx(2.13809, rel=1e-4)


def test_minimum(stats):
    assert stats.minimum([3, 1, 4, 1, 5]) == 1
    assert stats.minimum([-7, 0, 3]) == -7


def test_minimum_empty(stats):
    with pytest.raises(ValueError, match="Cannot compute minimum of empty list"):
        stats.minimum([])


def test_maximum(stats):
    assert stats.maximum([3, 1, 4, 1, 5]) == 5
    assert stats.maximum([-7, 0, 3]) == 3


def test_maximum_empty(stats):
    with pytest.raises(ValueError, match="Cannot compute maximum of empty list"):
        stats.maximum([])
