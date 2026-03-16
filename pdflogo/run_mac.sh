#!/bin/bash

echo "Starting PDF Logo Adder Web App..."
echo ""
echo "The app will open in your browser at: http://localhost:5000"
echo ""
echo "To stop the app, press Ctrl+C"
echo ""

# Try to find Python
if command -v python3 &> /dev/null; then
    python3 app.py
elif command -v python &> /dev/null; then
    python app.py
else
    echo "Python not found. Please install Python 3.6+ from https://www.python.org"
    exit 1
fi