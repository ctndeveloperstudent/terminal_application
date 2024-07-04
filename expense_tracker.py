expenses_file = "expenses.txt"

# Function to load expenses 
def load_expenses():
    try:
        with open(expenses_file, 'r') as file:
            expenses = [line.strip().split(',') for line in file.readlines()]
        return expenses
    except FileNotFoundError:
        with open(expenses_file, 'w') as file:  # Create file if it doesn't exist
            file.write("")
        return []

# Function to save expenses to file
def save_expenses(expenses):
    with open(expenses_file, 'w') as file:
        for expense in expenses:
            file.write(','.join(expense) + '\n')

# Function to add expense
def add_expense():
    global expenses
    name = input("Enter the name of the expense: ")
    category = input("Enter the category of the expense: ")
    budgeted_cost = input("Enter the budgeted cost: ")
    actual_cost = input("Enter the actual cost: ")
    paid = input("Has the expense been paid? (yes/no): ").lower()
    expenses.append([name, category, budgeted_cost, actual_cost, '✓' if paid == 'yes' else '✗'])
    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    global expenses
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        print("List of expenses:")
        for i, expense in enumerate(expenses):
            print(f"{i+1}. Name: {expense[0]}, Category: {expense[1]}, Budgeted Cost: {expense[2]}, Actual Cost: {expense[3]}, Paid: {expense[4]}")

# Function to delete an expense
def delete_expense():
    global expenses
    if len(expenses) == 0:
        print("No expenses to delete.")
    else:
        while True:
            print("Expenses:")
            for i, expense in enumerate(expenses):
                print(f"{i+1}. Name: {expense[0]}, Category: {expense[1]}, Budgeted Cost: {expense[2]}, Actual Cost: {expense[3]}, Paid: {expense[4]}")
            choice = input("Enter the expense number to delete: ")

            try:
                choice = int(choice)
                if 0 < choice <= len(expenses):
                    del expenses[choice-1]
                    print("Expense deleted successfully.")
                    break
                else:
                    print("Invalid expense number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

            # Option to remain in delete or return to main menu
            back_choice = input("Do you want to go back to the main menu? (y/n): ").lower()
            if back_choice == 'y':
                break

