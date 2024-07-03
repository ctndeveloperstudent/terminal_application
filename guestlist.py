guests = []

def add_guest():
    guest = input("Enter a new guest: ")
    guests.append(guest)
    print("Guest added successfully!")

def view_guests():
    if len(guests) == 0:
        print("No guests on the guest list.")
    else:
        print("List of guests:")
        for i, guest in enumerate(guests):
            print(f'{i+1}. {guest}')

def delete_guest():
    if len(guests) == 0:
        print("No guests to delete.")
    else:
        print('Guests:')
        for i, guest in enumerate(guests):
            print(f'{i+1}. {guest}')
        try:
            choice = int(input("Enter the guest number to delete: "))
            if 0 < choice <= len(guests):
                del guests[choice-1]
                print("Guest deleted successfully.")
            else:
                print("Invalid guest number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n===== Event Planner Application =====")
        print("============ Guest List =============")
        print("1. Add New Guest")
        print("2. View Guest List")
        print("3. Delete Guest")
        print("4. Back to Main Menu")
        print("5. Quit")

        try:
            choice = int(input("Enter the number of your choice: "))
            if choice == 1:
                add_guest()
            elif choice == 2:
                view_guests()
            elif choice == 3:
                delete_guest()
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
