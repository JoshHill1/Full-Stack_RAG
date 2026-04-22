import os
import csv
import io
import re
from PyPDF2 import PdfReader
from docx import Document

# def clean_text(text: str) -> str:
#     """
#     This function is to help visually see how the PDF is parsed. 
#     It is not required for the main parsing functionality, but it is useful for testing and debugging.
#     """
#     # Replace double newlines with a placeholder
#     text = text.replace("\n\n", "<<PARA>>")
#     # Replace single newlines with spaces
#     text = text.replace("\n", " ")
#     # Restore paragraph breaks
#     text = text.replace("<<PARA>>", "\n\n")
#     # Clean up any extra spaces
#     text = re.sub(r" +", " ", text)
#     return text.strip()
# Extract text from a PDF file, page by page. Images are skipped in a PDF
def parse_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return clean_text(text.strip())


# Extract text from a Word document, paragraph by paragraph. python-docx reads the .docx XML structure We join them with newlines to preserve the document's structure.
def parse_docx(file_path: str) -> str:
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text.strip()


# Read a plain text file. Straightforward. utf-8 encoding is explicitly used because Windows defaults to cp1252, which can choke on special characters.
def parse_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().strip()


def parse_csv(file_path: str) -> str:
    """
    Convert a CSV file into readable plain text.
    
    We turn each row into a comma-separated line. This isn't
    the fanciest approach, but it gives the LLM something
    readable to work with. For RAG purposes, flattened text
    works better than trying to preserve table structure.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [", ".join(row) for row in reader]
    return "\n".join(rows).strip()


def parse_file(file_path: str) -> str:
    """
    Main entry point. Detect file type by extension and
    route to the correct parser.

    It checks if the file exists, extracts the extension, 
    and calls the appropriate parsing function. 
    If the file type is unsupported, it raises a ValueError.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return parse_pdf(file_path)
    elif ext == ".docx":
        return parse_docx(file_path)
    elif ext == ".txt":
        return parse_txt(file_path)
    elif ext == ".csv":
        return parse_csv(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")