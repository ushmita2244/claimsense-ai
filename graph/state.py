from typing import TypedDict, Any

from models.memory_models import RetrievedMemory
from models.retrieval_response import RetrievalResponse
from models.planner_result import PlannerResult
from models.retrieval_context import RetrievalContext
from models.guardrail_result import GuardrailResult
from models.tool_result import ToolResult

class AgentState(TypedDict, total=False):

    # User input
    original_question: str
    question: str
    session_id: str
    
    # Guradrails
    guardrail_result: GuardrailResult | None
    
    # Conversation
    conversation_history: str

    # Query rewriting
    rewritten_question: str

    # Context
    retrieval_context: RetrievalContext
    retrieved_memories: list[RetrievedMemory]
    retrieval_response: RetrievalResponse

    # Planning
    plan: str
    planner_result: PlannerResult

    # Tool execution
    tool_result: ToolResult

    # Final response
    final_answer: str
    
    citations: list[Any]
    
    