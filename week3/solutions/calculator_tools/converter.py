"""Temperature and simple unit-conversion functions."""

from numbers import Real

from .exceptions import InvalidOperationError


def _validate_number(value, name="value"):
    """Validate that a value is a real number but not a Boolean."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} must be an integer or float.")


def _validate_non_negative(value, name="value"):
    """Validate that a measurement is not negative."""
    _validate_number(value, name)
    if value < 0:
        raise ValueError(f"{name} cannot be negative for this conversion.")


def celsius_to_fahrenheit(celsius):
    """Convert degrees Celsius to degrees Fahrenheit."""
    _validate_number(celsius, "celsius")
    if celsius < -273.15:
        raise ValueError("Celsius temperature cannot be below absolute zero.")
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert degrees Fahrenheit to degrees Celsius."""
    _validate_number(fahrenheit, "fahrenheit")
    if fahrenheit < -459.67:
        raise ValueError("Fahrenheit temperature cannot be below absolute zero.")
    return (fahrenheit - 32) * 5 / 9


def convert_temperature(value, from_scale, to_scale):
    """Convert a temperature between Celsius and Fahrenheit."""
    if not isinstance(from_scale, str) or not isinstance(to_scale, str):
        raise TypeError("Temperature scales must be strings.")

    source = from_scale.strip().lower()
    target = to_scale.strip().lower()
    celsius_names = {"c", "celsius"}
    fahrenheit_names = {"f", "fahrenheit"}

    if source in celsius_names and target in fahrenheit_names:
        return celsius_to_fahrenheit(value)
    if source in fahrenheit_names and target in celsius_names:
        return fahrenheit_to_celsius(value)
    if source in celsius_names and target in celsius_names:
        _validate_number(value)
        if value < -273.15:
            raise ValueError("Celsius temperature cannot be below absolute zero.")
        return value
    if source in fahrenheit_names and target in fahrenheit_names:
        _validate_number(value)
        if value < -459.67:
            raise ValueError("Fahrenheit temperature cannot be below absolute zero.")
        return value

    raise InvalidOperationError(
        f"Unsupported temperature conversion: {from_scale!r} to {to_scale!r}."
    )


def kilometers_to_miles(kilometers):
    """Convert kilometers to miles."""
    _validate_non_negative(kilometers, "kilometers")
    return kilometers * 0.621371


def miles_to_kilometers(miles):
    """Convert miles to kilometers."""
    _validate_non_negative(miles, "miles")
    return miles / 0.621371


def kilograms_to_pounds(kilograms):
    """Convert kilograms to pounds."""
    _validate_non_negative(kilograms, "kilograms")
    return kilograms * 2.20462


def pounds_to_kilograms(pounds):
    """Convert pounds to kilograms."""
    _validate_non_negative(pounds, "pounds")
    return pounds / 2.20462


def convert_unit(value, from_unit, to_unit):
    """Convert supported distance or weight units."""
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Unit names must be strings.")

    aliases = {
        "km": "km",
        "kilometer": "km",
        "kilometers": "km",
        "mi": "mi",
        "mile": "mi",
        "miles": "mi",
        "kg": "kg",
        "kilogram": "kg",
        "kilograms": "kg",
        "lb": "lb",
        "lbs": "lb",
        "pound": "lb",
        "pounds": "lb",
    }
    source = aliases.get(from_unit.strip().lower())
    target = aliases.get(to_unit.strip().lower())
    conversions = {
        ("km", "mi"): kilometers_to_miles,
        ("mi", "km"): miles_to_kilometers,
        ("kg", "lb"): kilograms_to_pounds,
        ("lb", "kg"): pounds_to_kilograms,
    }

    if source is not None and source == target:
        _validate_non_negative(value)
        return value
    if (source, target) not in conversions:
        raise InvalidOperationError(
            f"Unsupported unit conversion: {from_unit!r} to {to_unit!r}."
        )

    return conversions[(source, target)](value)

