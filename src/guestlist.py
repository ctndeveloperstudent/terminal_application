# Import necessary modules
from colorama import Fore, Style, init
init()

# Filename where guest data will be stored
guests_file = "guests.txt"

# Function to load guests from file into memory
def load_guests():
    global guests
    try:
        with open(guests_file, 'r') as file:
            guests = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        with open(guests_file, 'w') as file:
            file.write("")  
        guests = []

# Function to save guests to file
def save_guests():
    global guests
    with open(guests_file, 'w') as file:
        for guest in guests:
            file.write(guest + '\n')

# Function to add guest
def add_guest():
    global guests
    guest = input("Enter a new guest: ")
    guests.append(guest)
    save_guests() 
    print(Fore.GREEN + "Guest added successfully." + Style.RESET_ALL)

# View guest function
def view_guests():
    global guests
    load_guests()
    if len(guests) == 0:
        print(Fore.GREEN + "No guests on the guests list." + Style.RESET_ALL)
    else:
        print("List of guests:")
        for i, guest in enumerate(guests):
            print(f'{i+1}. {guest}')

# Function to delete guest from list
def delete_guest():
    global guests
    if len(guests) == 0:
        print(Fore.GREEN + "No guests to delete." + Style.RESET_ALL)
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
                    save_guests()
                    print(Fore.GREEN + "Guest deleted successfully" + Style.RESET_ALL)  
                    break
                else:
                    print(Fore.RED + "Invalid guest number. Please try again." + Fore.RESET)
            except ValueError:
                print(Fore.RED + "Invalid number. Please try again." + Fore.RESET)

            # Option to remain in delete or return to main menu
            back_choice = input("Do you want to go back to the main menu? (y/n): ").lower()
            if back_choice == 'y':
                break

# Function to handle saving changes before exiting
def save_changes_prompt():
    global guests
    save_decision = input("There are unsaved changes. Would you like to save them? (y/n): ").lower()
    if save_decision == 'y':
        save_guests()
        print(Fore.GREEN + "Changes saved successfully." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Changes not saved" + Fore.RESET)
