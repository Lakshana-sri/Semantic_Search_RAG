
import os
import pymupdf
from docx import Document
from bs4 import BeautifulSoup

def load_document(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        pdf = pymupdf.open(file_path)
        text = "\n".join(page.get_text() for page in pdf)
        pdf.close()

    elif extension == ".docx":
        document = Document(file_path)
        text = "\n".join(
            paragraph.text for paragraph in document.paragraphs
        )

    elif extension == ".html":
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file.read(), "html.parser")

        for element in soup(["script", "style"]):
            element.decompose()

        text = soup.get_text(separator="\n", strip=True)

    else:
        return ""

    return text.strip()


def load_all_documents(folder):

    documents = []

    for filename in os.listdir(folder):

        file_path = os.path.join(folder, filename)

        if not os.path.isfile(file_path):
            continue

        if filename.lower().endswith((".pdf", ".docx", ".html")):

            text = load_document(file_path)

            if text:
                documents.append({
                    "filename": filename,
                    "file_type": os.path.splitext(filename)[1].lower(),
                    "text": text,
                    "word_count": len(text.split())
                })

    return documents