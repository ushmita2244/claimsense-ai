
from core.utils.timer import Timer
from services.evaluation.diagnostics_service import DiagnosticsService
from models.rag_response import RAGResponse
from models.performance_metrics import PerformanceMetrics
from services.evaluation.evaluation_service import EvaluationService
from services.evaluation.answer_statistics_service import AnswerStatisticsService

from core.config.settings import settings

from models.retrieval_response import RetrievalResponse
from services.retrieval.hybrid_retriever import HybridRetriever
from services.reranker.cross_encoder_reranker import CrossEncoderReranker
from services.reranker.relevance_filter import RelevanceFilter

from models.memory_models import RetrievedMemory
from models.retrieval_quality import RetrievalQuality

from services.answer_generation.kb_answer_generator import KBAnswerGenerator
from services.answer_generation.web_answer_generator import WebAnswerGenerator
from models.retrieval_context import RetrievalContext

class RAGService:
    """
    Retrieval-Augmented Generation Service.
    """

    def __init__(self):

        self.diagnostics = DiagnosticsService()
        self.evaluation = EvaluationService()
        self.answer_statistics = AnswerStatisticsService()
        self.retriever = HybridRetriever()
        self.reranker = CrossEncoderReranker()
        self.relevance_filter = RelevanceFilter()
        self.kb_generator = KBAnswerGenerator()
        self.web_generator = WebAnswerGenerator()

    def retrieve(
        self,
        query: str,
    ) -> RetrievalResponse:
        """
        Retrieve, rerank and filter documents.
        """

        retrieval_response = self.retriever.retrieve(
            query=query
        )

        reranked_documents = self.reranker.rerank(
            query=query,
            documents=retrieval_response.documents,
        )

        filtered_documents = self.relevance_filter.filter(
            documents=reranked_documents,
            score_threshold=settings.RERANK_SCORE_THRESHOLD,
            minimum_documents=settings.MINIMUM_CONTEXT_DOCUMENTS,
        )

        documents = [
            document.document
            for document in filtered_documents
        ]

        return RetrievalResponse(
            documents=documents,
            embedding_time=retrieval_response.embedding_time,
            retrieval_time=retrieval_response.retrieval_time,
        )
        
        
    def build_retrieval_context(
        self,
        rewritten_question: str,
        retrieval_response: RetrievalResponse,
    ) -> RetrievalContext:
                
        diagnostics = self.diagnostics.analyze(
            retrieval_response.documents
        )

        return RetrievalContext(
            rewritten_question=rewritten_question,
            retrieved_documents=retrieval_response.documents,
            diagnostics=diagnostics,
            embedding_time=retrieval_response.embedding_time,
            retrieval_time=retrieval_response.retrieval_time,
        )

    
    def generate_answer(
        self,
        question: str,
        context: RetrievalContext,
        conversation_history: str,
        semantic_memories: list[RetrievedMemory] | None,
    ) -> RAGResponse:
        
        rewritten_question = context.rewritten_question
        retrieved_documents = context.retrieved_documents
        diagnostics = context.diagnostics
        embedding_time = context.embedding_time
        retrieval_time = context.retrieval_time
        
        with Timer() as total_timer:
            
            # ==================================================
            # Answer Generation
            # ==================================================
            
            if diagnostics.retrieval_quality is RetrievalQuality.POOR:

                generation_result = self.web_generator.generate(
                    question=rewritten_question,
                    retrieved_documents=retrieved_documents,
                    conversation_history=conversation_history,
                    semantic_memories=semantic_memories,
                )

            else:

                generation_result = self.kb_generator.generate(
                    question=rewritten_question,
                    retrieved_documents=retrieved_documents,
                    conversation_history=conversation_history,
                    semantic_memories=semantic_memories,
                )

            answer = generation_result.answer

            answer_source = generation_result.answer_source

            citations = generation_result.citations

            retrieved_documents = generation_result.retrieved_documents

            prompt_time = generation_result.prompt_time

            llm_time = generation_result.llm_time
            

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
        
        
        # ==================================================
        # Final Response
        # ==================================================

        return RAGResponse(
            question=question,
            retrieved_documents=retrieved_documents,
            evaluation=evaluation,
            answer=answer,
            answer_source=answer_source,
        )
        
        