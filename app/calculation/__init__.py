from abc import ABC, abstractmethod
from app.operation import Operation

class Calculation(ABC):
    def __init__(self, a: float, b:float) -> None:
        self.a: float = a
        self.b: float = b

    @abstractmethod
    def execute(self) -> float:
        pass # pragma: no cover

    def __str__(self) -> str:
        result = self.execute()
        operation_name = self.__class__.__name__.replace('Calculation', '')
        return f"{self.__class__.__name__}: {self.a} {operation_name} {self.b} = {result}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"
    
class CalculationFactory:
    _calculations = {}

    """
    Register a new calculation type.
    @param calculation_type: The type of calculation (e.g., 'add', 'subtract').
    @return: A decorator that registers the calculation class.
    @raises ValueError: If the calculation type is already registered.
    """
    @classmethod
    def register_calculation(cls, calculation_type: str):
        def decorator(subclass):
            calculation_type_lower = calculation_type.lower()
            if calculation_type_lower in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            cls._calculations[calculation_type_lower] = subclass
            return subclass
        return decorator
        
    """
    Create a calculation instance based on the type and operands.
    @param calculation_type: The type of calculation to create (e.g., 'add', 'subtract').
    @param a: The first operand.
    @param b: The second operand.
    @return: An instance of the corresponding Calculation subclass.
    @raises ValueError: If the calculation type is not supported.
    @raises ZeroDivisionError: If division by zero is attempted.
    """
    @classmethod
    def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:
        calculation_type_lower = calculation_type.lower()
        calculation_class = cls._calculations.get(calculation_type_lower)

        if not calculation_class:
            available_types = ', '.join(cls._calculations.keys())
            raise ValueError(f"Unsupported calculation type: '{calculation_type}'. Available types: {available_types}")
        
        return calculation_class(a,b)
    
@CalculationFactory.register_calculation('add')
class AddCalculation(Calculation):
    """
    Addition calculation.
    """
    def execute(self) -> float:
        return Operation.addition(self.a, self.b)
    
@CalculationFactory.register_calculation('subtract')
class SubtractCalculation(Calculation):
    """
    Subtraction calculation.
    """
    def execute(self) -> float:
        return Operation.subtraction(self.a, self.b)
    
@CalculationFactory.register_calculation('multiply')
class MultiplyCalculation(Calculation):
    """
    Multiplication calculation.
    """
    def execute(self) -> float:
        return Operation.multiplication(self.a,self.b)

@CalculationFactory.register_calculation('divide')
class DivideCalculation(Calculation):
    """
    Division calculation.
    """
    def execute(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Operation.division(self.a, self.b)