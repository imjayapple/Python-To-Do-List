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

# Adding tasks function, 'add new task'

def add_task(tasks):
    description = input("Enter the task description: ")
    tasks.append({"description": description, "completed": False})
    print("Task added.")

# Mark tasks as completed

def mark_task_completed(tasks):
    view_tasks(tasks)

    if not tasks:
        return
    
    while True:
        try:
            task_number = int(input("Enter the task number you want to mark as completed: "))
            if task_number < 1 or task_number > len(tasks):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    tasks[task_number - 1]["completed"] = True
    print("Task marked as completed.")