"""Calculation activity for the menu-driven application."""

from .exceptions import CalculationError


def _to_number(value, field_name, logger):
    """Convert user input to a float or raise a calculation error."""
    if isinstance(value, bool):
        logger.error("Boolean value supplied for %s.", field_name)
        raise CalculationError(f"{field_name} must be numeric.")

    try:
        return float(value)
    except (TypeError, ValueError) as error:
        logger.error("Non-numeric value %r supplied for %s.", value, field_name)
        raise CalculationError(f"{field_name} must be numeric.") from error


def calculate(first_value, second_value, operator, logger):
    """Perform addition, subtraction, multiplication, or division."""
    logger.debug(
        "Calculation requested with first=%r, second=%r, operator=%r.",
        first_value,
        second_value,
        operator,
    )

    first_number = _to_number(first_value, "First value", logger)
    second_number = _to_number(second_value, "Second value", logger)

    if not isinstance(operator, str):
        logger.error("Calculation operator must be text; received %r.", operator)
        raise CalculationError("Operator must be one of +, -, *, or /.")

    selected_operator = operator.strip()
    if selected_operator == "+":
        result = first_number + second_number
    elif selected_operator == "-":
        result = first_number - second_number
    elif selected_operator == "*":
        result = first_number * second_number
    elif selected_operator == "/":
        if second_number == 0:
            logger.error("Division by zero was attempted.")
            raise CalculationError("Cannot divide by zero.")
        result = first_number / second_number
    else:
        logger.warning("Unsupported calculation operator %r.", operator)
        raise CalculationError("Operator must be one of +, -, *, or /.")

    logger.info(
        "Calculation completed: %s %s %s = %s.",
        first_number,
        selected_operator,
        second_number,
        result,
    )
    return result

