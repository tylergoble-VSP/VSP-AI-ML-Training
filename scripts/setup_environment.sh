#!/bin/bash
# Setup script for VSP AI/ML Training Pipeline
# This script sets up the Python environment and installs dependencies

echo "VSP AI/ML Training Pipeline - Environment Setup"
echo "================================================"

# Check Python version
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

