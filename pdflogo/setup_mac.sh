#!/bin/bash

echo "Installing required packages for PDF Logo Adder..."
echo ""

# Check if pip is available
if command -v pip3 &> /dev/null; then
    pip3 install -r requirements.txt
elif command -v pip &> /dev/null; then
    pip install -r requirements.txt
else
    echo "pip not found. Please install pip first."
    exit 1
fi

echo ""
echo "Installation complete! You can now run the app."
echo ""