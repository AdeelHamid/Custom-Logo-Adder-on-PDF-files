# Custom Logo Adder for PDF Files

A simple web app that lets you add a company logo to PDF files quickly. Upload a PDF and a logo image, choose position and size, and download the updated PDF.

This repo contains the full app inside the `pdflogo/` folder.

## Features

- Web UI for adding a logo to PDFs
- Supports PNG/JPG logos
- Adjustable logo position and scale
- Processes a single PDF upload and returns a modified file

## Requirements

- Python 3.8+ (3.10+ recommended)
- Internet connection for first-time dependency install

## Quick Start (Windows)

1. Open the app folder:
   `cd pdflogo`
2. Install dependencies (first time only):
   Double-click `setup_windows.bat`
3. Run the app:
   Double-click `run_windows.bat`
4. Open your browser:
   `http://localhost:5000`

If the `.bat` scripts fail, see Troubleshooting below.

## Quick Start (macOS)

1. Open Terminal and go to the app folder:
   `cd /path/to/Custom-Logo-Adder-on-PDF-files/pdflogo`
2. Make scripts executable (first time only):
   `chmod +x setup_mac.sh`
   `chmod +x run_mac.sh`
3. Install dependencies (first time only):
   `./setup_mac.sh`
4. Run the app:
   `./run_mac.sh`
5. Open your browser:
   `http://localhost:5000`

## How to Use

1. Open `http://localhost:5000` in your browser.
2. Upload a PDF file.
3. Upload your logo image.
4. Set position (x, y) and scale.
5. Download the PDF with the logo added.

## Troubleshooting

- Windows: If the `.bat` files point to a Python path that does not exist, update them to your Python install path or run:
  `python -m pip install -r requirements.txt`
  `python app.py`
- macOS: If `python` is missing, install Python from python.org and try again.
- If you see permission errors on macOS, make sure the scripts are executable (`chmod +x`).

## Project Structure

- `pdflogo/app.py` - Flask web app
- `pdflogo/add_logo.py` - PDF processing logic (PyMuPDF)
- `pdflogo/templates/` - Web UI templates
- `pdflogo/run_mac.sh` / `pdflogo/run_windows.bat` - App launchers
- `pdflogo/setup_mac.sh` / `pdflogo/setup_windows.bat` - Dependency installers
- `pdflogo/requirements.txt` - Python dependencies

## License

MIT License. See `LICENSE`.
