import uuid
import opik

from models.memory_models import (
    MemoryRecord,
    RetrieveMemoryRequest,
    RetrievedMemory,
)

from services.embeddings.embedding_service import EmbeddingService
from services.vector_db.chroma_service import ChromaService


class MemoryRepository:

    COLLECTION_NAME = "claimsense_memory"

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

        document = (
            f"Question: {record.question}\n\n"
            f"Answer: {record.answer}"
        )

        embedding = self.embedding_service.generate_embedding(
            document
        )

        self.chroma.add_document(
            doc_id=str(uuid.uuid4()),
            text=document,
            embedding=embedding,
            metadata={
                "session_id": record.session_id
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

        retrieved_memories = []

        for document, distance in zip(documents, distances):

            retrieved_memories.append(
                RetrievedMemory(
                    content=document,
                    score=distance,
                )
            )

        return retrieved_memories