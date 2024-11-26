import json


def save_tasks(tasks):
    """Saves changes to the tasks file."""
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)


def display_tasks(completion, tasks):
    """Displays tasks depending on their completion status"""
    if completion == 1:
        print("Printing all complete tasks..")
        for i in tasks:
            if i["status"] == "complete":
                print(f" ID: {i["id"]} \n Description: {i["description"]}")
    elif completion == 2:
        print("Printing all incomplete tasks..")
        for i in tasks:
            if i["status"] == "incomplete":
                print(f" ID: {i["id"]} \n Description: {i["description"]}")
    elif completion == 3:
        print("Printing all tasks..")
        for i in tasks:
            print(f" ID: {i["id"]} \n Description: {i["description"]}")


def add_task(tasks):
    """Adds new tasks to the file or overwrites existing tasks"""
    task_id = input("Enter a unique task ID: ").upper()
    task_desc = input("Enter the task description: ")
    for i in range(0, len(tasks)):
        if tasks[i]["id"] == task_id:
            print("ID already exists in database. Would you like to overwrite it?")
            print(f"Current task: {tasks[i]}")
            resp = input("Input Y to overwrite task: ").lower().strip()
            if resp == "y":
                tasks[i] = {"id": task_id,
                            "description": task_desc, "status": "incomplete"}
                save_tasks(tasks)
                print("Task added successfully!")
                return tasks
            else:
                return tasks
    else:
        tasks.append(
            {"id": task_id, "description": task_desc, "status": "incomplete"})
    save_tasks(tasks)
    print("Task added successfully!")
    return tasks


def mark_task_complete(tasks):
    """Marks a task complete and writes it to the json file"""
    task_id = input("Enter the ID of the task you want to mark as complete:")
    for i in range(0, len(tasks)):
        if tasks[i]["id"] == task_id:
            tasks[i]["status"] = "complete"
            save_tasks(tasks)
            print("Task updated.")
            return tasks
    else:
        print("Task could not be found.")
        return tasks


def load_tasks():
    """Loads the tasks file"""
    try:
        with open("tasks.json", "r") as data:
            tasks = json.load(data)
    except:
        with open("tasks.json", "w") as data:
            tasks = []
            json.dump(tasks, data, indent=4)
    return tasks


def main():
    """Loops through option choices"""
    tasks = load_tasks()
    while True:
        print("")
        print("Please choose an option: \n1. View completed tasks \n2. View incomplete tasks \n3. View all tasks. \n4. Mark a task as complete \n5. Add a new task \n6. Exit")
        resp = input(">")
        print("")
        if resp == "1":
            display_tasks(1, tasks)
        elif resp == "2":
            display_tasks(2, tasks)
        elif resp == "3":
            display_tasks(3, tasks)
        elif resp == "4":
            tasks = mark_task_complete(tasks)
        elif resp == "5":
            tasks = add_task(tasks)
        elif resp == "6":
            break


if __name__ == "__main__":
    main()
