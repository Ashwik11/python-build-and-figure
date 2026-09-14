"""Arithmetic and percentage functions."""

from numbers import Real

from .exceptions import InvalidOperationError


def _validate_number(value, name):
    """Validate that a value is a real number but not a Boolean."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} must be an integer or float.")


def add(a, b):
    """Return the sum of two numbers."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    return a * b


def divide(a, b):
    """Return a divided by b."""
    _validate_number(a, "a")
    _validate_number(b, "b")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculate_percentage(part, whole):
    """Return part as a percentage of whole."""
    _validate_number(part, "part")
    _validate_number(whole, "whole")
    if whole == 0:
        raise ValueError("whole cannot be zero when calculating a percentage.")
    return (part / whole) * 100


def percentage(part, whole):
    """Return part as a percentage of whole."""
    return calculate_percentage(part, whole)


def calculate(a, b, operation):
    """Perform a supported arithmetic operation on two numbers."""
    if not isinstance(operation, str):
        raise TypeError("operation must be a string.")

    operations = {
        "+": add,
        "add": add,
        "-": subtract,
        "subtract": subtract,
        "*": multiply,
        "multiply": multiply,
        "/": divide,
        "divide": divide,
    }
    normalized_operation = operation.strip().lower()

    if normalized_operation not in operations:
        raise InvalidOperationError(
            f"Unsupported arithmetic operation: {operation!r}."
        )

    return operations[normalized_operation](a, b)

