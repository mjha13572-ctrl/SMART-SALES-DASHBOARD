import pandas as pd
import pdfplumber
from docx import Document
import os


def load_file(uploaded_file):
    """
    Reads CSV, Excel, PDF and DOCX files.
    Returns a Pandas DataFrame.
    """

    extension = os.path.splitext(uploaded_file.name)[1].lower()

    if extension == ".csv":
        return pd.read_csv(uploaded_file)

    elif extension in [".xlsx", ".xls"]:
        return pd.read_excel(uploaded_file)

    elif extension == ".pdf":
        return extract_pdf(uploaded_file)

    elif extension == ".docx":
        return extract_docx(uploaded_file)

    else:
        raise ValueError("Unsupported file type.")
    
def extract_pdf(uploaded_file):

    with pdfplumber.open(uploaded_file) as pdf:

        text = ""

        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return pd.DataFrame({"Extracted_Text": [text]})

def extract_docx(uploaded_file):

    doc = Document(uploaded_file)

    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    return pd.DataFrame({"Extracted_Text": text})   