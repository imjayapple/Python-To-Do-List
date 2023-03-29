# Create a display menu

def display_menu():
    print("\nTo-Do List Menu")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Quit")

# Allow users to view their tasks

def view_tasks(tasks):
    if not tasks:
        print("You have no tasks.")
        return
    
    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        status= "completed" if task["completed"] else "Pending"
        print(f"{i}. {task['description']} ({status})")