#!/bin/bash

set -e

echo "================================="
echo "AI DevOps Assistant Setup"
echo "================================="

PROJECT_DIR=$(pwd)

echo "Checking Python..."

python3 --version


echo "Creating virtual environment..."

python3 -m venv venv


echo "Activating virtual environment..."

source venv/bin/activate


echo "Upgrading pip..."

pip install --upgrade pip


echo "Installing Python dependencies..."

pip install -r setup/requirements.txt


echo ""
echo "Setup completed successfully"
echo ""
echo "Activate environment using:"
echo ""
echo "source venv/bin/activate"