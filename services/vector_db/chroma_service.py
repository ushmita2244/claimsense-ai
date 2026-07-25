from chromadb import PersistentClient
import opik

class ChromaService:

    def __init__(self, collection_name: str = "healthcare_knowledge"):
        
        self.collection_name = collection_name
        
        self.client = PersistentClient(
            path="data/chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )

    def clear(self):
        try:
            self.client.delete_collection(self.collection_name)
        except Exception:
            pass

        self.collection = self.client.get_or_create_collection(
            name=self.collection_name
        )

    def add_document(self, doc_id: str, text: str, embedding: list[float], metadata: dict | None = None):
        self.collection.add(
            ids=[doc_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata or {}]
        )
        
    @opik.track(
    type = "tool"
    )
    def search(
        self,
        query_embedding: list[float],
        top_k: int = 3,
        where: dict | None = None,
        ):

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where,
            include=[ "documents", "metadatas", "distances" ],
        )
    
    def count(self):

        return self.collection.count()