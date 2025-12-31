#!/bin/bash
# Setup script for VSP AI/ML Training Pipeline
# This script sets up the Python environment and installs dependencies
#
# Educational Context:
# This is a bash shell script - a series of commands executed in sequence.
# 
# Key Concepts:
# 1. Shebang (#!/bin/bash): Tells system to use bash interpreter
# 2. Comments (#): Lines starting with # are ignored (documentation)
# 3. Variables: Store values ($VARIABLE_NAME)
# 4. Conditionals: if/then/else for decision making
# 5. Error handling: Check exit codes ($?) to detect failures
#
# Why use a script?
# - Automates repetitive setup tasks
# - Ensures consistent environment
# - Saves time (one command vs many)
# - Can be shared and version controlled

# Print header message to user
# echo prints text to terminal
echo "VSP AI/ML Training Pipeline - Environment Setup"
echo "================================================"

# Check Python version before proceeding
# This verifies Python 3 is installed and accessible
# --version flag shows version number
echo "Checking Python version..."
python3 --version

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment."
        echo "Please ensure python3-venv is installed:"
        echo "  sudo apt-get install python3-venv  # On Ubuntu/Debian"
        exit 1
    fi
else
    echo "Virtual environment already exists."
    # Check if it's valid
    if [ ! -f ".venv/bin/activate" ]; then
        echo "Warning: .venv exists but appears incomplete. Recreating..."
        rm -rf .venv
        python3 -m venv .venv
        if [ $? -ne 0 ]; then
            echo "Error: Failed to recreate virtual environment."
            exit 1
        fi
    fi
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Create output directories
echo "Creating output directories..."
mkdir -p outputs/logs
mkdir -p outputs/processed
mkdir -p outputs/results

echo ""
echo "Setup complete!"
echo "To activate the environment in the future, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To run notebooks, open them in VS Code or use:"
echo "  jupyter notebook"

