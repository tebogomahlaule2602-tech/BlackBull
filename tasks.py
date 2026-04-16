tasks = []

while True:
    print("\n--- BLACKBULL TASK MANAGER ---")
    print("1. Add Task | 2. Show Tasks | 3. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        new_task = input("What needs to be done? ")
        tasks.append(new_task)
        print("Task added!")
    elif choice == '2':
        print("\nCURRENT TASKS:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == '3':
        print("Exiting BlackBull Suite.")
        break
    else:
        print("Invalid choice, try again.")
