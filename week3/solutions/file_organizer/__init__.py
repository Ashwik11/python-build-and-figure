"""Organize files into extension-based category folders."""

from .exceptions import (
    DestinationFolderError,
    FileMovementError,
    FileOrganizerError,
    UnsupportedFileError,
)
from .file_detector import EXTENSION_CATEGORIES, detect_category
from .file_mover import choose_available_path, move_file, prepare_destination
from .logging_config import configure_logging
from .organizer import organize_folder

__all__ = [
    "DestinationFolderError",
    "EXTENSION_CATEGORIES",
    "FileMovementError",
    "FileOrganizerError",
    "UnsupportedFileError",
    "choose_available_path",
    "configure_logging",
    "detect_category",
    "move_file",
    "organize_folder",
    "prepare_destination",
]

