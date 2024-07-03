tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks on the to-do list.")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')

def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
    else:
        print('Tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        try:
            choice = int(input("Enter the task number to delete: "))
            if 0 < choice <= len(tasks):
                del tasks[choice-1]
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n===== Event Planner Application =====")
        print("============ To-Do List =============")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Back to Main Menu")
        print("5. Quit")

        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                continue
            elif choice == 5:
                print("Thank you for using the Event Planner Application.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

main()
