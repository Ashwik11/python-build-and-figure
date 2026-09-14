"""Interactive command-line interface for the daily task manager."""

from pathlib import Path

from .exceptions import StorageError, TaskManagerError
from .logging_config import configure_logging
from .storage import TaskStore
from .task_service import TaskManager


MENU = """
Daily Task Manager
1. Add Task
2. List Tasks
3. Complete Task
4. Delete Task
5. Exit
"""


def _read_task_id(raw_value):
    """Convert menu input to a positive integer task ID."""
    try:
        task_id = int(raw_value)
    except (TypeError, ValueError) as error:
        raise ValueError("Task ID must be a number.") from error
    if task_id < 1:
        raise ValueError("Task ID must be greater than zero.")
    return task_id


def _format_task(task):
    """Return one task as a readable CLI line."""
    status = "Done" if task.completed else "Pending"
    due_text = task.due_date or "No due date"
    return f"[{task.task_id}] {task.title} | {status} | Due: {due_text}"


def run_cli(input_func=input, output_func=print, data_file=None, log_file=None):
    """Run the menu loop and return the final TaskManager when it closes."""
    package_directory = Path(__file__).parent
    if data_file is None:
        data_file = package_directory / "data" / "tasks.json"

    logger = configure_logging(log_file)
    logger.info("Daily Task Manager started.")

    try:
        try:
            manager = TaskManager(TaskStore(data_file, logger), logger)
        except StorageError as error:
            logger.critical("Application could not load task data: %s", error)
            output_func(f"Could not start: {error}")
            return None

        while True:
            try:
                output_func(MENU)
                choice = input_func("Choose an option (1-5): ").strip()
                logger.debug("Menu choice %r received.", choice)

                if choice == "1":
                    title = input_func("Task title: ")
                    due_date = input_func("Due date YYYY-MM-DD (optional): ")
                    task = manager.add_task(title, due_date or None)
                    output_func(f"Added: {_format_task(task)}")

                elif choice == "2":
                    tasks = manager.list_tasks()
                    if not tasks:
                        output_func("No tasks found.")
                    else:
                        output_func("\n".join(_format_task(task) for task in tasks))

                elif choice == "3":
                    task_id = _read_task_id(input_func("Task ID to complete: "))
                    task = manager.complete_task(task_id)
                    output_func(f"Completed: {_format_task(task)}")

                elif choice == "4":
                    task_id = _read_task_id(input_func("Task ID to delete: "))
                    task = manager.delete_task(task_id)
                    output_func(f"Deleted task {task.task_id}: {task.title}")

                elif choice == "5":
                    output_func("Goodbye!")
                    break

                else:
                    logger.warning("Invalid menu choice %r.", choice)
                    output_func("Invalid choice. Enter a number from 1 to 5.")

            except (TaskManagerError, ValueError) as error:
                logger.error("Operation failed: %s: %s", type(error).__name__, error)
                output_func(f"Operation failed: {error}")
                continue
            except (EOFError, KeyboardInterrupt):
                logger.warning("Input was interrupted.")
                output_func("\nInput interrupted. Closing the application.")
                break
            except Exception as error:
                logger.critical(
                    "Unexpected application error: %s: %s",
                    type(error).__name__,
                    error,
                    exc_info=True,
                )
                output_func("An unexpected error occurred. You may continue.")
                continue

        return manager
    finally:
        logger.info("Daily Task Manager closed.")

