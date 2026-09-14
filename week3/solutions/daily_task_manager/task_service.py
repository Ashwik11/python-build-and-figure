"""Business operations for adding, listing, completing, and deleting tasks."""

from dataclasses import replace

from .exceptions import TaskNotFoundError
from .models import Task


class TaskManager:
    """Coordinate task operations with persistent storage."""

    def __init__(self, store, logger):
        self.store = store
        self.logger = logger
        self._tasks = self.store.load_tasks()

    def list_tasks(self):
        """Return all tasks ordered by task ID."""
        self.logger.debug("Listing %s task(s).", len(self._tasks))
        return sorted(self._tasks, key=lambda task: task.task_id)

    def add_task(self, title, due_date=None):
        """Create, save, and return a new task."""
        next_id = max((task.task_id for task in self._tasks), default=0) + 1
        task = Task.create(next_id, title, due_date)
        updated_tasks = [*self._tasks, task]
        self.store.save_tasks(updated_tasks)
        self._tasks = updated_tasks
        self.logger.info("Added task %s: %s.", task.task_id, task.title)
        return task

    def find_task(self, task_id):
        """Return the task with the requested ID."""
        for task in self._tasks:
            if task.task_id == task_id:
                return task
        self.logger.warning("Task ID %s was not found.", task_id)
        raise TaskNotFoundError(f"Task {task_id} was not found.")

    def complete_task(self, task_id):
        """Mark a task complete, persist the change, and return it."""
        selected_task = self.find_task(task_id)
        if selected_task.completed:
            self.logger.warning("Task %s is already complete.", task_id)
            return selected_task

        completed_task = replace(selected_task, completed=True)
        updated_tasks = [
            completed_task if task.task_id == task_id else task
            for task in self._tasks
        ]
        self.store.save_tasks(updated_tasks)
        self._tasks = updated_tasks
        self.logger.info("Completed task %s: %s.", task_id, completed_task.title)
        return completed_task

    def delete_task(self, task_id):
        """Delete a task, persist the change, and return the deleted task."""
        selected_task = self.find_task(task_id)
        updated_tasks = [task for task in self._tasks if task.task_id != task_id]
        self.store.save_tasks(updated_tasks)
        self._tasks = updated_tasks
        self.logger.info("Deleted task %s: %s.", task_id, selected_task.title)
        return selected_task

