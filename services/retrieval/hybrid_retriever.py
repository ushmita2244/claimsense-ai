from core.config.settings import settings
from models.retrieval_response import RetrievalResponse
from services.embeddings.embedding_service import EmbeddingService
from services.retrieval.base_retriever import BaseRetriever
from services.retrieval.retriever import Retriever
from services.retrieval.bm25_service import BM25Service
from services.retrieval.score_fusion_service import ScoreFusionService

from models.retrieved_document import RetrievedDocument


class HybridRetriever(BaseRetriever):
    """
    Hybrid retriever combining vector search and BM25 search.
    """

    def __init__(self):

        self.vector_retriever = Retriever()

        self.bm25_service = BM25Service()

        self.score_fusion = ScoreFusionService()

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ) -> RetrievalResponse:
        """
        Retrieve documents using both vector search and BM25,
        then combine the rankings using Reciprocal Rank Fusion.
        """

        # ==========================================
        # Vector Search
        # ==========================================

        vector_response = self.vector_retriever.retrieve(
            query=query,
            top_k=top_k
        )

        # ==========================================
        # BM25 Search
        # ==========================================

        bm25_documents = self.bm25_service.search(
            query=query,
            top_k=top_k
        )

        # ==========================================
        # Fuse Rankings
        # ==========================================
        
        hybrid_documents = self.score_fusion.fuse(
            vector_documents=vector_response.documents,
            bm25_documents=bm25_documents,
            top_k=top_k,
            vector_weight=settings.VECTOR_WEIGHT,
            bm25_weight=settings.BM25_WEIGHT,
            rrf_constant=settings.RRF_CONSTANT
        )

        # ==========================================
        # Return Retrieval Response
        # ==========================================

        return RetrievalResponse(
            documents=hybrid_documents,
            embedding_time=vector_response.embedding_time,
            retrieval_time=vector_response.retrieval_time
        )