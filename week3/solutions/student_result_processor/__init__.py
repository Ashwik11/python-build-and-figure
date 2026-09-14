"""Fault-tolerant tools for processing student examination results."""

from .exceptions import (
    InvalidMarksError,
    MissingStudentInformationError,
    ResultCalculationError,
    StudentProcessingError,
)
from .logging_config import configure_logging
from .result_calculation import (
    calculate_percentage,
    calculate_result,
    calculate_total,
    determine_grade,
    determine_status,
)
from .student_operations import (
    create_student,
    parse_mark,
    read_students_from_csv,
    student_from_row,
)

__all__ = [
    "InvalidMarksError",
    "MissingStudentInformationError",
    "ResultCalculationError",
    "StudentProcessingError",
    "calculate_percentage",
    "calculate_result",
    "calculate_total",
    "configure_logging",
    "create_student",
    "determine_grade",
    "determine_status",
    "parse_mark",
    "read_students_from_csv",
    "student_from_row",
]

