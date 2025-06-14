""" tests/test_operations.py """
import pytest
from typing import Union
from app.operation import Operation


Number = Union[int, float]

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 6, 10),
        (0, 3, 3),
        (-5, 5, 0),
        (2.5, 3.5, 6.0),
        (-2.5, 3.5, 1.0),
    ],
    ids=[
        "add_two_positive_integers",
        "add_zero_and_positive_integer",
        "add_negative_and_positive_integer",
        "add_two_positive_floats",
        "add_negative_float_and_positive_float"
    ]
)

def test_addition(a: Number, b: Number, expected: Number) -> None:
    result = Operation.addition(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"
    
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (8, 3, 5),
        (0, 0, 0),
        (-5, -3, -2),
        (9.5, 5.5, 4.0),
        (-8.5, -4.5, -4.0),
    ],
    ids=[
        "subtract_positive_integer_from_larger",
        "subtract_two_zeros",
        "subtract_negative_integer_from_negative_integer",
        "subtract_two_positive_floats",
        "subtract_two_begative_floats"
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = Operation.subtraction(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 4, 8),
        (0, 8, 0),
        (-5, -3, 15),
        (3.5, 2.0, 7.0),
        (-3.5, 2.0, -7.0)
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_zero_with_positive_integer",
        "multiply_two_negative_numbers",
        "multiply_two_positive_floats",
        "multiply_negative_float_with_positive_float"
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    result = Operation.multiplication(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (15, 3, 5),
        (-10, -2, 5.0),
        (12.0, 6.0, 2.0),
        (-8.0, 2.0, -4.0),
        (0, 9, 0.0),
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positve_integer"
    ]
)
def test_division(a: Number, b: Number, expected: float) -> None:
    result = Operation.division(a, b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),
        (-1, 0),
        (0, 0),
    ],
    ids=[
        "divide_positive_dividend_by_zero",
        "divide_negative_dividend_by_zero",
        "divide_zero_by_zero"
    ]
)
def test_division_by_zero(a: Number, b: Number) -> None:
    with pytest.raises(ValueError, match="Division by zero is not allowed.") as excinfo:
        Operation.division(a, b)

    assert "Division by zero is not allowed." in str(excinfo.value), \
        f"Expected error message 'Division by zero is not allowed.', but got '{excinfo.value}'"