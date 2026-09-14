"""Simple statistical functions."""

from numbers import Real


def average(values):
    """Return the arithmetic mean of a non-empty collection of numbers."""
    if isinstance(values, (str, bytes)):
        raise TypeError("values must be an iterable of numbers, not text.")

    try:
        numbers = list(values)
    except TypeError as error:
        raise TypeError("values must be an iterable of numbers.") from error

    if not numbers:
        raise ValueError("Cannot calculate the average of an empty collection.")

    for index, value in enumerate(numbers):
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError(f"Item at index {index} must be an integer or float.")

    return sum(numbers) / len(numbers)


def calculate_average(values):
    """Return the arithmetic mean of a non-empty collection of numbers."""
    return average(values)

