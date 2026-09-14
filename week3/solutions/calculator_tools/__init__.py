"""Reusable calculator functions for arithmetic, statistics, and conversions."""

from .arithmetic import (
    add,
    calculate,
    calculate_percentage,
    divide,
    multiply,
    percentage,
    subtract,
)
from .converter import (
    celsius_to_fahrenheit,
    convert_temperature,
    convert_unit,
    fahrenheit_to_celsius,
    kilograms_to_pounds,
    kilometers_to_miles,
    miles_to_kilometers,
    pounds_to_kilograms,
)
from .exceptions import InvalidOperationError
from .statistics import average, calculate_average

__all__ = [
    "InvalidOperationError",
    "add",
    "average",
    "calculate",
    "calculate_average",
    "calculate_percentage",
    "celsius_to_fahrenheit",
    "convert_temperature",
    "convert_unit",
    "divide",
    "fahrenheit_to_celsius",
    "kilograms_to_pounds",
    "kilometers_to_miles",
    "miles_to_kilometers",
    "multiply",
    "percentage",
    "pounds_to_kilograms",
    "subtract",
]

