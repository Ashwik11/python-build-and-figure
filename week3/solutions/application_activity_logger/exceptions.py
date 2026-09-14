"""Custom exceptions raised by application activities."""


class ActivityError(Exception):
    """Base exception for recoverable application activity errors."""


class AuthenticationError(ActivityError):
    """Raised when login information is invalid."""


class CalculationError(ActivityError):
    """Raised when a calculation cannot be completed."""


class FileActivityError(ActivityError):
    """Raised when a file activity cannot be completed."""

