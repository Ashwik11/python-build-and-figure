"""Logging configuration for the student result processor."""

import logging
from pathlib import Path


def configure_logging(log_file=None):
    """Create and return the application logger."""
    if log_file is None:
        log_file = Path(__file__).with_name("student_errors.log")
    else:
        log_file = Path(log_file)

    logger = logging.getLogger("student_result_processor")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    for existing_handler in logger.handlers[:]:
        existing_handler.close()
        logger.removeHandler(existing_handler)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
