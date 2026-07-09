import time
from core.utils.timer import Timer
from services.prompts.rag_prompt import RAGPrompt
from services.embeddings.embedding_service import EmbeddingService
from services.llm.gemini_service import GeminiService
from services.retrieval.retriever import Retriever
from services.evaluation.diagnostics_service import DiagnosticsService

from models.rag_response import RAGResponse
from models.performance_metrics import PerformanceMetrics


class RAGService:
    """
    Retrieval-Augmented Generation Service.
    """

    def __init__(self):

        self.embedding_service = EmbeddingService()
        self.retriever = Retriever()
        self.llm = GeminiService()
        self.diagnostics = DiagnosticsService()

    def ask(
        self,
        question: str
    ) -> RAGResponse:
        """
        Answer a user's question using Retrieval-Augmented Generation.
        """

        with Timer() as total_timer:
            
            # Embedding
            with Timer() as timer:
                query_embedding = self.embedding_service.generate_embedding(question)
            embedding_time = timer.elapsed

            # Retrieval
            with Timer() as timer:
                retrieved_documents = self.retriever.retrieve(
                    query_embedding=query_embedding
                )
            retrieval_time = timer.elapsed

            # Diagnostics
            diagnostics = self.diagnostics.analyze(retrieved_documents)

            # Prompt
            with Timer() as timer:
                prompt = RAGPrompt.build(
                    question=question,
                    context=retrieved_documents
                )
            prompt_time = timer.elapsed

            # LLM
            with Timer() as timer:
                answer = self.llm.generate_response(prompt)
            llm_time = timer.elapsed

        total_time = total_timer.elapsed
            # ==================================================
            # Performance Metrics
            # ==================================================

        performance = PerformanceMetrics(
            embedding_time=embedding_time,
            retrieval_time=retrieval_time,
            prompt_time=prompt_time,
            llm_time=llm_time,
            total_time=total_time
        )

        # ==================================================
        # Final Response
        # ==================================================

        return RAGResponse(
            question=question,
            retrieved_documents=retrieved_documents,
            diagnostics=diagnostics,
            performance=performance,
            answer=answer
        )