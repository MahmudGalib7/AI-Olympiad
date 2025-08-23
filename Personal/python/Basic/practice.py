import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error reading tasks file. Starting with an empty list.")
            return []
    return []

def save_tasks(tasks):
    """Saves tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    """Adds a new task to the list."""
    description = input("Enter task description: ")
    if description:
        tasks.append({"description": description, "done": False})
        print("Task added.")
    else:
        print("Task description cannot be empty.")

def view_tasks(tasks):
    """Displays all tasks with their status."""
    if not tasks:
        print("No tasks yet!")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{i + 1}. [{status}] {task['description']}")
    print("------------------\n")

def mark_task_done(tasks):
    """Marks a specific task as done."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the number of the task to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f"Task {task_num} marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a specific task."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['description']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def print_menu():
    """Prints the main menu options."""
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("-----------------------")

def main():
    """Main function to run the To-Do list application."""
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
            save_tasks(tasks)
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            print("Exiting To-Do List. Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()