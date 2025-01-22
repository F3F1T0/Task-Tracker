import json
from datetime import datetime

json_file = "Tasks.json"

def save_file(json_file, tasks):
    with open(json_file, "w") as file:
        json.dump(tasks, file, indent=4)


def load_file(json_file):
    try:
        with open(json_file, "r") as file:
            return json.load(file)
    except:
        return []


def add_task(tasks, description):
    # Generate ID
    if tasks:
        task_id = tasks[-1]["id"] + 1
    else:
        task_id = 1

    # Create the diccionarie
    task = {
        "id": task_id,
        "name": description,
        "status": "to do",
        "creation": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "update": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
    }

    tasks.append(task)  # Agregar la nueva tarea a la lista
    save_file(json_file, tasks)  # Guardar la lista actualizada en el archivo
    print(f"Task added correctly! ID: {task_id}")


def list_tasks(tasks, type):
    flag = False
    if tasks:

        valid_types = {"all", "to do", "done", "in-progress"}
        if type not in valid_types:
            print("Sorry, that type of listing is not admitted. Use: 'all', 'to do', 'done', or 'in-progress'.")
            return

        for task in tasks:
            task_for_printing = f"ID: {task['id']} | Name: {task['name']} | Status: {task['status']} | Created: {task['creation']} | Last Updated: {task['update']}"
            if type == "all" or task["status"] == type:
                print(task_for_printing)
                flag = True
        if flag is False:
            print(f"Sorry, the isn't any tasks with the {type} status at the moment.")
    else:
        print("Sorry, actually there aren't any tasks saved. Try to add a task first!")


def change_status(tasks, status, id):
    for task in tasks:
        if task["id"] == id:
            task["status"] = status
            task["update"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"Task with ID {id} marked as '{status}'.")
            return
    else:
        print(f"Sorry, the task with the id {id} doesn't exists.")


def update_task(tasks, id, name):
    for task in tasks:
        if task["id"] == id:
            task["name"] = name
            task["update"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"The new name for the task {id} is: {name}")
            return
    else:
        print(f"Sorry, the task with the id {id} doesn't exists.")


def delete_task(tasks, id):
    for i, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(i)
            print(f"Task with ID {id} has been deleted successfully.")
            return
    else:
        print(f"Sorry, the task with the ID {id} doesn't exist.")



