# Filename where guest data will be stored
guests_file = "guests.txt"

# Function to load guests from file
def load_guests():
    try:
        with open(guests_file, 'r') as file:
            guests = [line.strip() for line in file.readlines()]
        return guests
    except FileNotFoundError:
        return []

# Function to save guests to file
def save_guests(guests):
    with open(guests_file, 'w') as file:
        for guest in guests:
            file.write(guest + '\n')

# Function to add guest
def add_guest():
    guest = input("Enter a new guest: ")
    guests.append(guest)
    save_guests(guests)
    print("Guest added successfully!")

# Function to delete guest
def delete_guest():
    global guests  # This is to make sure we're modifying the global guests list
    if len(guests) == 0:
        print("No guests to delete.")
    else:
        while True:
            print('Guests:')
            for i, guest in enumerate(guests):
                print(f'{i+1}. {guest}')
            choice = input("Enter the guest number to delete: ")
            
            try:
                choice = int(choice)
                if 0 < choice <= len(guests):
                    del guests[choice-1]
                    save_guests(guests)  # Update the file after deletion
                    print("Guest deleted successfully.")
                    break
                else:
                    print("Invalid guest number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
            
            # Option to remain in delete or return to main menu
            back_choice = input("Do you want to go back to the main menu? (y/n): ").lower()
            if back_choice == 'y':
                break

# View guest function
def view_guests():
    global guests  
    guests = load_guests()  
    if len(guests) == 0:
        print("No guests on the guest list.")
    else:
        print("List of guests:")
        for i, guest in enumerate(guests):
            print(f'{i+1}. {guest}')


def main():
    global guests  
    guests = load_guests()  
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
                save_guests(guests)  # Save guests to file before quitting
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

