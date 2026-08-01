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
                    "Retrieve enterprise healthcare knowledge from documents "
                    "and answer questions that require remembering information "
                    "from previous conversations (semantic memory)."
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
        
        conversation_history = kwargs.get(
            "conversation_history",
            ""
        )

        semantic_memories = kwargs.get(
            "semantic_memories",
            []
        )
        
        retrieval_context = kwargs["retrieval_context"]

        response = self.rag_service.generate_answer(
            question=question,
            context=retrieval_context,
            conversation_history=conversation_history,
            semantic_memories=semantic_memories,
        )

        return ToolResult(
            output=response.answer,
            metadata={
                "retrieved_documents": response.retrieved_documents,
                "evaluation": response.evaluation,
                "citations": response.citations,
            }
        )