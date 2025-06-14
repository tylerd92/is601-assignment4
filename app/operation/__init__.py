
class Operation:
    """
    parameters:
    @float: a
    @float: b
    returns float
    """
    @staticmethod
    def addition(a: float, b: float) -> float:
        return a + b
    
    """
    parameters:
    @float: a
    @float: b
    returns float
    """
    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        Finds the difference between numbers a and b and returns the result
        """
        return a - b

    """
    parameters:
    @float: a
    @float: b
    returns float
    """
    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        Calculates the product between numbers a and b and returns the result.
        """
        return a * b

    """
    parameters:
    @float: a
    @float: b
    returns float
    raises ValueError
    """
    @staticmethod
    def division(a: float, b: float) -> float:
        """
        Calculates the quotient between numbers a and b and returns the result.
        Before dividing a with b, there is a check if b is equal to zero. If b
        is zero the function raises a ValueError with a message saying
        "Division by zero is not allowed."
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b