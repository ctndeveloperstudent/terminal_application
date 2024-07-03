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



    


