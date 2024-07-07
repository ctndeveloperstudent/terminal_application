# Import necessary modules
from colorama import Fore, Style, init
init()

# Filename where to do list data will be stored
tasks_file = "tasks.txt"

# Function to load tasks from file into memory
def load_tasks():
    global tasks
    try:
        with open(tasks_file, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        with open(tasks_file, 'w') as file:
            file.write("")  
        tasks = []

# Function to save tasks to file
def save_tasks():
    global tasks
    with open(tasks_file, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to add task
def add_task():
    global tasks
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks() 
    print(Fore.GREEN + "Task added successfully." + Style.RESET_ALL)

# View Task Function
def view_tasks():
    global tasks
    load_tasks()
    if len(tasks) == 0:
        print(Fore.GREEN + "No tasks on the to-do list."+ Style.RESET_ALL)
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')

# Function to delete task from list
def delete_task():
    global tasks
    if len(tasks) == 0:
        print(Fore.GREEN + "No tasks to delete." + Style.RESET_ALL)
    else:
        while True:
            print('Tasks:')
            for i, task in enumerate(tasks):
                print(f'{i+1}. {task}')
            choice = input("Enter the task number to delete: ")
                
            try:
                choice =int(choice)
                if 0 < choice <= len(tasks):
                    del tasks[choice-1]
                    save_tasks()
                    print(Fore.GREEN + "Task deleted successfully." + Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED + "Invalid task number. Please try again." + Fore.RESET)
            except ValueError:
                print(Fore.RED + "Invalid number. Please try again.")
            
            # Option to break out of the loop and go back to the main menu
            back_choice = input("Do you want to go back to the main menu? (y/n): ").lower()
            if back_choice == 'y':
                break

#Function to save before quitting app
def save_changes_prompt():
    global tasks
    save_decision = input("There are unsaved changes. Would you like to save them? (y/n): ").lower()
    if save_decision == 'y':
        save_tasks()
        print(Fore.GREEN + "Changes saved successfully." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Changes not saved." + Fore.RESET)