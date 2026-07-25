from models.tool_definition import ToolDefinition
from models.tool_parameter import ToolParameter
from models.tool_result import ToolResult

from services.rag.rag_service import RAGService
from services.tools.base_tool import BaseTool


class KnowledgeBaseTool(BaseTool):
    """
    Tool that answers questions using the enterprise healthcare
    knowledge base through the RAG pipeline.
    """

    def __init__(
        self,
        rag_service: RAGService
    ):
        self.rag_service = rag_service

    @property
    def definition(self) -> ToolDefinition:

        return ToolDefinition(
            name="knowledge_base",
            description=(
                "Answers questions using the enterprise healthcare "
                "knowledge base."
            ),
            parameters=[
                ToolParameter(
                    name="question",
                    description="The user's question.",
                    type="string",
                    required=True
                ),
                ToolParameter(
                    name="session_id",
                    description="Conversation session identifier.",
                    type="string",
                    required=False,
                ),
            ]
        )

    def execute(
        self,
        **kwargs
    ) -> ToolResult:

        question = kwargs["question"]
        
        session_id = kwargs.get(
            "session_id",
            "default"
        )

        response = self.rag_service.ask(
            question=question,
            session_id=session_id
        )

        return ToolResult(
            output=response.answer,
            metadata={
                "retrieved_documents": response.retrieved_documents,
                "evaluation": response.evaluation
            }
        )