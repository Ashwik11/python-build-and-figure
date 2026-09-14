"""Logging configuration for successful and failed file operations."""

import logging
from pathlib import Path


LOGGER_NAME = "file_organizer"


def configure_logging(log_file=None):
    """Create and return the file-organizer logger."""
    if log_file is None:
        logs_directory = Path(__file__).parent / "logs"
        log_file = logs_directory / "file_organizer.log"
    else:
        log_file = Path(log_file)
        logs_directory = log_file.parent

    logs_directory.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    for existing_handler in logger.handlers[:]:
        existing_handler.close()
        logger.removeHandler(existing_handler)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.debug("File-organizer logging configured.")
    return logger

