# Import Files
from guestlist import load_guests, save_guests, add_guest, view_guests, delete_guest
from todolist import load_tasks, save_tasks, add_task, view_tasks, delete_task
from expense_tracker import load_expenses, save_expenses, add_expense, delete_expense, view_expenses, view_expenses_by_category

# Main Menu Function
def main_menu():
    while True:
        print("\n===== Event Planner Application =====")
        print("1. Guest List")
        print("2. To-Do List")
        print("3. Expense Tracker")
        print("4. Quit")

        try:
            choice = input("Enter the number of your choice: ")

            if choice == '1':
                guest_menu()
            elif choice == '2':
                todo_menu()
            elif choice == '3':
                expences_menu()
            elif choice == '4':
                print("Thank you for using the Event Planner Application.")
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

# Guest List Function
def guest_menu():
    load_guests()  

    while True:
        print("\n===== Event Planner Application =====")
        print("============ Guest List =============")
        print("1. Add New Guest")
        print("2. View Guest List")
        print("3. Delete Guest")
        print("4. Back to Main Menu")

        try:
            choice = input("Enter the number of your choice: ")

            if choice == '1':
                add_guest()
            elif choice == '2':
                view_guests()
            elif choice == '3':
                delete_guest()
            elif choice == '4':
                save_guests()  
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")
        

# To Do list Function
def todo_menu():
    load_tasks()  

    while True:
        print("\n===== Event Planner Application =====")
        print("============ To Do List =============")
        print("1. Add Task")
        print("2. View Task List")
        print("3. Delete Task")
        print("4. Back to Main Menu")

        try:
            choice = input("Enter the number of your choice: ")

            if choice == '1':
                add_task()
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                delete_task()
            elif choice == '4':
                save_tasks()  
                break
            else:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
 

# Expense Tracker Function
def expences_menu():
    load_expenses()  

    while True:
        print("\n===== Event Planner Application =====")
        print("============ Expense Tracker =============")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Delete Expense")
        print("5. Back to Main Menu")
        print("6. Quit")

        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                view_expenses_by_category()
            elif choice == 4:
                delete_expense()
            elif choice == 5:
                continue
            elif choice == 6:
                save_expenses()
                print("Thank you for using the Event Planner Application.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter 'yes' or 'no'.")

    # Save changes before exiting
    save_expenses()

        

        


if __name__ == "__main__":
    main_menu()
