"""Create destination folders and move files without overwriting duplicates."""

from pathlib import Path
import shutil

from .exceptions import DestinationFolderError, FileMovementError


def prepare_destination(destination_root, category, logger):
    """Create and return the category destination folder when necessary."""
    root = Path(destination_root)

    if root.exists() and not root.is_dir():
        logger.error("Destination root is not a directory: %s.", root)
        raise DestinationFolderError(f"Destination is not a folder: {root}")

    try:
        if not root.exists():
            logger.warning("Destination folder was missing; creating %s.", root)
            root.mkdir(parents=True, exist_ok=True)

        category_directory = root / category
        if not category_directory.exists():
            logger.warning(
                "Category folder was missing; creating %s.",
                category_directory,
            )
            category_directory.mkdir(parents=True, exist_ok=True)
    except PermissionError as error:
        logger.error("Permission denied while creating destination %s.", root)
        raise DestinationFolderError(
            f"Permission denied while creating destination: {root}"
        ) from error
    except OSError as error:
        logger.error("Could not prepare destination %s: %s.", root, error)
        raise DestinationFolderError(
            f"Could not prepare destination folder: {root}"
        ) from error

    return category_directory


def choose_available_path(destination_path, logger):
    """Return a non-existing destination path for a duplicate filename."""
    path = Path(destination_path)
    if not path.exists():
        return path

    counter = 1
    while True:
        candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        if not candidate.exists():
            logger.warning(
                "Duplicate filename %s detected; using %s.",
                path.name,
                candidate.name,
            )
            return candidate
        counter += 1


def move_file(file_path, destination_root, category, logger):
    """Move one file into its category folder and return the final path."""
    source = Path(file_path)
    if not source.exists():
        logger.error("Cannot move missing file: %s.", source)
        raise FileNotFoundError(f"File does not exist: {source}")
    if not source.is_file():
        logger.error("Cannot move a path that is not a file: %s.", source)
        raise FileMovementError(f"Source is not a file: {source}")

    category_directory = prepare_destination(destination_root, category, logger)
    destination = choose_available_path(category_directory / source.name, logger)

    try:
        shutil.move(str(source), str(destination))
    except PermissionError as error:
        logger.error("Permission denied while moving %s to %s.", source, destination)
        raise FileMovementError(f"Permission denied while moving: {source}") from error
    except OSError as error:
        logger.error("Failed to move %s to %s: %s.", source, destination, error)
        raise FileMovementError(f"Could not move file: {source}") from error

    logger.info("Moved %s to %s successfully.", source, destination)
    return destination

