# Daily Task Manager CLI

A small command-line productivity tool built through a staged AI-assisted workflow. It allows a user to add, list, complete, and delete daily tasks. Tasks persist in JSON, and application events are written to a log file.

## Features

- Add a task with an optional `YYYY-MM-DD` due date.
- List pending and completed tasks.
- Mark a task complete.
- Delete a task.
- Persist data between sessions using JSON.
- Validate titles, dates, and task IDs.
- Continue after recoverable input and operation errors.
- Record DEBUG, INFO, WARNING, ERROR, and CRITICAL events when applicable.

## Project structure

```text
daily_task_manager/
├── __init__.py
├── cli.py
├── exceptions.py
├── logging_config.py
├── main.py
├── models.py
├── storage.py
├── task_service.py
├── README.md
├── data/
│   └── tasks.json          # Created when the first task is saved
└── logs/
    └── task_manager.log    # Created when the application runs
```

## Run the application

From `week3/solutions`, use either command:

```bash
python -m daily_task_manager.main
```

```bash
python daily_task_manager/main.py
```

## Menu

```text
1. Add Task
2. List Tasks
3. Complete Task
4. Delete Task
5. Exit
```

## Package responsibilities

| Module | Responsibility |
|---|---|
| `models.py` | Defines the `Task` model and validation rules |
| `storage.py` | Loads and safely saves JSON task data |
| `task_service.py` | Implements add, list, complete, delete, and find operations |
| `cli.py` | Runs the menu and handles user input errors |
| `logging_config.py` | Configures file logging |
| `exceptions.py` | Defines project-specific exceptions |
| `main.py` | Starts the application |

## AI prompts used step by step

I did not request the entire project in one prompt. I used the following staged prompts:

1. **Requirement analysis:** “Help me understand the requirements for the Vibe Coding Challenge and choose one small CLI productivity tool that can demonstrate packages, exceptions, logging, and persistence.”
2. **Structure:** “Suggest a package and module structure for a Daily Task Manager, but do not generate the implementation yet.”
3. **Task model:** “Create only the task model and custom exception module. Validate a required title and an optional date in YYYY-MM-DD format.”
4. **Model testing:** “Give me small tests for task creation, invalid titles, invalid dates, serialization, and rebuilding a task from stored data.”
5. **Storage:** “Add a JSON storage module using try, except, and finally. Save through a temporary file so a failed write does not damage the existing data.”
6. **Bug investigation:** “A malformed JSON test raises JSONDecodeError instead of my custom StorageError. Explain why and make the smallest safe fix.”
7. **Business operations:** “Create a task service module for add, list, find, complete, and delete operations while keeping JSON logic inside the storage module.”
8. **CLI:** “Build the menu-driven CLI using the existing modules. Catch operation errors inside the loop so one error does not close the program.”
9. **Logging:** “Review the project and make sure successful actions, validation failures, missing task IDs, storage errors, startup, and shutdown are logged to a file.”
10. **Final refactor and tests:** “Refactor only where needed, support both module and direct-file execution, then test persistence, invalid input, try/except/finally, and continued menu operation.”

## Error found and fixed during development

The first storage version handled operating-system and task-validation errors but did not catch `json.JSONDecodeError`. A malformed `tasks.json` file therefore leaked a low-level exception instead of the project’s custom error. The storage exception handler was updated to catch `json.JSONDecodeError`, log it, and raise `StorageError`. The valid-data and malformed-data tests then both passed.

## Requirement checklist

- [x] Command-line Python productivity application
- [x] At least four Python modules
- [x] One importable package
- [x] Imports between modules
- [x] `try`, `except`, and `finally`
- [x] Custom exceptions
- [x] Logging to `logs/task_manager.log`
- [x] JSON persistence in `data/tasks.json`
- [x] README with at least five AI prompts
- [x] Tested after each development stage

