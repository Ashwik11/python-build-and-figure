"""Custom exceptions for student-data and result-processing errors."""


class StudentProcessingError(Exception):
    """Base exception for errors raised while processing a student."""


class InvalidMarksError(StudentProcessingError):
    """Raised when marks are missing, non-numeric, or outside 0 to 100."""


class MissingStudentInformationError(StudentProcessingError):
    """Raised when required student information is missing."""


class ResultCalculationError(StudentProcessingError):
    """Raised when a result cannot be calculated safely."""

