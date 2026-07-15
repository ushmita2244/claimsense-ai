
from core.utils.timer import Timer
from models.retrieval_response import RetrievalResponse
from services.vector_db.chroma_service import ChromaService
from models.retrieved_document import RetrievedDocument
import opik
from services.retrieval.base_retriever import BaseRetriever
from services.embeddings.embedding_service import EmbeddingService


class Retriever(BaseRetriever):

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.vector_db = ChromaService()

    @opik.track(
        type = "tool"
    )
    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ) -> RetrievalResponse:
        
        """
        Retrieve the most relevant documents from the vector database.
        """
        
        with Timer() as timer:

            query_embedding = self.embedding_service.generate_embedding(
                query
            )

        embedding_time = timer.elapsed
        

        with Timer() as timer:

            results = self.vector_db.search(
                query_embedding=query_embedding,
                top_k=top_k
            )

        retrieval_time = timer.elapsed

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

        return RetrievalResponse(
            documents=retrieved_documents,

            embedding_time=embedding_time,

            retrieval_time=retrieval_time
        )