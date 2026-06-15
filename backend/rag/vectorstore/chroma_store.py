import chromadb

class ChromaDB:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="data/chroma")

        self.collection = self.client.get_or_create_collection(
            name="intellifellow_rag",
            metadata={"hnsw:space": "cosine"}
        )

    def add_document(self, doc_id: str, text: str, embedding: list):
        self.collection.add(
            ids=[doc_id],
            documents=[text],
            embeddings=[embedding]
        )

    def search(self, query_embedding: list, top_k: int = 3):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
