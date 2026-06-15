from rag.embeddings.embedder import Embedder
from rag.vectorstore.chroma_store import ChromaDB

class RAGQueryEngine:
    def __init__(self):
        self.embedder = Embedder()
        self.vectorstore = ChromaDB()

    def query(self, question: str, top_k: int = 3):
        # 1. Embed the question
        query_embedding = self.embedder.embed_text(question)

        # 2. Search vectorstore
        results = self.vectorstore.search(query_embedding, top_k=top_k)

        # 3. Format results
        docs = results.get("documents", [[]])[0]
        ids = results.get("ids", [[]])[0]

        return {
            "question": question,
            "results": [
                {"id": ids[i], "text": docs[i]}
                for i in range(len(docs))
            ]
        }
