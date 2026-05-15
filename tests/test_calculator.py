import pytest
from mypackage.calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_calculator_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(0, 0) == 0


def test_calculator_subtract(calculator):
    assert calculator.subtract(10, 4) == 6
    assert calculator.subtract(0, 5) == -5


def test_calculator_multiply(calculator):
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10
    assert calculator.multiply(0, 100) == 0


def test_calculator_divide(calculator):
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(7, 2) == 3.5


def test_calculator_divide_by_zero(calculator):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(5, 0)
