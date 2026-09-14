"""Run the menu-driven application activity logger."""

from pathlib import Path
import sys


if __package__ in (None, ""):
    package_parent = Path(__file__).resolve().parent.parent
    sys.path.insert(0, str(package_parent))

from application_activity_logger.auth import login, logout
from application_activity_logger.calculator import calculate
from application_activity_logger.exceptions import ActivityError
from application_activity_logger.file_operations import read_file, write_file
from application_activity_logger.logging_config import configure_logging


MENU = """
Application Activity Logger
1. Login
2. Calculate
3. Read a File
4. Write a File
5. Logout
"""


def _require_login(current_user, logger):
    """Raise a recoverable error when an activity requires login."""
    if current_user is None:
        logger.warning("Protected activity attempted before login.")
        raise ActivityError("Please log in before selecting this activity.")


def run_application(input_func=input, output_func=print, logs_directory=None):
    """Run the menu loop and continue after recoverable operation errors."""
    logger = configure_logging(logs_directory)
    logger.debug("Application started.")
    current_user = None

    while True:
        try:
            output_func(MENU)
            choice = input_func("Choose an activity (1-5): ").strip()
            logger.debug("Menu choice %r received.", choice)

            if choice == "1":
                username = input_func("Username: ")
                password = input_func("Password: ")
                current_user = login(username, password, logger)
                output_func(f"Welcome, {current_user}!")

            elif choice == "2":
                _require_login(current_user, logger)
                first_value = input_func("First number: ")
                second_value = input_func("Second number: ")
                operator = input_func("Operator (+, -, *, /): ")
                result = calculate(first_value, second_value, operator, logger)
                output_func(f"Result: {result}")

            elif choice == "3":
                _require_login(current_user, logger)
                file_path = input_func("File to read: ")
                content = read_file(file_path, logger)
                output_func(f"File contents:\n{content}")

            elif choice == "4":
                _require_login(current_user, logger)
                file_path = input_func("File to write: ")
                content = input_func("Text to write: ")
                saved_path = write_file(file_path, content, logger)
                output_func(f"Saved: {saved_path}")

            elif choice == "5":
                logout(current_user, logger)
                output_func("Goodbye!")
                break

            else:
                logger.warning("Invalid menu choice %r.", choice)
                output_func("Invalid choice. Enter a number from 1 to 5.")

        except ActivityError as error:
            logger.error("Activity failed: %s: %s", type(error).__name__, error)
            output_func(f"Operation failed: {error}")
            continue
        except (EOFError, KeyboardInterrupt):
            logger.warning("Application input was interrupted.")
            output_func("\nInput interrupted. Closing the application.")
            break
        except Exception as error:
            logger.critical(
                "Unexpected application failure: %s: %s",
                type(error).__name__,
                error,
                exc_info=True,
            )
            output_func("An unexpected error occurred. You may continue.")
            continue

    logger.debug("Application ended.")


def main():
    """Start the interactive application."""
    run_application()


if __name__ == "__main__":
    main()
