#!/bin/bash

# Python instalation check
if ! command -v python &> /dev/null; then
  echo "Python is not installed."
  echo "Please download and install Python from https://www.python.org/downloads/"
  exit 1
fi

# Check if virtual environment folder exists
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python -m venv venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Display setup completion message
echo "Setup completed successfully!"

# Run the application
echo "Running the application..."
python event_planner.py

# Deactivate the virtual environment
deactivate
