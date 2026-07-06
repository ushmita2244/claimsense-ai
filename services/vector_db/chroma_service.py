from chromadb import PersistentClient

class ChromaService:

    def __init__(self):
        self.client = PersistentClient(
            path="data/chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name="healthcare_knowledge"
        )

    def clear(self):
        try:
            self.client.delete_collection("healthcare_knowledge")
        except Exception:
            pass

        self.collection = self.client.get_or_create_collection(
            name="healthcare_knowledge"
        )

    def add_document(self, doc_id: str, text: str, embedding: list[float], metadata: dict | None = None):
        self.collection.add(
            ids=[doc_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata or {}]
        )
    def search(self, query_embedding: list[float], top_k: int = 3):

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=[ "documents", "metadatas", "distances" ]
        )
    
    def count(self):

        return self.collection.count()