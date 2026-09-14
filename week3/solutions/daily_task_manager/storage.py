"""JSON storage for daily tasks."""

import json
from pathlib import Path

from .exceptions import StorageError, TaskValidationError
from .models import Task


class TaskStore:
    """Load and save tasks in a JSON file."""

    def __init__(self, data_file, logger):
        self.data_file = Path(data_file)
        self.logger = logger

    def load_tasks(self):
        """Load tasks from JSON and return Task objects."""
        self.logger.debug("Loading tasks from %s.", self.data_file)
        try:
            if not self.data_file.exists():
                self.logger.info("No task data file exists yet; starting with an empty list.")
                return []

            with self.data_file.open("r", encoding="utf-8") as file:
                raw_tasks = json.load(file)
            if not isinstance(raw_tasks, list):
                raise TaskValidationError("Stored task data must be a list.")

            tasks = [Task.from_dict(item) for item in raw_tasks]
            self.logger.info("Loaded %s task(s).", len(tasks))
            return tasks
        except (OSError, json.JSONDecodeError, TaskValidationError) as error:
            self.logger.error("Could not load tasks: %s: %s.", type(error).__name__, error)
            raise StorageError("Task data could not be loaded.") from error
        finally:
            self.logger.debug("Finished the task-loading attempt.")

    def save_tasks(self, tasks):
        """Safely save Task objects using a temporary file."""
        temporary_file = self.data_file.with_suffix(self.data_file.suffix + ".tmp")
        self.logger.debug("Saving %s task(s) to %s.", len(tasks), self.data_file)

        try:
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            serialized_tasks = [task.to_dict() for task in tasks]
            temporary_file.write_text(
                json.dumps(serialized_tasks, indent=2),
                encoding="utf-8",
            )
            temporary_file.replace(self.data_file)
            self.logger.info("Saved %s task(s) successfully.", len(tasks))
        except (OSError, TypeError, TaskValidationError) as error:
            self.logger.error("Could not save tasks: %s: %s.", type(error).__name__, error)
            raise StorageError("Task data could not be saved.") from error
        finally:
            if temporary_file.exists():
                try:
                    temporary_file.unlink()
                except OSError as cleanup_error:
                    self.logger.warning(
                        "Temporary file %s could not be removed: %s.",
                        temporary_file,
                        cleanup_error,
                    )
            self.logger.debug("Finished the task-saving attempt.")
