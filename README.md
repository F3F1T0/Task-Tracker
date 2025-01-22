# Task Tracker CLI

A simple and efficient command-line application for tracking and managing tasks.

## Features

- Add tasks with a description and default status.
- List tasks by their current status (`to do`, `in-progress`, `done`, or `all`).
- Update task names and change their statuses.
- Delete tasks by ID.
- Persist tasks in a JSON file for future sessions.

---

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/task-tracker-cli.git
   cd task-tracker-cli
2. Ensure you have Python 3.8+ installed.
3. Run the application directly using:
   ```
   python task_tracker.py

# Usage

Run the program with the following command:

``` python main.py <command> [arguments] ```

## Commands and Examples

- Add a new task ✅:

``` python main.py add "Task description" ```

- List tasks by status 📋:

``` python main.py list all ```

- Change the status of a task 🖋️:

``` python main.py mark done 1 ```

- Update a task's name 🖊️:

``` python main.py update 1 "New Task Name" ```

- Delete a task by its ID 🗑️:

``` python main.py delete 1 ```

## Example

```
# Adding a new task
python main.py add "Walk the dog"

# Listing all tasks
python main.py list all

# Marking a task as done
python main.py mark done 1

# Updating a task's name
python main.py update 1 "Walk Lira"

# Deleting a task
python main.py delete 1
```
# File Structure

main.py: Entry point of the application

functions.py: Contains all the core logic

Tasks.json: JSON file where tasks are stored

README.md: Project documentation

# Contributing

Contributions are welcome! If you'd like to improve this project, feel free to fork the repository and submit a pull request. Please ensure your code adheres to the existing style and includes appropriate comments.

### Project URL:
It was made following the project of roadmap.sh:
https://roadmap.sh/projects/task-tracker
