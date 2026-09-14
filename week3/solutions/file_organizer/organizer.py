"""Coordinate file detection and movement for an entire folder."""

from pathlib import Path

from .exceptions import FileOrganizerError
from .file_detector import detect_category
from .file_mover import move_file
from .logging_config import configure_logging


def organize_folder(source_folder, destination_root, logger=None):
    """Organize supported files and continue after individual file failures."""
    if logger is None:
        logger = configure_logging()

    source = Path(source_folder)
    destination = Path(destination_root)
    summary = {"moved": [], "skipped": [], "failed": []}

    if not source.exists():
        logger.error("Source folder does not exist: %s.", source)
        raise FileNotFoundError(f"Source folder does not exist: {source}")
    if not source.is_dir():
        logger.error("Source path is not a folder: %s.", source)
        raise NotADirectoryError(f"Source path is not a folder: {source}")

    logger.info("Starting organization from %s into %s.", source, destination)
    files = [path for path in source.iterdir() if path.is_file()]

    for file_path in files:
        try:
            category = detect_category(file_path, logger)
            final_path = move_file(file_path, destination, category, logger)
            summary["moved"].append(final_path)
        except FileOrganizerError as error:
            logger.error(
                "Skipped %s: %s: %s.",
                file_path,
                type(error).__name__,
                error,
            )
            summary["skipped"].append(file_path)
            continue
        except (FileNotFoundError, PermissionError, OSError) as error:
            logger.error(
                "Failed to process %s: %s: %s.",
                file_path,
                type(error).__name__,
                error,
            )
            summary["failed"].append(file_path)
            continue

    logger.info(
        "Organization completed: %s moved, %s skipped, %s failed.",
        len(summary["moved"]),
        len(summary["skipped"]),
        len(summary["failed"]),
    )
    return summary

