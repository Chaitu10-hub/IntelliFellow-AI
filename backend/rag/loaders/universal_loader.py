import os
from .pdf_loader import PDFLoader
from .docx_loader import DOCXLoader
from .txt_loader import TXTLoader

class UniversalLoader:
    @staticmethod
    def load(path: str) -> str:
        ext = os.path.splitext(path)[1].lower()

        if ext == ".pdf":
            return PDFLoader.load(path)
        elif ext == ".docx":
            return DOCXLoader.load(path)
        elif ext == ".txt":
            return TXTLoader.load(path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
