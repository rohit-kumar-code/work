# Initialize an empty list to store tasks
tasks = []

def show_menu():
    """Display the menu to the user."""
    print("\nTo-Do List App")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Mark a task as completed")
    print("5. Exit")

def add_task():
    """Add a new task to the list."""
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def view_tasks():
    """Display all tasks in the list."""
    if not tasks:
        print("No tasks to show.")
    else:
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index + 1}. {task['task']} - {status}")

def delete_task():
    """Delete a task from the list by its number."""
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_number < len(tasks):
            removed_task = tasks.pop(task_number)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_completed():
    """Mark a task as completed."""
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_number < len(tasks):
            tasks[task_number]["completed"] = True
            print(f"Task '{tasks[task_number]['task']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the To-Do List app."""
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_completed()
        elif choice == "5":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
