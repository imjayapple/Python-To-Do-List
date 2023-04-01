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

# Create the main loop in which the user will 'enter' the to-do list, receive user inputs & call appropriate functions

def main():
    tasks = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter the number of the action you want to perform (1, 2, 3, or 4): "))
            if choice not in range(1, 5):
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 4.")
            continue

        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            mark_task_completed(tasks)
        elif choice == 4:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()