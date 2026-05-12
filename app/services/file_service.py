import os
import fitz
from fastapi import UploadFile

UPLOAD_DIR = "uploads"

async def save_file(file: UploadFile):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    return file_path

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    pdf_document = fitz.open(file_path)
    for page in pdf_document:
        text += page.get_text()

    pdf_document.close()
    return text

def read_text_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()