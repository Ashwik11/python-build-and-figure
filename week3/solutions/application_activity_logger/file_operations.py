"""File-reading and file-writing activities."""

from pathlib import Path

from .exceptions import FileActivityError


def _validate_path(file_path, logger):
    """Return a Path for non-empty path input."""
    if file_path is None or not str(file_path).strip():
        logger.error("A file activity was attempted without a path.")
        raise FileActivityError("A file path is required.")
    return Path(str(file_path).strip())


def read_file(file_path, logger):
    """Read and return UTF-8 text from a file."""
    path = _validate_path(file_path, logger)
    logger.debug("Attempting to read file %s.", path)

    try:
        content = path.read_text(encoding="utf-8")
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError) as error:
        logger.error("File %s could not be opened: %s.", path, error)
        raise FileActivityError(f"Could not read file: {path}") from error

    if not content:
        logger.warning("File %s was empty.", path)
    else:
        logger.info("File %s was read successfully.", path)
    return content


def write_file(file_path, content, logger):
    """Write UTF-8 text to a file and return its path."""
    path = _validate_path(file_path, logger)
    logger.debug("Attempting to write file %s.", path)

    if not isinstance(content, str):
        logger.error("Non-text content supplied for file %s.", path)
        raise FileActivityError("File content must be text.")
    if not content:
        logger.warning("Empty content is being written to file %s.", path)

    try:
        path.write_text(content, encoding="utf-8")
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError) as error:
        logger.error("File %s could not be written: %s.", path, error)
        raise FileActivityError(f"Could not write file: {path}") from error

    logger.info("File %s was written successfully.", path)
    return path

