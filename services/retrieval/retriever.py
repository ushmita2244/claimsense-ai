
from services.vector_db.chroma_service import ChromaService
from models.retrieved_document import RetrievedDocument
import opik


class Retriever:

    def __init__(self):

        self.vector_db = ChromaService()

    @opik.track(
        type = "retrieval"
    )
    def retrieve(
        self,
        query_embedding: list[float],
        top_k: int = 3
    ) -> list[RetrievedDocument]:
        """
        Retrieve the most relevant documents from the vector database.
        """

        results = self.vector_db.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        retrieved_documents = []

        for text, metadata, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        ):

            document = RetrievedDocument(
                text=text,
                source=metadata["source"],
                chunk_number=metadata["chunk_number"],
                distance=distance
            )

            retrieved_documents.append(document)

        return retrieved_documents