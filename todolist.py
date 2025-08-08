def todo_list():
    tasks = []
    
    def add_task(task_name):
        tasks.append({"name": task_name, "completed": False})
        print(f"Task '{task_name}' added.")

    def view_tasks():
        if not tasks:
            print("No tasks in the list.")
            return

        print("--- Your To-Do List ---")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['name']}")
        print("-----------------------")

    def mark_completed(task_index):
        if 1 <= task_index <= len(tasks):
            tasks[task_index - 1]["completed"] = True
            print(f"Task '{tasks[task_index - 1]['name']}' marked as completed.")
        else:
            print("Invalid task number.")

    while True:
        print("\nOptions:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task_name = input("Enter the task name: ")
            add_task(task_name)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                mark_completed(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

todo_list()