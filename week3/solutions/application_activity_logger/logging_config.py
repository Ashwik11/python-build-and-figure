"""Configure application and error log files."""

import logging
from pathlib import Path


LOGGER_NAME = "application_activity_logger"


def configure_logging(logs_directory=None):
    """Create DEBUG and ERROR-level file handlers and return the logger."""
    if logs_directory is None:
        logs_directory = Path(__file__).parent / "logs"
    else:
        logs_directory = Path(logs_directory)

    logs_directory.mkdir(parents=True, exist_ok=True)
    application_log = logs_directory / "application.log"
    error_log = logs_directory / "error.log"

    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    for existing_handler in logger.handlers[:]:
        existing_handler.close()
        logger.removeHandler(existing_handler)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    application_handler = logging.FileHandler(
        application_log,
        mode="a",
        encoding="utf-8",
    )
    application_handler.setLevel(logging.DEBUG)
    application_handler.setFormatter(formatter)

    error_handler = logging.FileHandler(error_log, mode="a", encoding="utf-8")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    logger.addHandler(application_handler)
    logger.addHandler(error_handler)
    logger.debug("Logging configured successfully.")
    return logger

