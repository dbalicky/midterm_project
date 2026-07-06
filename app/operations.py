from abc import ABC, abstractmethod
from decimal import Decimal as DEC
from typing import Dict
from exceptions import ValidationError


class Operation(ABC):
    """
    This is the Abstract Base Class for creating calculator operations.

    Each operation subclass must implement the abstract execute method from this class.
    """

    @abstractmethod
    def execute(self, x: DEC, y: DEC) -> DEC:
        """
        Abstract method for executing the operation.

        The operation is performed on the two operands:
        decimal 'x' as the first operand, and decimal 'y' as the second.

        The method returns the result of the operation.

        If the operation fails, an exception is raised.
        """
        pass #pragma: no cover

    def validate_operands(self, x: DEC, y: DEC) -> None:
        """
        This method validates the two operands 'x' and 'y'.
        
        It is not an abstract method, so subclasses can override it depending on the operation.

        If the operands are invalid, this method raises a ValidationError.
        """
        pass

    def __str__(self) -> str:
        """
        This method returns the operation name as a string
        so it can be displayed in the output.
        """

        return self.__class__.__name__
    

class Addition(Operation):
    """
    Addition subclass.

    Performs an addition operation on two Decimal operands.
    """

    def execute(self, x: DEC, y: DEC) -> DEC:
        """
        Executes the addition operation.

        Validates the operands x and y.

        Raises ValidationError if validation fails.

        If validation succeeds, returns the sum of x and y.
        """
        self.validate_operands(x,y)
        return x + y
    
class Subtraction(Operation):
    """
    Subtraction subclass.

    Performs a subtraction operation on two Decimal operands.
    """

    def execute(self, x: DEC, y: DEC) -> DEC:
        """
        Executes the subtraction operation.

        Validates the operands x and y.
        
        Raises ValidationError if validation fails.

        If validation succeeds, returns the difference of x and y.
        """
        self.validate_operands(x,y)
        return x - y
    
class Multiplication(Operation):
    """
    Multiplication subclass.

    Performs a multiplication operation on two Decimal operands.
    """

    def execute(self, x: DEC, y: DEC) -> DEC:
        """
        Executes the multiplication operation.

        Validates the operands x and y.
        
        Raises ValidationError if validation fails.

        If validation succeeds, returns the product of x and y.
        """
        self.validate_operands(x,y)
        return x * y
    
class Division(Operation):
    """
    Division subclass.

    Performs a division operation on two Decimal operands.
    """

    def validate_operands(self, x: DEC, y: DEC) -> None:
        """
        Overrides validate_operands method from base class.

        Raises ValidationError if divisor (operand y) is zero.
        """
        super().validate_operands(x, y)
        if y == 0:
            raise ValidationError("Error: Cannot divide by zero")
        
    def execute(self, x: DEC, y: DEC) -> DEC:
        """
        Executes the division operation.

        Validates the operands x and y.
        
        Raises ValidationError if validation fails.

        If validation succeeds, returns the quotent of x and y.
        """
        self.validate_operands(x,y)
        return x / y
    
class Power(Operation):
    """
    Power subclass.

    Performs an exponentiation operation on two Decimal operands.
    """
    def validate_operands(self, x: DEC, y: DEC) -> None:
        """
        Overrides validate_operands method from base class.

        Raises ValidationError if base (operand x) is 0 and exponent (operand y) is negative.
        """
        super().validate_operands(x, y)
        if x == 0 and y < 0:
            raise ValidationError("Error: Cannot raise zero to the power of a negative number")
        
    def execute(self, x: DEC, y: DEC) -> DEC:
        """
        Executes the power operation.

        Validates the operands x and y.
        
        Raises ValidationError if validation fails.

        If validation succeeds, returns the exponetiation of x and y.
        """
        self.validate_operands(x,y)
        return x ** y
    
class Root(Operation):
    """
    Root subclass.

    Performs a root operation on two Decimal operands.
    """
    def validate_operands(self, x: DEC, y: DEC) -> None:
        """
        Overrides validate_operands method from base class.

        Raises ValidationError if radicand x is negative or root degree y is zero.
        """
        super().validate_operands(x, y)
        if x < 0:
            raise ValidationError("Error: Cannot take the root of a negative number")
        if y == 0:
            raise ValidationError("Error: Zero root is undefined")
        
        
    def execute(self, x: DEC, y: DEC) -> DEC:
        """
        Executes the root operation.

        Validates the operands x and y.
        
        Raises ValidationError if validation fails.

        If validation succeeds, returns the y-th root of x.
        """
        self.validate_operands(x,y)
        return x ** (DEC("1") / y)
    
class Modulus(Operation):
    """
    Modulus subclass.

    Performs a modulus operation on two Decimal operands.
    """
    def validate_operands(self, x: DEC, y: DEC) -> None:
        """
        Overrides validate_operands method from base class.

        Raises ValidationError if divisor is 0.
        """
        super().validate_operands(x, y)
        if y == 0:
            raise ValidationError("Error: Cannot find remainder of a number divided by zero")
        
        
    def execute(self, x: DEC, y: DEC) -> DEC:
        """
        Executes the modulus operation.

        Validates the operands x and y.
        
        Raises ValidationError if validation fails.

        If validation succeeds, returns the remainder of operand x divided by operand y.
        """
        self.validate_operands(x,y)
        return x % y
    
class IntegerDivision(Operation):
    """
    Integer Division subclass.

    Performs an integer division operation on two Decimal operands.
    """
    def validate_operands(self, x: DEC, y: DEC) -> None:
        """
        Overrides validate_operands method from base class.

        Raises ValidationError if divisor is 0.
        """
        super().validate_operands(x, y)
        if y == 0:
            raise ValidationError("Error: Cannot divide by zero")
        
        
    def execute(self, x: DEC, y: DEC) -> DEC:
        """
        Executes the integer division operation.

        Validates the operands x and y.
        
        Raises ValidationError if validation fails.

        If validation succeeds, returns an integer quotient of operand x divided by operand y.
        """
        self.validate_operands(x,y)
        return DEC(int(x / y))
    
class Percentage(Operation):
    """
    Percentage calculation subclass.

    Performs a percentage calculation on two Decimal operands.
    """
    def validate_operands(self, x: DEC, y: DEC) -> None:
        """
        Overrides validate_operands method from base class.

        Raises ValidationError if divisor is 0.
        """
        super().validate_operands(x, y)
        if y == 0:
            raise ValidationError("Error: Cannot divide by zero")
        
        
    def execute(self, x: DEC, y: DEC) -> DEC:
        """
        Executes the percentage calucaltion operation.

        Validates the operands x and y.
        
        Raises ValidationError if validation fails.

        If validation succeeds, return the percentage of operand x divided by operand y.
        """
        self.validate_operands(x,y)
        return (x / y) * DEC("100")
    
class AbsoluteDifference(Operation):
    """
    Absolute difference subclass.

    Performs an absolute difference operation on two Decimal operands.
    """
    def execute(self, x: DEC, y: DEC) -> DEC:
        """
        Executes the asbolute difference operation.

        Validates the operands x and y.
        
        Raises ValidationError if validation fails.

        If validation succeeds, return the absolute difference of operand y subtracted from operand x.
        """
        self.validate_operands(x,y)
        return abs(x - y)