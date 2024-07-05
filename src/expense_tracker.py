# Import necessary modules
from colorama import Fore, Style, init
init()

# File storage name
expenses_file = "expenses.txt"

# Function to load expenses from file to memory
def load_expenses():
    global expenses
    try:
        with open(expenses_file, 'r') as file:
            expenses = [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        with open(expenses_file, 'w') as file:
            file.write("")  
        expenses = []

# Function to save expenses to file
def save_expenses():
    global expenses
    with open(expenses_file, 'w') as file:
        for expense in expenses:
            file.write(','.join(expense) + '\n')

# Function to add expense
def add_expense():
    global expenses
    name = input("Enter the name of the expense: ")
    category = input("Enter the category of the expense: ")
    budgeted_cost = input("Enter the budgeted cost: $")
    actual_cost = input("Enter the actual cost: $")
    expenses.append([name, category, budgeted_cost, actual_cost])
    save_expenses()  
    print(Fore.GREEN + "Expense added successfully." + Style.RESET_ALL)

# Function to view all expenses
def view_expenses():
    global expenses
    load_expenses()
    if len(expenses) == 0:
        print(Fore.GREEN + "No expenses recorded." + Style.RESET_ALL)
    else:
        print("List of all expenses:")
        for i, expense in enumerate(expenses):
            print(f"{i+1}. Name: {expense[0]}, Category: {expense[1]}, Budgeted Cost: ${expense[2]}, Actual Cost: ${expense[3]}")

# Function to view expenses by category
def view_expenses_by_category():
    global expenses
    load_expenses()
    categories = set([expense[1] for expense in expenses])
    if len(categories) == 0:
        print(Fore.GREEN + "No expenses recorded." + Style.RESET_ALL)
    else:
        print("Available categories:")
        for i, category in enumerate(categories):
            print(f"{i+1}. {category}")

        chosen_category = input("Enter the number of the category to view expenses: ")
        try:
            chosen_category = int(chosen_category)
            if 0 < chosen_category <= len(categories):
                category_name = list(categories)[chosen_category - 1]
                print(f"Expenses in category '{category_name}':")
                for expense in expenses:
                    if expense[1] == category_name:
                        print(f"Name: {expense[0]}, Budgeted Cost: ${expense[2]}, Actual Cost: ${expense[3]}")
            else:
                print(Fore.RED + "Invalid category number. Please try again." + Fore.RESET)
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Fore.RESET)

# Function to delete an expense
def delete_expense():
    global expenses
    if len(expenses) == 0:
        print(Fore.GREEN + "No expenses to delete." + Style.RESET_ALL)
    else:
        while True:
            print("Expenses:")
            for i, expense in enumerate(expenses):
                print(f"{i+1}. Name: {expense[0]}, Category: {expense[1]}, Budgeted Cost: {expense[2]}, Actual Cost: {expense[3]}")
            choice = input("Enter the expense number to delete: ")

            try:
                choice = int(choice)
                if 0 < choice <= len(expenses):
                    del expenses[choice-1]
                    save_expenses()  
                    print(Fore.GREEN + "Expense deleted successfully." + Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED + "Invalid expense number. Please try again." + Fore.RESET)
            except ValueError:
                print(Fore.RED + "Invalid number. Please try again." + Fore.RESET)

            # Option to remain in delete or return to main menu
            back_choice = input("Do you want to go back to the main menu? (y/n): ").lower()
            if back_choice == 'y':
                break

# Function to handle saving changes before exiting
def save_changes_prompt():
    global expenses
    save_decision = input("There are unsaved changes. Would you like to save them? (y/n): ").lower()
    if save_decision == 'y':
        save_expenses()
        print(Fore.GREEN + "Changes saved successfully." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Changes not saved." + Fore.RESET)

