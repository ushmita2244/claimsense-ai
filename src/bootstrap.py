from pathlib import Path

from services.agent.agent_service import AgentService

from services.llm.gemini_service import GeminiService
from services.rag.rag_service import RAGService

from services.tools.calculator_tool import CalculatorTool
from services.tools.knowledge_base_tool import KnowledgeBaseTool
from services.tools.sql_tool import SQLTool

from services.tools.tool_executor import ToolExecutor
from services.tools.tool_registry import ToolRegistry
from services.guardrails.agent_guardrail_service import AgentGuardrailService
from services.tools.medical_web_search_tool import (
    MedicalWebSearchTool,
)

DATABASE_PATH = Path("data/healthcare.db")


def build_agent() -> AgentService:
    """
    Build and configure the complete AI agent.

    Returns:
        Fully configured AgentService.
    """

    # ==========================================
    # Core Services
    # ==========================================

    llm = GeminiService()

    rag_service = RAGService()
    
    agent_guardrail = AgentGuardrailService()

    # ==========================================
    # Tools
    # ==========================================

    calculator_tool = CalculatorTool()

    sql_tool = SQLTool(
        database_path=DATABASE_PATH
    )

    knowledge_base_tool = KnowledgeBaseTool(
        rag_service=rag_service
    )
    
    medical_web_search = MedicalWebSearchTool()

    # ==========================================
    # Tool Registry
    # ==========================================

    registry = ToolRegistry()

    registry.register_tool(calculator_tool)

    registry.register_tool(sql_tool)

    registry.register_tool(knowledge_base_tool)
    
    registry.register_tool(medical_web_search)

    # ==========================================
    # Tool Executor
    # ==========================================

    tool_executor = ToolExecutor(
        registry=registry
    )

    # ==========================================
    # Agent
    # ==========================================

    return AgentService(
        llm=llm,
        tool_executor=tool_executor,
        agent_guardrail=agent_guardrail
    )