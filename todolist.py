tasks = []

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks on the to do list.")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')

def delete_tasks():
    if len(tasks) == 0:
        print("No tasks to delete.")
    else:
        print('Tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        choice = int(input("Enter the task number to delete:"))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task deleted successfuly.")
        else:
            print("Invalid task number.")

def main():

    while True:
        print("\n===== Event Planner Application =====")
        print("\n============ To Do List =============")
        print("1.Add Task")
        print("2.View Task")
        print("3.Delete Task")
        print("4.Back to Main Menu")
        print("5.Quit")

        choice = int(input("Enter the number of your choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_tasks()
        elif choice == 4:
            pass
        elif choice == 5:
            print("Thank you for using the Event Planner Application.")
            break
        else:
            print("Invalid choice. Please try again.")

main()

    


