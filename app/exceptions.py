class CalculatorError(Exception):
    """
    This is the base class for exception errors with the calcutor.

    All the exception classes inherit from this class.
    """
    pass

class ValidationError(CalculatorError):
    """
    This exception is raised when the validation fails.

    Example inputs that raise the validation error include when a non-numeric
    value is entered, or when more arguments are given than allowed.
    """
    pass

class OperationError(CalculatorError):
    """
    This exception is raised when a calculation operation fails.
    
    Indivcates failures during execution of arithmetic operations, such 
    as dividing by zero or an invalid operation.
    """
    pass

class ConfigurationError(CalculatorError):
    """
    This exception is raised when the configuration of the calculator is invalid.

    Examples that raise this error include invalid directory paths or
    faulty configuration values.
    """
    pass