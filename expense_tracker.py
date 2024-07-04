# Filename where expenses data will be stored
expenses_file = "expenses.txt"

# Function to load expenses from file to memory
def load_expenses():
    global expenses
    try:
        with open(expenses_file, 'r') as file:
            expenses = [line.strip().split(',') for line in file.readlines()]
    except FileNotFoundError:
        with open(expenses_file, 'w') as file:
            file.write("")  # Create an empty file if it doesn't exist
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
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    global expenses
    load_expenses()
    if len(expenses) == 0:
        print("No expenses recorded.")
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
        print("No expenses recorded.")
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
                print("Invalid category number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete an expense
def delete_expense():
    global expenses
    if len(expenses) == 0:
        print("No expenses to delete.")
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

# Function to handle saving changes before exiting
def save_changes_prompt():
    global expenses
    save_decision = input("There are unsaved changes. Would you like to save them? (y/n): ").lower()
    if save_decision == 'y':
        save_expenses()
        print("Changes saved successfully.")
    else:
        print("Changes not saved.")

# Main function to run the application
def main():
    global expenses
    load_expenses()

    while True:
        print("\n===== Event Planner Application =====")
        print("============ Expense Tracker =============")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. Delete Expense")
        print("5. Back to Main Menu")
        

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
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    # Save changes before exiting
    save_expenses()

if __name__ == "__main__":
    main()
