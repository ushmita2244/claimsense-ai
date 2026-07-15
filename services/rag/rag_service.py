import opik
from core.utils.timer import Timer
from models import retrieval_response
from services.prompts.rag_prompt import RAGPrompt
from services.embeddings.embedding_service import EmbeddingService
from services.llm.gemini_service import GeminiService
from services.retrieval.retriever import Retriever
from services.evaluation.diagnostics_service import DiagnosticsService

from models.rag_response import RAGResponse
from models.performance_metrics import PerformanceMetrics
from services.attribution.attribution_service import AttributionService
from services.evaluation.evaluation_service import EvaluationService
from services.evaluation.answer_statistics_service import AnswerStatisticsService
from opik import opik_context
from core.config.settings import settings
from opik import track

class RAGService:
    """
    Retrieval-Augmented Generation Service.
    """

    def __init__(self):

        self.retriever = Retriever()
        self.llm = GeminiService()
        self.diagnostics = DiagnosticsService()
        self.attribution = AttributionService()
        self.evaluation = EvaluationService()
        self.answer_statistics = AnswerStatisticsService()


    @opik.track(
    type="general",
    project_name=settings.OPIK_PROJECT_NAME
    )
    def ask(
        self,
        question: str
    ) -> RAGResponse:
        """
        Answer a user's question using Retrieval-Augmented Generation.
        """

        with Timer() as total_timer:
            

            # Retrieval
            
            with Timer() as timer:

                retrieval_response = self.retriever.retrieve(
                    query=question
                )

            retrieved_documents = retrieval_response.documents

            embedding_time = retrieval_response.embedding_time

            retrieval_time = retrieval_response.retrieval_time

            # Diagnostics
            
            diagnostics = self.diagnostics.analyze(retrieved_documents)
            
            #Citations
            
            citations = self.attribution.build(retrieved_documents)

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
        # Answer Statistics
        # ==================================================

        answer_statistics = self.answer_statistics.analyze(
            answer
        )

        
        # ==========================================
        # Evaluation Report
        # ==========================================

        evaluation = self.evaluation.build(
            diagnostics=diagnostics,
            performance=performance,
            citations=citations,
            answer_statistics=answer_statistics
        )
        
        opik_context.update_current_trace(
        metadata={
        "question": question,
        "retrieval_quality": diagnostics.retrieval_quality,
        "documents_retrieved": diagnostics.total_documents,
        "top_distance": diagnostics.top_distance,
        "average_distance": diagnostics.average_distance,
        "sources": diagnostics.sources,
        "answer_words": answer_statistics.word_count,
        "answer_characters": answer_statistics.character_count,
        "answer_lines": answer_statistics.line_count,
        "total_time": performance.total_time,
        "embedding_time": performance.embedding_time,
        "retrieval_time": performance.retrieval_time,
        "llm_time": performance.llm_time,
        },
        tags=[
        "rag",
        "gemini",
        "chromadb",
        "healthcare",
        "evaluation"
        ]
        )
        
        # ==================================================
        # Final Response
        # ==================================================

        return RAGResponse(
            question=question,
            retrieved_documents=retrieved_documents,
            evaluation=evaluation,
            answer=answer
        )