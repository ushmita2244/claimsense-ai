from core.service_container import ServiceContainer
from graph.graph_builder import GraphBuilder
from graph.state import AgentState
import opik
from core.config.settings import settings
from opik import opik_context
from models.agent_response import AIInsights
from models.graph_response import GraphResponse


class GraphService:

    def __init__(
        self,
        container: ServiceContainer,
    ) -> None:

        self.graph = GraphBuilder(
            container
        ).build()


    @opik.track(
        type="general",
        project_name=settings.OPIK_PROJECT_NAME,
    )
    def run(
        self,
        state: AgentState,
    ) -> GraphResponse:
        
        """
        Execute the LangGraph workflow and return the final agent state.
        """

        result = self.graph.invoke(state)
        
        retrieval_context = result.get("retrieval_context")
        guardrail_result = result.get("guardrail_result")
        planner_result = result.get("planner_result")
        tool_result = result.get("tool_result")
        
        knowledge_sources = (
            tool_result.knowledge_sources
            if tool_result
            else []
        )

        opik_context.update_current_trace(
            metadata={
                "session_id": result.get("session_id"),
                "question": result.get("question"),
                "rewritten_question": result.get("rewritten_question"),

                "documents_retrieved": (
                    len(retrieval_context.retrieved_documents)
                    if retrieval_context
                    else 0
                ),
                
                "embedding_time": (
                    retrieval_context.embedding_time
                    if retrieval_context
                    else None
                ),

                "retrieval_time": (
                    retrieval_context.retrieval_time
                    if retrieval_context
                    else None
                ),

                "memory_count": len(result.get("retrieved_memories", [])),

                "guardrail_allowed": (
                    guardrail_result.allowed
                    if guardrail_result
                    else None
                ),

                "guardrail_reason": (
                    guardrail_result.reason
                    if guardrail_result
                    else None
                ),

                "planner_type": (
                    planner_result.type
                    if planner_result
                    else None
                ),

                "tool_name": (
                    planner_result.tool_request.tool_name
                    if planner_result and planner_result.tool_request
                    else None
                ),
                
                "tool_metadata": (
                    tool_result.metadata
                    if tool_result
                    else {}
                ),

            },
            tags=["langgraph", "claimsense-ai"],
        )
        
        diagnostics = (
            retrieval_context.diagnostics
            if retrieval_context
            else None
        )

        insights = AIInsights(

            planner=(
                planner_result.type
                if planner_result
                else "-"
            ),

            tool=(
                planner_result.tool_request.tool_name
                if planner_result
                and planner_result.tool_request
                else "-"
            ),

            retrieval_quality=(
                diagnostics.retrieval_quality.name
                if diagnostics
                else "-"
            ),

            memory_count=len(
                result.get(
                    "retrieved_memories",
                    []
                )
            ),

            embedding_time=(
                retrieval_context.embedding_time
                if retrieval_context
                else 0.0
            ),

            retrieval_time=(
                retrieval_context.retrieval_time
                if retrieval_context
                else 0.0
            ),
            
            knowledge_sources=knowledge_sources,
        )
        
        citations = (
            tool_result.metadata.get("citations", [])
            if tool_result
            else []
        )

        return GraphResponse(
            state=result,
            insights=insights,
            citations=citations,
        )
        