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
from services.memory.conversation_manager import ConversationManager
from services.memory.history_formatter import HistoryFormatter
from services.rewriting.query_rewriter import QueryRewriter
from services.memory.conversation_window import ConversationWindow
from services.guardrails.guardrail_service import GuardrailService

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
        self.guardrail = GuardrailService()
        self.conversation_manager = ConversationManager()
        self.conversation_window = ConversationWindow(
            max_messages=6
        )
        self.query_rewriter = QueryRewriter()


    @opik.track(
    type="general",
    project_name=settings.OPIK_PROJECT_NAME
    )
    def ask(
        self,
        question: str,
        session_id: str = "default"
    ) -> RAGResponse:
        """
        Answer a user's question using Retrieval-Augmented Generation.
        """

        with Timer() as total_timer:
            
            # ==========================================
            # Guardrail Validation
            # ==========================================

            guardrail_result = self.guardrail.validate(
                question
            )
            
            if not guardrail_result.allowed:

                return RAGResponse(
                    question=question,
                    retrieved_documents=[],
                    evaluation=None,
                    answer=guardrail_result.reason
                )
            
            # ==========================================
            # Store User Message
            # ==========================================

            self.conversation_manager.add_user_message(
                session_id=session_id,
                content=question
            )
            
            # ==========================================
            # Get Conversation History
            # ==========================================

            history = self.conversation_manager.get_history(
                session_id
            )
            
            # ==========================================
            # Build Conversation Window
            # ==========================================
            
            window_history = self.conversation_window.build(
                history
            )

            # ==========================================
            # Format Conversation History
            # ==========================================

            formatted_history = HistoryFormatter.format(
                window_history
            )
            # ==========================================
            # Rewrite Question
            # ==========================================

            rewritten_question = self.query_rewriter.rewrite(
                question=question,
                conversation_history=formatted_history
            )

            # Retrieval
            
            with Timer() as timer:

                retrieval_response = self.retriever.retrieve(
                    query=rewritten_question
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
                    context=retrieved_documents,
                    conversation_history=formatted_history
                )
            prompt_time = timer.elapsed

            # LLM
            with Timer() as timer:
                answer = self.llm.generate_response(prompt)
            llm_time = timer.elapsed
            
            # ==========================================
            # Store  Assistant Message
            # ==========================================
            
            self.conversation_manager.add_assistant_message(
            session_id=session_id,
            content=answer
            )

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
        "rewritten_question": rewritten_question,
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
        "guardrail_allowed": guardrail_result.allowed,
        "guardrail_reason": guardrail_result.reason
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