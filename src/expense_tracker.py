# Import necessary modules
from colorama import Fore, Style, init
from tabulate import tabulate

init()

# File storage name
expenses_file = "expenses.txt"

# Function to load expenses from file to memory
def load_expenses():
    global expenses
    try:
        with open(expenses_file, 'r') as file:
            expenses = [line.strip().split(',') for line in \
                        file.readlines()]
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
        headers = ["Name", "Category", "Budgeted Cost $", "Actual Cost \
                   $"]
        print(Fore.GREEN + "List of all expenses:" + Style.RESET_ALL)
        print(tabulate(expenses, headers=headers, tablefmt="pretty"))


# Function to view expenses by category
def view_expenses_by_category():
    global expenses
    load_expenses()
    categories = set([expense[1] for expense in expenses])
    if len(categories) == 0:
        print(Fore.GREEN + "No expenses recorded." + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Available categories:" + Style.RESET_ALL)
        for i, category in enumerate(categories):
            print(f"{i+1}. {category}")

        chosen_category = input("Enter the number of the category to \
                                view expenses: ")
        try:
            chosen_category = int(chosen_category)
            if 0 < chosen_category <= len(categories):
                category_name = list(categories)[chosen_category - 1]
                filtered_expenses = [expense for expense in expenses if \
                                     expense[1] == category_name]
                headers = ["Name", "Category", "Budgeted Cost $", "Actual \
                           Cost $"]
                print(Fore.GREEN + f"Expenses in category '{category_name}\
                      ':" + Style.RESET_ALL)
                print(tabulate(filtered_expenses, headers=headers, tablefmt=\
                               "pretty"))
            else:
                print(Fore.RED + "Invalid category number. Please try again." \
                      + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)


# Function to delete an expense
def delete_expense():
    global expenses
    if len(expenses) == 0:
        print(Fore.GREEN + "No expenses to delete." + Style.RESET_ALL)
    else:
        while True:
            headers = ["#", "Name", "Category", "Budgeted Cost $", "Actual Cost \
                       $"]
            numbered_expenses = [[i+1] + expense for i, expense in enumerate\
                                 (expenses)]
            print(Fore.GREEN + "List of all expenses:" + Style.RESET_ALL)
            print(tabulate(numbered_expenses, headers=headers, tablefmt=\
                           "pretty"))

            choice = input("Enter the expense number to delete (or 'b' to \
                           go back): ")

            if choice.lower() == 'b':
                break

            try:
                choice = int(choice)
                if 0 < choice <= len(expenses):
                    del expenses[choice-1]
                    save_expenses()
                    print(Fore.GREEN + "Expense deleted successfully." + \
                          Style.RESET_ALL)
                    break
                else:
                    print(Fore.RED + "Invalid expense number. Please try \
                          again." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Invalid number. Please try again." + \
                      Style.RESET_ALL)

# Function to handle saving changes before exiting
def save_changes_prompt():
    global expenses
    save_decision = input("There are unsaved changes. Would you like to \
                          save them? (y/n): ").lower()
    if save_decision == 'y':
        save_expenses()
        print(Fore.GREEN + "Changes saved successfully." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Changes not saved." + Fore.RESET)

