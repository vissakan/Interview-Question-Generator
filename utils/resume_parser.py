import io


def extract_text(file_obj, filename: str) -> str:
    """Extract plain text from PDF, DOCX, or TXT resume files."""
    try:
        if filename.endswith('.pdf'):
            return _extract_pdf(file_obj)
        elif filename.endswith('.docx'):
            return _extract_docx(file_obj)
        elif filename.endswith('.txt'):
            return file_obj.read().decode('utf-8', errors='ignore')
    except Exception as e:
        raise RuntimeError(f"Failed to parse resume: {e}")
    return ''


def _extract_pdf(file_obj) -> str:
    import pdfplumber
    text_parts = []
    with pdfplumber.open(io.BytesIO(file_obj.read())) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
    return '\n'.join(text_parts)


def _extract_docx(file_obj) -> str:
    from docx import Document
    doc = Document(io.BytesIO(file_obj.read()))
    return '\n'.join([para.text for para in doc.paragraphs if para.text.strip()])
