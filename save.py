# Task List Save/Load Program

tasks = []

def load_tasks():
    global tasks
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.read().splitlines()
        print("Tasks loaded successfully!")
    except FileNotFoundError:
        print("No saved task file found.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    print("Tasks saved successfully!")

while True:
    print("\n--- TASK LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Save Tasks")
    print("4. Load Tasks")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        save_tasks()

    elif choice == "4":
        load_tasks()

    elif choice == "5":
        save_tasks()  # Automatically save before exiting
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")