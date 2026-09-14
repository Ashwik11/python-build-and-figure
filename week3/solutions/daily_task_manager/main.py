"""Start the Daily Task Manager command-line application."""

from pathlib import Path
import sys


if __package__ in (None, ""):
    package_parent = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(package_parent))

from daily_task_manager.cli import run_cli


def main():
    """Run the interactive task manager."""
    run_cli()


if __name__ == "__main__":
    main()

