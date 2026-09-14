"""Detect file categories from filename extensions."""

from pathlib import Path

from .exceptions import UnsupportedFileError


EXTENSION_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "Text": {".txt", ".md", ".rtf"},
    "Documents": {".pdf", ".doc", ".docx", ".ppt", ".pptx"},
    "Data": {".csv", ".json", ".xml", ".xls", ".xlsx"},
}


def detect_category(file_path, logger):
    """Return the configured category for an existing file."""
    path = Path(file_path)
    logger.debug("Detecting category for %s.", path)

    if not path.exists():
        logger.error("File does not exist: %s.", path)
        raise FileNotFoundError(f"File does not exist: {path}")
    if not path.is_file():
        logger.error("Path is not a file: %s.", path)
        raise IsADirectoryError(f"Path is not a file: {path}")

    extension = path.suffix.lower()
    for category, extensions in EXTENSION_CATEGORIES.items():
        if extension in extensions:
            logger.debug("Detected %s as category %s.", path.name, category)
            return category

    logger.error("Unsupported file type %r for %s.", extension or "no extension", path)
    raise UnsupportedFileError(
        f"Unsupported file type {extension or 'without an extension'}: {path.name}"
    )

