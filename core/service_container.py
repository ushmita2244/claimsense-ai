from services.memory.memory_service import MemoryService
from services.rewriting.query_rewriter import QueryRewriter
from services.rag.rag_service import RAGService
from services.planner.planner_service import PlannerService
from services.llm.gemini_service import GeminiService
from services.tools.tool_executor import ToolExecutor
from services.tools.tool_registry import ToolRegistry
from services.tools.calculator_tool import CalculatorTool
from services.tools.sql_tool import SQLTool
from services.tools.knowledge_base_tool import KnowledgeBaseTool
from services.tools.medical_web_search_tool import MedicalWebSearchTool
from core.config.settings import settings
from services.response.response_generation_service import ResponseGenerationService
from services.validation.output_validation_service import OutputValidationService
from services.response.response_finalization_service import ResponseFinalizationService
from services.guardrails.output_guardrail_service import OutputGuardrailService
from services.memory.conversation_manager import ConversationManager
from services.web_search.web_search_service import WebSearchService
from services.guardrails.knowledgebase_guardrail_service import KnowledgeBaseGuardrailService


class ServiceContainer:
    """
    Lazily creates and manages application services.

    Each service is instantiated only once and reused
    throughout the application's lifetime.
    """

    def __init__(self) -> None:

        self._query_rewriter: QueryRewriter | None = None
        self._memory_service: MemoryService | None = None
        self._rag_service: RAGService | None = None
        self._llm: GeminiService | None = None
        self._tool_executor: ToolExecutor | None = None
        self._tool_registry: ToolRegistry | None = None
        self._planner_service: PlannerService | None = None
        self._response_generation_service: ResponseGenerationService | None = None
        self._output_validation_service: OutputValidationService | None = None
        self._response_finalization_service: ResponseFinalizationService | None = None
        self._output_guardrail: OutputGuardrailService | None = None
        self._guardrail_service: KnowledgeBaseGuardrailService | None = None
        self._conversation_manager: ConversationManager | None = None
        self._web_search_service: WebSearchService | None = None

    # =====================================================
    # Query Rewriter
    # =====================================================

    @property
    def query_rewriter(self) -> QueryRewriter:

        if self._query_rewriter is None:
            self._query_rewriter = QueryRewriter()

        return self._query_rewriter

    # =====================================================
    # Memory Service
    # =====================================================

    @property
    def memory_service(self) -> MemoryService:

        if self._memory_service is None:
            self._memory_service = MemoryService()

        return self._memory_service
    
    # =====================================================
    # Rag Service
    # =====================================================
    
    @property
    def rag_service(self) -> RAGService:

        if self._rag_service is None:
            self._rag_service = RAGService()

        return self._rag_service
    
    
    @property
    def llm(self) -> GeminiService:

        if self._llm is None:
            self._llm = GeminiService()

        return self._llm
    
    
    @property
    def tool_registry(self) -> ToolRegistry:

        if self._tool_registry is None:

            registry = ToolRegistry()

            calculator_tool = CalculatorTool()

            sql_tool = SQLTool(
                database_path=settings.DATABASE_PATH
            )

            knowledge_base_tool = KnowledgeBaseTool(
                rag_service=self.rag_service
            )

            medical_web_search = MedicalWebSearchTool()

            registry.register_tool(calculator_tool)
            registry.register_tool(sql_tool)
            registry.register_tool(knowledge_base_tool)
            registry.register_tool(medical_web_search)

            self._tool_registry = registry

        return self._tool_registry
    
    
    @property
    def tool_executor(self) -> ToolExecutor:

        if self._tool_executor is None:

            self._tool_executor = ToolExecutor(
                registry=self.tool_registry
            )

        return self._tool_executor
    
    
    @property
    def planner_service(self):

        if self._planner_service is None:

            self._planner_service = PlannerService(
                llm=self.llm,
                tool_executor=self.tool_executor,
            )

        return self._planner_service
    
    
    @property
    def response_generation_service(
        self,
    ) -> ResponseGenerationService:

        if self._response_generation_service is None:

            self._response_generation_service = (
                ResponseGenerationService(
                    llm=self.llm,
                )
            )

        return self._response_generation_service
    
    
    @property
    def output_guardrail(
        self,
    ) -> OutputGuardrailService:

        if self._output_guardrail is None:

            self._output_guardrail = OutputGuardrailService()

        return self._output_guardrail
    
    
    @property
    def knowledgebase_guardrail_service(
        self,
    ) -> KnowledgeBaseGuardrailService:

        if self._guardrail_service is None:

            self._guardrail_service = (
                KnowledgeBaseGuardrailService()
            )

        return self._guardrail_service
    
    
    @property
    def output_validation_service(
        self,
    ) -> OutputValidationService:

        if self._output_validation_service is None:

            self._output_validation_service = (
                OutputValidationService(
                    output_guardrail=self.output_guardrail,
                )
            )

        return self._output_validation_service
    
    
    @property
    def conversation_manager(self) -> ConversationManager:

        if self._conversation_manager is None:

            self._conversation_manager = ConversationManager(
                memory_service=self.memory_service,
            )

        return self._conversation_manager
    
    
    @property
    def response_finalization_service(
        self,
    ) -> ResponseFinalizationService:

        if self._response_finalization_service is None:

            self._response_finalization_service = (
                ResponseFinalizationService(
                    conversation_manager=self.conversation_manager,
                    memory_service=self.memory_service,
                )
            )

        return self._response_finalization_service
    
    
    @property
    def web_search_service(self) -> WebSearchService:

        if self._web_search_service is None:
            self._web_search_service = WebSearchService()

        return self._web_search_service
    
