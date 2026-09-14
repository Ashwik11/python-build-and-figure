"""Demonstrate the functionality provided by the calculator_tools package."""

from calculator_tools import (
    InvalidOperationError,
    add,
    average,
    calculate,
    calculate_percentage,
    celsius_to_fahrenheit,
    convert_temperature,
    convert_unit,
    divide,
    fahrenheit_to_celsius,
    kilograms_to_pounds,
    kilometers_to_miles,
    multiply,
    subtract,
)


def show_expected_error(label, action):
    """Run an action and display an expected exception without stopping the program."""
    try:
        action()
    except (InvalidOperationError, TypeError, ValueError, ZeroDivisionError) as error:
        print(f"{label}: {type(error).__name__} - {error}")


def main():
    """Run examples for every package requirement."""
    print("BASIC ARITHMETIC")
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))
    print("Dispatcher: 9 * 4 =", calculate(9, 4, "multiply"))

    print("\nPERCENTAGE AND AVERAGE")
    print("45 out of 60 =", calculate_percentage(45, 60), "%")
    print("Average of [80, 90, 70, 100] =", average([80, 90, 70, 100]))

    print("\nTEMPERATURE CONVERSION")
    print("25 C =", celsius_to_fahrenheit(25), "F")
    print("77 F =", fahrenheit_to_celsius(77), "C")
    print("0 C =", convert_temperature(0, "C", "F"), "F")

    print("\nSIMPLE UNIT CONVERSION")
    print("10 km =", round(kilometers_to_miles(10), 3), "miles")
    print("5 kg =", round(kilograms_to_pounds(5), 3), "pounds")
    print("10 miles =", round(convert_unit(10, "miles", "km"), 3), "km")

    print("\nERROR HANDLING")
    show_expected_error("Division by zero", lambda: divide(8, 0))
    show_expected_error("Incorrect data type", lambda: add("8", 2))
    show_expected_error("Invalid empty values", lambda: average([]))
    show_expected_error("Invalid temperature", lambda: celsius_to_fahrenheit(-300))
    show_expected_error("Unsupported arithmetic", lambda: calculate(2, 3, "power"))
    show_expected_error("Unsupported conversion", lambda: convert_unit(1, "meter", "liter"))


if __name__ == "__main__":
    main()

