import pytest
from unittest.mock import patch
from app.operation import Operation
from app.calculation import (
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
    Calculation
)

# Postive and Negative Tests for Execute Method

@patch.object(Operation, 'addition')
def test_add_calculation_execute_positive(mock_addition):
    a = 10.0
    b = 5.0
    expected_result = 15.0
    mock_addition.return_value = expected_result
    add_calc = AddCalculation(a, b)

    result = add_calc.execute()
    mock_addition.assert_called_once_with(a, b)
    assert result == expected_result

@patch.object(Operation, 'addition')
def test_add_calculation_execute_negative(mock_addition):
    a = 10.0
    b = 5.0
    mock_addition.side_effect = Exception("Addition error")
    add_calc = AddCalculation(a, b)

    with pytest.raises(Exception) as exc_info:
        add_calc.execute()

    assert str(exc_info.value) == "Addition error"

@patch.object(Operation, 'subtraction')
def test_subtract_calculation_execute_positive(mock_subtraction):
    a = 10.0
    b = 5.0
    expected_result = 5.0
    mock_subtraction.return_value = expected_result
    subtract_calc = SubtractCalculation(a, b)

    result = subtract_calc.execute()
    mock_subtraction.assert_called_once_with(a, b)
    assert result == expected_result

@patch.object(Operation, 'subtraction')
def test_subtract_calculation_execute_negative(mock_subtraction):
    a = 10.0
    b = 5.0
    mock_subtraction.side_effect = Exception("Subtraction error")
    subtract_calc = SubtractCalculation(a, b)

    with pytest.raises(Exception) as exc_info:
        subtract_calc.execute()

    assert str(exc_info.value) == "Subtraction error"

@patch.object(Operation, 'multiplication')
def test_multiply_calculation_execute_positive(mock_multiplication):
    a = 4.0
    b = 11.0
    expected_result = 44.0
    mock_multiplication.return_value = expected_result
    multiply_calc = MultiplyCalculation(a, b)

    result = multiply_calc.execute()
    mock_multiplication.assert_called_once_with(a, b)
    assert result == expected_result

@patch.object(Operation, 'multiplication')
def test_multiply_calculation_execute_negative(mock_multiplication):
    a = 4.0
    b = 11.0
    mock_multiplication.side_effect = Exception("Multiplication error")
    multiply_calc = MultiplyCalculation(a, b)

    with pytest.raises(Exception) as exc_info:
        multiply_calc.execute()

    assert str(exc_info.value) == "Multiplication error"

@patch.object(Operation, 'division')
def test_divide_calculation_execute_positive(mock_division):
    a = 20.0
    b = 5.0
    expected_result = 4.0
    mock_division.return_value = expected_result
    divide_calc = DivideCalculation(a, b)

    result = divide_calc.execute()
    mock_division.assert_called_once_with(a, b)
    assert result == expected_result

@patch.object(Operation, 'division')
def test_divide_calculation_execution_negative(mock_divison):
    a = 20.0
    b = 5.0
    mock_divison.side_effect = Exception("Division error")
    divide_calc = DivideCalculation(a, b)

    with pytest.raises(Exception) as exc_info:
        divide_calc.execute()

    assert str(exc_info.value) == "Division error"

def test_divide_calculation_execute_division_by_zero():
    a = 10.0
    b = 0.0
    divide_calc = DivideCalculation(a, b)

    with pytest.raises(ZeroDivisionError) as exc_info:
        divide_calc.execute()

    assert str(exc_info.value) == "Cannot divide by zero."

def test_factory_creates_add_calculation():
    a = 4.0
    b = 3.0
    calc = CalculationFactory.create_calculation('add', a, b)

    assert isinstance(calc, AddCalculation)
    assert calc.a == a
    assert calc.b == b

def test_factory_creates_subtract_calculation():
    a = 4.0
    b = 3.0
    calc = CalculationFactory.create_calculation('subtract', a, b)

    assert isinstance(calc, SubtractCalculation)
    assert calc.a == a
    assert calc.b == b

def test_factory_creates_multiply_calculation():
    a = 5.0
    b = 6.0
    calc = CalculationFactory.create_calculation('multiply', a, b)

    assert isinstance(calc, MultiplyCalculation)
    assert calc.a == a
    assert calc.b == b

def test_factory_creates_divide_calculation():
    a = 10.0
    b = 5.0
    calc = CalculationFactory.create_calculation('divide', a, b)

    assert isinstance(calc, DivideCalculation)
    assert calc.a == a
    assert calc.b == b

def test_factory_create_unsupported_calculation():
    a = 15.0
    b = 5.0 
    unsupported_type = 'modulus'

    with pytest.raises(ValueError) as exc_info:
        CalculationFactory.create_calculation(unsupported_type, a, b)

    assert f"Unsupported calculation type: '{unsupported_type}'" in str(exc_info.value)

def test_factory_register_calculation_duplicate():
    with pytest.raises(ValueError) as exc_info:
        @CalculationFactory.register_calculation('add')
        class AnotherAddCalculation(Calculation):
            def execute(self) -> float:
                return Operation.addition(self.a, self.b)
            
    assert "Calculation type 'add' is already registered." in str(exc_info)

@patch.object(Operation, 'addition', return_value=7.0)
def test_calculation_str_representation_addition(mock_addition):
    a = 3.0
    b = 4.0
    add_calc = AddCalculation(a, b)

    calc_str = str(add_calc)
    expected_str = f"{add_calc.__class__.__name__}: {a} Add {b} = 7.0"
    assert calc_str == expected_str

@patch.object(Operation, 'subtraction', return_value=9.0)
def test_calculation_str_representation_subtraction(mock_subtraction):
    a = 18.0
    b = 9.0
    subtract_calc = SubtractCalculation(a, b)

    calc_str = str(subtract_calc)
    expected_str = f"{subtract_calc.__class__.__name__}: {a} Subtract {b} = 9.0"
    assert calc_str == expected_str

@patch.object(Operation, 'multiplication', return_value=45.0)
def test_calution_str_representation_multiplication(mock_multiplication):
    a = 5.0
    b = 9.0
    multiply_calc = MultiplyCalculation(a, b)

    calc_str = str(multiply_calc)
    expected_str = f"{multiply_calc.__class__.__name__}: {a} Multiply {b} = 45.0"
    assert calc_str == expected_str

@patch.object(Operation, 'division', return_value=2.0)
def test_calculation_str_representation_division(mock_division):
    a = 12.0
    b = 6.0
    divide_calc = DivideCalculation(a, b)

    calc_tr = str(divide_calc)
    expected_str = f"{divide_calc.__class__.__name__}: {a} Divide {b} = 2.0"
    assert calc_tr == expected_str

def test_calculation_repr_representation_subtraction():
    a = 10.0
    b = 5.0
    subtract_calc = SubtractCalculation(a, b)

    calc_repr = repr(subtract_calc)
    expected_repr = f"{SubtractCalculation.__name__}(a={a}, b={b})"
    assert calc_repr == expected_repr

def test_calculation_repr_representation_division():
    a = 15.0
    b = 5.0
    divide_calc = DivideCalculation(a, b)

    calc_repr = repr(divide_calc)
    expected_repr = f"{DivideCalculation.__name__}(a={a}, b={b})"
    assert calc_repr == expected_repr

# Parameterized Tests for Execute Method

@pytest.mark.parametrize("calc_type, a, b, expected_result", [
    ('add', 4.0, 6.0, 10.0),
    ('subtract', 7.0, 3.0, 4.0),
    ('multiply', 6.0, 5.0, 30.0),
    ('divide', 15.0, 3.0, 5.0),
])
@patch.object(Operation, 'addition')
@patch.object(Operation, 'subtraction')
@patch.object(Operation, 'multiplication')
@patch.object(Operation, 'division')
def test_calculation_execute_parameterized(
    mock_division, mock_multiplication, mock_subtraction, mock_addition,
    calc_type, a, b, expected_result
):
    if calc_type == 'add':
        mock_addition.return_value = expected_result
    elif calc_type == 'subtract':
        mock_subtraction.return_value = expected_result
    elif calc_type == 'multiply':
        mock_multiplication.return_value = expected_result
    elif calc_type == 'divide':
        mock_division.return_value = expected_result
    
    calc = CalculationFactory.create_calculation(calc_type, a, b)
    result = calc.execute()

    if calc_type == 'add':
        mock_addition.assert_called_once_with(a, b)
    elif calc_type == 'subtract':
        mock_subtraction.assert_called_once_with(a, b)
    elif calc_type == 'multiply':
        mock_multiplication.assert_called_once_with(a, b)
    elif calc_type == 'divide':
        mock_division.assert_called_once_with(a, b)
    
    assert result == expected_result