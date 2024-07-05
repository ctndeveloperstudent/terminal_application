# Event Planner Application

## Overview

Welcome to the Event Planner Application! This application helps you manage various aspects of event planning, including managing the guest lists, keeping track of our to-do lists, and event expense tracking.

## Getting Started
To run the Event Planner Application, follow these steps:

1. Clone the repository
    
        git clone <https://github.com/ctndeveloperstudent/terminal_application>

2. Navigate to the project directory

        cd event-planner

3. Run the setup script to install dependencies and set up the environment. This script will check for Python installation and install necessary dependencies:
        
        ./run.sh ()
        
4. Once setup is complete, you can run the application:

        python event_planner.py

## Features

### 1. Guest List Management
- Add new guests
- View guest list
- Delete guests
- Save guest list to file (guests.txt)

### 2. To-Do List Management
- Add tasks
- View task list
- Delete tasks
- Save task list to file (tasks.txt)

### 3. Expense Tracker
- Add expenses (name, category, budgeted cost, actual cost)
- View all expenses
- View expenses by category
- Delete expenses

### 4. User Interface Enhancements
- Colorful and formatted output using libraries like Colorama, PyFiglet, or Tabulate
- User-friendly prompts and menus

### 5. Data Persistence
- Automatic saving and loading of data from files
- Ensure changes are saved before exiting the application

### 6. Error Handling and Validation
- Graceful handling of invalid inputs
- Validation of user inputs to prevent errors

### 7. Main Menu Navigation
- Easy navigation between guest list, to-do list, and expense tracker
- Option to quit the application

### 8. Setup and Dependencies
- Include setup instructions and dependencies in a run.sh or setup script
- Notify users if Python is not installed and provide instructions or a link to download it

## Dependencies
- Python 3.9
- Pyfiglet
- Colorama

## Contributing
Contributions are welcome! If you have suggestions, feature requests, or find any issues, please create a new issue or pull request.