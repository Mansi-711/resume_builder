import pdfkit
import tempfile

def save_pdf(html_content):
    # Configure wkhtmltopdf settings
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
        'margin-top': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'margin-right': '0.5in',
    }

    # Generate PDF in a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
        pdf_path = f.name
    try:
        pdfkit.from_string(html_content, pdf_path, options=options)
        return pdf_path
    except Exception as e:
        raise RuntimeError(f"Failed to generate PDF: {e}")
