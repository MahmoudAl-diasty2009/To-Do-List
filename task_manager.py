tasks = []

def main():
    message = """
1- Add tasks to a list
2- Mark task as complete
3- View tasks
4- Quit
"""

    while True:
        print(message)
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            mark_task_complete()
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4")

def add_task():
    task = input("Enter task: ")
    task_info = {"task": task, "completed": False}
    tasks.append(task_info)
    print("Task added to the list successfully")

def mark_task_complete():
    incomplete_tasks = [(i, task) for i, task in enumerate(tasks) if not task["completed"]]

    if not incomplete_tasks:
        print("No tasks to mark as complete")
        return

    for i, (original_index, task) in enumerate(incomplete_tasks):
        print(f"{i + 1}- {task['task']}")
        print("-" * 30)

    try:
        task_number = int(input("Choose the task number to complete: "))
        if task_number < 1 or task_number > len(incomplete_tasks):
            print("Invalid Task Number")
            return

        task_index = incomplete_tasks[task_number - 1][0]
        tasks[task_index]["completed"] = True

        print("Task marked as completed ✅")

    except ValueError:
        print("Invalid input, please enter a valid number")

def view_tasks(tasks_list):
    if not tasks_list:
        print("No tasks to view")
        return

    for i, task in enumerate(tasks_list):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i + 1}. {task['task']} {status}")

if __name__ == "__main__":
    main()
