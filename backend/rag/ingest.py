import uuid
from rag.loaders.universal_loader import UniversalLoader
from rag.utils.text_splitter import TextSplitter
from rag.embeddings.embedding_model import EmbeddingModel
from rag.vectorstore.chroma_store import ChromaDB

class RAGIngestor:
    def __init__(self):
        self.embedder = EmbeddingModel()
        self.vectorstore = ChromaDB()

    def ingest_file(self, file_path: str):
        # 1. Load text
        text = UniversalLoader.load(file_path)

        # 2. Split text
        chunks = TextSplitter.split_text(text)

        # 3. Embed + store
        for chunk in chunks:
            embedding = self.embedder.embed(chunk)
            doc_id = str(uuid.uuid4())
            self.vectorstore.add_document(doc_id, chunk, embedding)

        return {"status": "success", "chunks_added": len(chunks)}
