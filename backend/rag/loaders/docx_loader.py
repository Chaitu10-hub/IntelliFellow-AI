from docx import Document

class DOCXLoader:
    @staticmethod
    def load(path: str) -> str:
        doc = Document(path)
        return "\n".join([p.text for p in doc.paragraphs])
