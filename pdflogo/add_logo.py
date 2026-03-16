import os
import fitz  # PyMuPDF
import argparse

def add_logo_to_pdf(input_pdf, logo_path, output_pdf, position=(0, 0), scale=0.5):
    """
    Add a logo image to each page of a PDF, shifting existing content down to make room.

    :param input_pdf: Path to the input PDF file
    :param logo_path: Path to the logo image file (PNG, JPG, etc.)
    :param output_pdf: Path to save the output PDF
    :param position: Tuple (x, y) for logo position in points (top-left origin for new pages)
    :param scale: Scale factor for the logo size (1.0 = original size)
    """
    # Open the PDF
    doc = fitz.open(input_pdf)

    # Load the logo image
    try:
        pix = fitz.Pixmap(logo_path)
    except Exception as e:
        print(f"Error loading logo: {e}")
        return

    logo_width = pix.width * scale
    logo_height = pix.height * scale

    # Create a new PDF document
    new_doc = fitz.open()

    # Process each page
    for page_num in range(len(doc)):
        page = doc[page_num]

        # Calculate new page height to accommodate logo + original content
        new_height = page.rect.height + logo_height

        # Create new page
        new_page = new_doc.new_page(width=page.rect.width, height=new_height)

        # Insert logo at the specified position
        logo_rect = fitz.Rect(position[0], position[1], position[0] + logo_width, position[1] + logo_height)
        new_page.insert_image(logo_rect, pixmap=pix)

        # Show the original page content shifted down below the logo
        content_rect = fitz.Rect(0, logo_height, page.rect.width, new_height)
        new_page.show_pdf_page(content_rect, doc, page_num)

    # Save the new PDF
    new_doc.save(output_pdf)
    new_doc.close()
    doc.close()
    pix = None  # Free memory

def process_folder(input_folder, logo_path, output_folder, position=(50, 50), scale=0.5):
    """
    Process all PDF files in a folder, adding the logo to each.

    :param input_folder: Folder containing PDF files
    :param logo_path: Path to the logo image
    :param output_folder: Folder to save modified PDFs
    :param position: Position for the logo
    :param scale: Scale for the logo
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            input_pdf = os.path.join(input_folder, filename)
            output_pdf = os.path.join(output_folder, f"with_logo_{filename}")
            print(f"Processing {filename}...")
            add_logo_to_pdf(input_pdf, logo_path, output_pdf, position, scale)
            print(f"Saved to {output_pdf}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add logo to PDF files")
    parser.add_argument("--input", help="Input PDF file or folder")
    parser.add_argument("--logo", required=True, help="Path to logo image")
    parser.add_argument("--output", help="Output PDF file or folder")
    parser.add_argument("--position", nargs=2, type=int, default=[50, 50], help="Logo position (x y) in points")
    parser.add_argument("--scale", type=float, default=0.5, help="Logo scale factor")

    args = parser.parse_args()

    if os.path.isfile(args.input):
        # Single file
        if not args.output:
            args.output = args.input.replace('.pdf', '_with_logo.pdf')
        add_logo_to_pdf(args.input, args.logo, args.output, tuple(args.position), args.scale)
        print(f"Logo added. Output: {args.output}")
    elif os.path.isdir(args.input):
        # Folder
        if not args.output:
            args.output = os.path.join(args.input, "output")
        process_folder(args.input, args.logo, args.output, tuple(args.position), args.scale)
        print(f"Processed all PDFs in {args.input}. Outputs in {args.output}")
    else:
        print("Invalid input path")