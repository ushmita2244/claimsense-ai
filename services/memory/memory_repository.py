import uuid
import opik

from models.memory_models import (
    MemoryRecord,
    RetrieveMemoryRequest,
    RetrievedMemory,
)

from services.embeddings.embedding_service import EmbeddingService
from services.vector_db.chroma_service import ChromaService
from models.memory_category import MemoryCategory


class MemoryRepository:

    COLLECTION_NAME = "claimsense_memory"
    SIMILARITY_THRESHOLD = 0.8

    def __init__(
        self,
        chroma_service: ChromaService | None = None,
        embedding_service: EmbeddingService | None = None,
    ):

        self.chroma = (
            chroma_service
            if chroma_service is not None
            else ChromaService(
                collection_name=self.COLLECTION_NAME
            )
        )

        self.embedding_service = (
            embedding_service
            if embedding_service is not None
            else EmbeddingService()
        )

    @opik.track(type="tool")
    def store(
        self,
        record: MemoryRecord,
    ) -> None:
        """
        Stores one conversation as semantic memory.
        """

        document = record.memory
        
        # ===== DEBUG =====
        print("\n========== STORING MEMORY ==========")
        print(document)
        print(f"Session ID: {record.session_id}")
        print("====================================")
    
        embedding = self.embedding_service.generate_embedding(
            document
        )

        self.chroma.add_document(
            doc_id=str(uuid.uuid4()),
            text=document,
            embedding=embedding,
            metadata={
                "session_id": record.session_id,
                "category": record.category.value,
            },
        )

    @opik.track(type="tool")
    def retrieve(
        self,
        request: RetrieveMemoryRequest,
    ) -> list[RetrievedMemory]:
        """
        Retrieves the most relevant memories for a session.
        """

        query_embedding = self.embedding_service.generate_embedding(
            request.query
        )

        results = self.chroma.search(
            query_embedding=query_embedding,
            top_k=request.top_k,
            where={
                "session_id": request.session_id
            },
        )

        documents = results.get("documents", [[]])[0]
        distances = results.get("distances", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        retrieved_memories = []

        for document, distance, metadata in zip(documents, distances, metadatas):
            
            if distance > self.SIMILARITY_THRESHOLD:
                continue

            retrieved_memories.append(
                RetrievedMemory(
                    content=document,
                    score=distance,
                    category=MemoryCategory(metadata["category"]),
                )
            )
            
        print("\n===== DEBUG RETRIEVED MEMORIES =====")

        for memory in retrieved_memories:
            print(memory.content)
            print(memory.score)

        print("==============================")

        return retrieved_memories