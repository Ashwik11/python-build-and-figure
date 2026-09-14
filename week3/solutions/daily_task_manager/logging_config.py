"""Logging configuration for task-manager activities and failures."""

import logging
from pathlib import Path


LOGGER_NAME = "daily_task_manager"


def configure_logging(log_file=None):
    """Create and return a DEBUG-level file logger."""
    if log_file is None:
        log_file = Path(__file__).parent / "logs" / "task_manager.log"
    else:
        log_file = Path(log_file)

    log_file.parent.mkdir(parents=True, exist_ok=True)
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
    handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug("Task-manager logging configured.")
    return logger

