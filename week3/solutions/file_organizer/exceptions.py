"""Custom exceptions for file-organization failures."""


class FileOrganizerError(Exception):
    """Base exception for recoverable file-organizer errors."""


class UnsupportedFileError(FileOrganizerError):
    """Raised when a file extension has no configured category."""


class DestinationFolderError(FileOrganizerError):
    """Raised when a destination folder cannot be used or created."""


class FileMovementError(FileOrganizerError):
    """Raised when a file cannot be moved safely."""

