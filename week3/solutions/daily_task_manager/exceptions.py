"""Custom exceptions used by the daily task manager."""


class TaskManagerError(Exception):
    """Base exception for recoverable task-manager errors."""


class TaskValidationError(TaskManagerError):
    """Raised when task information is invalid."""


class TaskNotFoundError(TaskManagerError):
    """Raised when a requested task ID does not exist."""


class StorageError(TaskManagerError):
    """Raised when task data cannot be loaded or saved."""

