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
            file.write("")  # Create an empty file if it doesn't exist
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
    save_tasks() #Save tasks to memory after adding
    print("Task added successfully!")

# View Task Function
def view_tasks():
    global tasks
    load_tasks()
    if len(tasks) == 0:
        print("No tasks on the to-do list.")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')

# Function to delete task from list
def delete_task():
    global tasks
    if len(tasks) == 0:
        print("No tasks to delete.")
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
                    save_tasks() #save immedietly after deletion
                    print("Task deleted successfully.")
                    break
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
            
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
        print("Changes saved successfully.")
    else:
        print("Changes not saved.")

#ain function to run the application
def main():
    global tasks
    load_tasks()

    while True:
        print("\n===== Event Planner Application =====")
        print("============ To-Do List =============")
        print("1. Add New Task")
        print("2. View Task List")
        print("3. Delete Task")
        print("4. Back to Main Memu")
        print("5. Quit")

        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                delete_task()
            elif choice ==4:
                continue
            elif choice == 5:
                print("Thank you for using the Event Planner Application.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Save changes before exiting
    save_tasks()

if __name__ == "__main__":
    main()

