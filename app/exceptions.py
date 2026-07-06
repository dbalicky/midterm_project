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