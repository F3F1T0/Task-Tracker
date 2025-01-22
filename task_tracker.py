import argparse

from functions import *

json_file = "Tasks.json"


def main():
    # Read json file to save tasks, to work in the program
    tasks = load_file(json_file)

    # Configurate parser
    parser = argparse.ArgumentParser(description="CLI Task Tracker")

    # Create subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subcomand "add"
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="Task description")

    # Subcomand "list"
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("type", type=str, choices=["all", "to do", "done", "in-progress"], help="Type of listing")

    # Subcommand "mark"
    mark_parser = subparsers.add_parser("mark", help="Change the status of a task by ID")
    mark_parser.add_argument("status", type=str, choices=["to do", "done", "in-progress"], help="New status of the task")
    mark_parser.add_argument("id", type=int, help="ID of the task to update")

    # Subcommand "update"
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="ID of the task to update")
    update_parser.add_argument("new_name", help="Task to update.")

    # Subcommand "delete"
    delete_parser = subparsers.add_parser("delete", help = "Delete a task")
    delete_parser.add_argument("id", type=int, help="id of the task to remove.")

    # Parse the arguments
    args = parser.parse_args()

    # Manejo de los comandos
    if args.command == "add":
        add_task(tasks, args.task)
    elif args.command == "list":
        list_tasks(tasks, args.type)
    elif args.command == "mark":
        change_status(tasks, args.status, args.id)
        save_file(json_file, tasks)
    elif args.command == "update":
        update_task(tasks, args.id, args.new_name)
        save_file(json_file, tasks)
    elif args.command == "delete":
        delete_task(tasks, args.id)
        save_file(json_file, tasks)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
