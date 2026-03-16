# PDF Logo Adder

A Python script and web app to add a logo image to PDF files. It can process single PDF files or batch process all PDFs in a folder. The logo is placed at the top of each page, and existing content is automatically shifted down to make room.

## Requirements

- Python 3.6+
- PyMuPDF (install via pip)
- Flask (for web app)

## Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Command Line

#### Single PDF File

```
python add_logo.py --input path/to/input.pdf --logo path/to/logo.png --output path/to/output.pdf
```

#### Batch Process Folder

```
python add_logo.py --input path/to/pdf_folder --logo path/to/logo.png --output path/to/output_folder
```

### Web App

Run the web application locally:

```
python app.py
```

Then open your browser and go to `http://localhost:5000`

The web app allows you to:

- Upload PDF and logo files
- Set logo position and scale
- Download the processed PDF

You can share the local URL with friends via WhatsApp, and they can use the app on your machine.

### Options

- `--input`: Path to input PDF file or folder containing PDFs
- `--logo`: Path to logo image (PNG, JPG, etc.) - required
- `--output`: Path to output PDF file or folder (optional, defaults to input_with_logo.pdf or input/output)
- `--position`: Logo position as x y coordinates in points from top-left (default: 0 0)
- `--scale`: Logo scale factor (default: 0.5, meaning 50% of original size)

## Example

Assuming you have PDFs in `c:\Users\adeel\Desktop\pdfs\` and logo at `c:\Users\adeel\Desktop\logo.png`:

```
python add_logo.py --input c:\Users\adeel\Desktop\pdfs --logo c:\Users\adeel\Desktop\logo.png
```

This will create a folder `c:\Users\adeel\Desktop\pdfs\output` with modified PDFs.

## Notes

- Position (0,0) is top-left of the page
- Coordinates are in points (1/72 inch)
- Supported logo formats: PNG, JPG, JPEG, etc.
- Original PDFs are not modified; new files are created
- Each page height is increased to accommodate the logo + original content
- Web app runs locally on port 5000
