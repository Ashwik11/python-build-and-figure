"""Command-line entry point for the extension-based file organizer."""

import argparse
from pathlib import Path
import sys


if __package__ in (None, ""):
    package_parent = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(package_parent))

from file_organizer.logging_config import configure_logging
from file_organizer.organizer import organize_folder


def build_parser():
    """Create the command-line argument parser."""
    package_directory = Path(__file__).parent
    parser = argparse.ArgumentParser(
        description="Organize files into folders based on their extensions."
    )
    parser.add_argument(
        "source",
        nargs="?",
        default=package_directory / "sample_files",
        help="Folder containing files to organize.",
    )
    parser.add_argument(
        "destination",
        nargs="?",
        default=package_directory / "organized_files",
        help="Root folder that will contain category folders.",
    )
    return parser


def main():
    """Parse arguments, organize the folder, and display a summary."""
    arguments = build_parser().parse_args()
    logger = configure_logging()

    try:
        summary = organize_folder(arguments.source, arguments.destination, logger)
    except (FileNotFoundError, NotADirectoryError, PermissionError, OSError) as error:
        logger.critical("The organizer could not start: %s: %s.", type(error).__name__, error)
        print(f"Organizer could not start: {error}")
        return

    print(f"Moved: {len(summary['moved'])}")
    print(f"Skipped: {len(summary['skipped'])}")
    print(f"Failed: {len(summary['failed'])}")
    print(f"Log: {Path(__file__).parent / 'logs' / 'file_organizer.log'}")


if __name__ == "__main__":
    main()

