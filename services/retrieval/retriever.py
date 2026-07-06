from services.embeddings.embedding_service import EmbeddingService
from services.vector_db.chroma_service import ChromaService

from models.retrieved_document import RetrievedDocument


class Retriever:

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.vector_db = ChromaService()

    def _generate_query_embedding(
        self,
        query: str
    ) -> list[float]:
        """
        Generate an embedding for the user's query.
        """

        return self.embedding_service.generate_embedding(query)

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ) -> list[RetrievedDocument]:
        """
        Retrieve the most relevant documents from the vector database.
        """

        query_embedding = self._generate_query_embedding(query)

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