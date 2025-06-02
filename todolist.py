tasks = []

def show_menu():
    print("\n=== To-Do List ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks):
            status = "✓" if task['done'] else "✗"
            print(f"{i + 1}. [{status}] {task['title']}")

def add_task():
    title = input("Enter task: ")
    tasks.append({'title': title, 'done': False})
    print("Task added.")

def mark_done():
    view_tasks()
    try:
        choice = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= choice < len(tasks):
            tasks[choice]['done'] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        choice = int(input("Enter task number to delete: ")) - 1
        if 0 <= choice < len(tasks):
            removed = tasks.pop(choice)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
