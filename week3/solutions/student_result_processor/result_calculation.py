"""Functions for calculating student totals, percentages, grades, and status."""

from numbers import Real

from .exceptions import ResultCalculationError


MAX_MARKS_PER_SUBJECT = 100
PASS_MARK_PER_SUBJECT = 40
REQUIRED_SUBJECT_COUNT = 5


def calculate_total(marks):
    """Return the sum of a student's subject marks."""
    if not marks:
        raise ResultCalculationError("Marks are required to calculate a total.")
    try:
        return sum(marks)
    except (TypeError, ValueError, ArithmeticError) as error:
        raise ResultCalculationError("Unable to calculate the total marks.") from error


def calculate_percentage(total, subject_count, max_marks_per_subject=100):
    """Return the percentage for a total and number of subjects."""
    numeric_values = (total, subject_count, max_marks_per_subject)
    if any(isinstance(value, bool) or not isinstance(value, Real) for value in numeric_values):
        raise ResultCalculationError("Percentage inputs must be numeric.")

    try:
        maximum_total = subject_count * max_marks_per_subject
        if maximum_total <= 0:
            raise ZeroDivisionError("Maximum total must be greater than zero.")
        return (total / maximum_total) * 100
    except (TypeError, ValueError, ArithmeticError, ZeroDivisionError) as error:
        raise ResultCalculationError("Unable to calculate the percentage.") from error


def determine_grade(percentage):
    """Return a letter grade for a validated percentage."""
    if isinstance(percentage, bool) or not isinstance(percentage, Real):
        raise ResultCalculationError("Percentage must be numeric.")
    if not 0 <= percentage <= 100:
        raise ResultCalculationError("Percentage must be between 0 and 100.")

    if percentage >= 90:
        return "A"
    if percentage >= 80:
        return "B"
    if percentage >= 70:
        return "C"
    if percentage >= 60:
        return "D"
    if percentage >= 40:
        return "E"
    return "F"


def determine_status(marks, pass_mark=PASS_MARK_PER_SUBJECT):
    """Return Pass only when every subject mark meets the pass mark."""
    if not marks:
        raise ResultCalculationError("Marks are required to determine status.")
    try:
        return "Pass" if all(mark >= pass_mark for mark in marks) else "Fail"
    except (TypeError, ValueError) as error:
        raise ResultCalculationError("Unable to determine pass/fail status.") from error


def calculate_result(student):
    """Calculate and return the complete result for one validated student."""
    try:
        marks = student["marks"]
        if len(marks) != REQUIRED_SUBJECT_COUNT:
            raise ResultCalculationError(
                f"Exactly {REQUIRED_SUBJECT_COUNT} subject marks are required."
            )
        total = calculate_total(marks)
        percentage = calculate_percentage(
            total,
            subject_count=len(marks),
            max_marks_per_subject=MAX_MARKS_PER_SUBJECT,
        )
        status = determine_status(marks)
        grade = determine_grade(percentage) if status == "Pass" else "F"
    except ResultCalculationError:
        raise
    except (KeyError, TypeError, ValueError, ArithmeticError) as error:
        raise ResultCalculationError("Unable to calculate the student result.") from error

    return {
        "student_id": student["student_id"],
        "name": student["name"],
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status,
    }
