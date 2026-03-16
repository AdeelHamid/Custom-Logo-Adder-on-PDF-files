# PDF Logo Adder - Easy Shareable App

A simple web app to add logos to PDF files. Share this entire folder with your friends - they can run it on their own computers!

## For Windows Users:

1. **First time setup**: Double-click `setup_windows.bat` to install required software
2. **Run the app**: Double-click `run_windows.bat`
3. **Use the app**: Open your browser to `http://localhost:5000`

## For Mac Users:

1. **First time setup**:
   - Open Terminal
   - Navigate to this folder: `cd /path/to/pdflogo`
   - Make setup script executable: `chmod +x setup_mac.sh`
   - Run setup: `./setup_mac.sh`

2. **Run the app**:
   - Make run script executable: `chmod +x run_mac.sh`
   - Run: `./run_mac.sh`

3. **Use the app**: Open your browser to `http://localhost:5000`

## What the App Does:

- Upload any PDF file
- Upload your logo image (PNG, JPG, etc.)
- Set logo position and size
- Download the PDF with logo added at the top (content shifts down automatically)

## Requirements:

- Python 3.6+ (download from https://www.python.org if needed)
- Internet connection for initial setup

## Troubleshooting:

- If setup fails, try running Terminal/Command Prompt as Administrator
- Make sure Python is installed and added to PATH
- For Mac: Make sure you have Xcode command line tools: `xcode-select --install`

## Files in this folder:

- `app.py` - The web app
- `add_logo.py` - PDF processing script
- `requirements.txt` - Required packages
- `templates/` - Web interface files
- `run_windows.bat` - Windows launcher
- `run_mac.sh` - Mac launcher
- `setup_windows.bat` - Windows setup
- `setup_mac.sh` - Mac setup
- `README.md` - This file

Enjoy adding logos to your PDFs! 🎉