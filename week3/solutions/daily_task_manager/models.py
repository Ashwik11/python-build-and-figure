"""Task model and validation rules."""

from dataclasses import asdict, dataclass
from datetime import date, datetime

from .exceptions import TaskValidationError
from typing import Optional



@dataclass
class Task:
    """Represent one daily task."""

    task_id: int
    title: str
    due_date: Optional[str] = None
    completed: bool = False
    created_at: str = ""

    @classmethod
    def create(cls, task_id, title, due_date=None):
        """Validate inputs and create a new task."""
        if isinstance(task_id, bool) or not isinstance(task_id, int) or task_id < 1:
            raise TaskValidationError("Task ID must be a positive integer.")
        if not isinstance(title, str) or not title.strip():
            raise TaskValidationError("Task title is required.")

        cleaned_due_date = None
        if due_date is not None and str(due_date).strip():
            cleaned_due_date = str(due_date).strip()
            try:
                date.fromisoformat(cleaned_due_date)
            except ValueError as error:
                raise TaskValidationError("Due date must use YYYY-MM-DD format.") from error

        return cls(
            task_id=task_id,
            title=title.strip(),
            due_date=cleaned_due_date,
            completed=False,
            created_at=datetime.now().isoformat(timespec="seconds"),
        )

    @classmethod
    def from_dict(cls, data):
        """Validate stored dictionary data and rebuild a task."""
        if not isinstance(data, dict):
            raise TaskValidationError("Stored task data must be a dictionary.")

        required_fields = {"task_id", "title", "completed", "created_at"}
        missing_fields = required_fields.difference(data)
        if missing_fields:
            raise TaskValidationError(
                "Stored task is missing: " + ", ".join(sorted(missing_fields))
            )

        task = cls.create(data["task_id"], data["title"], data.get("due_date"))
        if not isinstance(data["completed"], bool):
            raise TaskValidationError("Stored completed value must be true or false.")
        if not isinstance(data["created_at"], str) or not data["created_at"].strip():
            raise TaskValidationError("Stored creation time is invalid.")

        task.completed = data["completed"]
        task.created_at = data["created_at"]
        return task

    def to_dict(self):
        """Return a JSON-serializable task dictionary."""
        return asdict(self)

