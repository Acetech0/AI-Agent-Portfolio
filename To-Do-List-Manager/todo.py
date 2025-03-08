import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file or return an empty list."""
    return open(TASKS_FILE).read().splitlines() if os.path.exists(TASKS_FILE) else []

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASKS_FILE, "w") as file:
        file.write("\n".join(tasks) + "\n")

def add_task():
    """Add a new task."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added!")
    else:
        print("Task cannot be empty.")

def view_tasks():
    """View all tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task():
    """Remove a task."""
    view_tasks()
    if not tasks:
        return
    
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Task '{tasks.pop(index)}' removed!")
            save_tasks(tasks)
        else:
            print("Invalid number. Try again.")
    except ValueError:
        print("Please enter a valid number.")

tasks = load_tasks()

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
