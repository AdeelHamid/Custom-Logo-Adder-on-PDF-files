from flask import Flask, request, render_template, send_file, flash, redirect, url_for
import os
import tempfile
import fitz
from add_logo import add_logo_to_pdf

app = Flask(__name__)
app.secret_key = 'pdf-logo-app-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'pdf' not in request.files or 'logo' not in request.files:
        flash('Both PDF and logo files are required')
        return redirect(url_for('index'))

    pdf_file = request.files['pdf']
    logo_file = request.files['logo']

    if pdf_file.filename == '' or logo_file.filename == '':
        flash('No files selected')
        return redirect(url_for('index'))

    # Get parameters
    try:
        pos_x = float(request.form.get('pos_x', 0))
        pos_y = float(request.form.get('pos_y', 0))
        scale = float(request.form.get('scale', 0.5))
    except ValueError:
        flash('Invalid position or scale values')
        return redirect(url_for('index'))

    # Create temp files
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf:
        pdf_file.save(temp_pdf.name)
        temp_pdf_path = temp_pdf.name

    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(logo_file.filename)[1]) as temp_logo:
        logo_file.save(temp_logo.name)
        temp_logo_path = temp_logo.name

    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_output:
        temp_output_path = temp_output.name

    try:
        # Process the PDF
        add_logo_to_pdf(temp_pdf_path, temp_logo_path, temp_output_path, position=(pos_x, pos_y), scale=scale)

        # Return the processed file
        return send_file(temp_output_path, as_attachment=True, download_name=f"with_logo_{pdf_file.filename}")

    except Exception as e:
        flash(f'Error processing files: {str(e)}')
        return redirect(url_for('index'))
    finally:
        # Clean up temp files
        try:
            os.unlink(temp_pdf_path)
            os.unlink(temp_logo_path)
            # Don't delete temp_output_path as send_file needs it
        except:
            pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)