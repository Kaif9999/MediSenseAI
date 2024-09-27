import PyPDF2
import streamlit as st

def handle_pdf_upload(pdf_file) -> str:
    """
    Extract text from an uploaded PDF file.

    Args:
        pdf_file: The uploaded PDF file.

    Returns:
        str: Extracted text from the PDF.
    """
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        if not text.strip():
            st.error("No text found in the PDF.")
            return ""
        return text
    except Exception as e:
        st.error(f"Failed to process PDF file: {e}")
        return ""