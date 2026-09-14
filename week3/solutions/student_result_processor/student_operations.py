"""Functions for reading and validating student information."""

import csv
import math
from pathlib import Path

from .exceptions import InvalidMarksError, MissingStudentInformationError


SUBJECT_COLUMNS = ("subject1", "subject2", "subject3", "subject4", "subject5")
REQUIRED_COLUMNS = ("student_id", "name", *SUBJECT_COLUMNS)


def validate_required_text(value, field_name):
    """Return cleaned required text or raise an exception if it is missing."""
    if value is None or not str(value).strip():
        raise MissingStudentInformationError(f"{field_name} is required.")
    return str(value).strip()


def parse_mark(value, subject_name):
    """Convert one mark to a float and validate its allowed range."""
    if value is None or (isinstance(value, str) and not value.strip()):
        raise InvalidMarksError(f"{subject_name} mark is missing.")

    if isinstance(value, bool):
        raise InvalidMarksError(f"{subject_name} mark must be numeric.")

    try:
        mark = float(value)
    except (TypeError, ValueError) as error:
        raise InvalidMarksError(
            f"{subject_name} mark must be numeric; received {value!r}."
        ) from error

    if not math.isfinite(mark):
        raise InvalidMarksError(f"{subject_name} mark must be a finite number.")
    if not 0 <= mark <= 100:
        raise InvalidMarksError(
            f"{subject_name} mark must be between 0 and 100; received {mark}."
        )

    return mark


def create_student(student_id, name, marks):
    """Validate student fields and return a normalized student dictionary."""
    cleaned_id = validate_required_text(student_id, "student_id")
    cleaned_name = validate_required_text(name, "name")

    if not isinstance(marks, (list, tuple)):
        raise InvalidMarksError("marks must be supplied as a list or tuple.")
    if len(marks) != len(SUBJECT_COLUMNS):
        raise InvalidMarksError(
            f"Exactly {len(SUBJECT_COLUMNS)} subject marks are required."
        )

    cleaned_marks = [
        parse_mark(mark, f"subject{index}")
        for index, mark in enumerate(marks, start=1)
    ]

    return {
        "student_id": cleaned_id,
        "name": cleaned_name,
        "marks": cleaned_marks,
    }


def student_from_row(row):
    """Create a validated student dictionary from one CSV-style row."""
    if not isinstance(row, dict):
        raise MissingStudentInformationError("Each student record must be a dictionary.")

    missing_columns = [column for column in REQUIRED_COLUMNS if column not in row]
    if missing_columns:
        raise MissingStudentInformationError(
            "Missing required field(s): " + ", ".join(missing_columns)
        )

    marks = [row[column] for column in SUBJECT_COLUMNS]
    return create_student(row["student_id"], row["name"], marks)


def read_students_from_csv(file_path):
    """Read raw student rows from a CSV file."""
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"Student input file was not found: {path}")

    with path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames or []
        missing_columns = [column for column in REQUIRED_COLUMNS if column not in fieldnames]
        if missing_columns:
            raise MissingStudentInformationError(
                "CSV is missing required column(s): " + ", ".join(missing_columns)
            )
        return list(reader)

