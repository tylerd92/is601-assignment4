import pytest
from io import StringIO

from app.calculator import display_help, display_history, calculator

def test_display_help(capsys):
    display_help()

    captured = capsys.readouterr()
    expected_output = """
Calculator REPL Help
--------------------
Usage:
    <operation> <number1> <number2>
    - Perform a calculation with the specified operation and two numbers.
    - Supported operations:
        add       : Adds two numbers.
        subtract  : Subtracts the second number from the first.
        multiply  : Multiplies two numbers.
        divide    : Divides the first number by the second.

Special Commands:
    help      : Display this help message.
    history   : Show the history of calculations.
    exit      : Exit the calculator.

Examples:
    add 10 5
    subtract 15.5 3.2
    multiply 7 8
    divide 20 4
"""
    assert captured.out.strip() == expected_output.strip()

def test_display_history_empty(capsys):
    history = []
    display_history(history)

    captured = capsys.readouterr()
    assert captured.out.strip() == "No calculations performed yet."

def test_display_history_with_entries(capsys):
    history = [
        "AddCalculation: 4.0 Add 6.0 = 10.0",
        "SubtractCalculation: 7.0 Subtract 3.0 = 4.0",
        "MultiplyCalculation: 6.0 Multiply 5.0 = 30.0",
        "DivideCalculation: 15.0 Divide 3.0 = 5.0"
    ]

    display_history(history)

    captured = capsys.readouterr()
    expected_output = """Calculation History:
1. AddCalculation: 4.0 Add 6.0 = 10.0
2. SubtractCalculation: 7.0 Subtract 3.0 = 4.0
3. MultiplyCalculation: 6.0 Multiply 5.0 = 30.0
4. DivideCalculation: 15.0 Divide 3.0 = 5.0"""
    assert captured.out.strip() == expected_output.strip()

def test_calculator_exit(monkeypatch, capsys):
    user_input = 'exit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Exiting calculator. Goodbye!" in captured.out
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 0

def test_calculator_help_command(monkeypatch, capsys):
    user_input = 'help\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Calculator REPL Help" in captured.out
    assert "Exiting calculator. Goodbye!" in captured.out

def test_calculator_invalid_input(monkeypatch, capsys):
    user_input = 'invalid input\nadd 5\nsubtract\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Invalid input. Please follow the format: <operation> <num1> <num2>" in captured.out
    assert "Type 'help' for more information." in captured.out

def test_calculator_addition(monkeypatch, capsys):
    user_input = 'add 2 3\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Result: AddCalculation: 2.0 Add 3.0 = 5.0" in captured.out

def test_calculator_subtraction(monkeypatch, capsys):
    user_input = 'subtract 10 7\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Result: SubtractCalculation: 10.0 Subtract 7.0 = 3.0" in captured.out

def test_calculator_multiplication(monkeypatch, capsys):
    user_input = 'multiply 8 3\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Result: MultiplyCalculation: 8.0 Multiply 3.0 = 24.0" in captured.out

def test_calculation_division(monkeypatch, capsys):
    user_input = 'divide 12 2\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Result: DivideCalculation: 12.0 Divide 2.0 = 6.0" in captured.out
    
def test_calculation_division_by_zero(monkeypatch, capsys):
    user_input = 'divide 4 0\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "Cannot divide by zero." in captured.out

def test_calculator_history(monkeypatch, capsys):
    user_input = 'add 5 4\nsubtract 10 3\nhistory\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Result: AddCalculation: 5.0 Add 4.0 = 9.0" in captured.out
    assert "Result: SubtractCalculation: 10.0 Subtract 3.0 = 7.0" in captured.out
    assert "Calculation History:" in captured.out
    assert "1. AddCalculation: 5.0 Add 4.0 = 9.0" in captured.out
    assert "2. SubtractCalculation: 10.0 Subtract 3.0 = 7.0" in captured.out

def test_calculator_invalid_number_input(monkeypatch, capsys):
    user_input = 'add five four\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Invalid input. Please ensure numbers are valid." in captured.out or \
           "could not convert string to float: 'ten'" in captured.out or \
           "Invalid input. Please follow the format: <operation> <num1> <num2>" in captured.out
    
def test_calculator_unsupported_operation(monkeypatch, capsys):
    user_input = 'modulus 4 2\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit) as exc_info:
        calculator()

    captured = capsys.readouterr()
    assert "Unsupported calculation type: 'modulus'." in captured.out
    assert "Type 'help' to see the list of supported operations." in captured.out

def test_calculator_keyboard_interrupt(monkeypatch, capsys):
    def mock_input(prompt):
        raise KeyboardInterrupt()
    monkeypatch.setattr('builtins.input', mock_input)

    with pytest.raises(SystemExit) as exc_info:
        calculator()
    
    captured = capsys.readouterr()
    assert "\nKeyboard interrupt detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0

def test_calculator_eof_error(monkeypatch, capsys):
    def mock_input(prompt):
        raise EOFError()
    monkeypatch.setattr('builtins.input', mock_input)

    with pytest.raises(SystemExit) as exc_info:
        calculator()
    
    captured = capsys.readouterr()
    assert "\nEOF detected. Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0
    
def test_calculator_unexpected_exception(monkeypatch, capsys):
    class MockCalculation:
        def execute(self):
            raise Exception("Mock exception during execution")
        def __str__(self):
            return "MockCalculation"

    def mock_create_calculation(operation, a, b):
        return MockCalculation()

    monkeypatch.setattr('app.calculation.CalculationFactory.create_calculation', mock_create_calculation)
    user_input = 'add 9 6\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    with pytest.raises(SystemExit):
        calculator()

    captured = capsys.readouterr()
    assert "An error occurred during calculation: Mock exception during execution" in captured.out
    assert "Please try again." in captured.out