from langgraph.graph import END, StateGraph

from core.service_container import ServiceContainer
from graph.nodes import GraphNodes
from graph.state import AgentState


class GraphBuilder:
    """
    Responsible for constructing and compiling the LangGraph workflow.
    """

    def __init__(self, container: ServiceContainer) -> None:

        self.container = container
        self.nodes = GraphNodes(container)

    def route_after_plan(
        self,
        state: AgentState,
    ) -> str:

        return state["planner_result"].type
    
    def route_after_agent_guardrail(
        self,
        state: AgentState,
    ) -> str:

        if state["guardrail_result"].allowed:
            return "rewrite_query"

        return "blocked_response"
    
    
    def build(self):

        builder = StateGraph(AgentState)
        
        # Nodes
        
        builder.add_node(
            "load_conversation",
            self.nodes.load_conversation_node,
        )

        builder.add_node(
            "rewrite_query",
            self.nodes.rewrite_query_node,
        )
        
        builder.add_node(
            "retrieve_memory",
            self.nodes.retrieve_memory_node,
        )
        
        builder.add_node(
            "retrieve_rag",
            self.nodes.retrieve_rag_node,
        )
        
        builder.add_node(
            "agent_guardrail",
            self.nodes.agent_guardrail_node,
        )
        
        builder.add_node(
            "blocked_response",
            self.nodes.blocked_response_node
            )
        
        builder.add_node(
            "plan",
            self.nodes.plan_node,
        )
        
        builder.add_node(
            "execute_tool",
            self.nodes.execute_tool_node,
        )

        builder.add_node(
            "generate_answer",
            self.nodes.generate_answer_node,
        )
        
        builder.add_node(
            "validate_output",
            self.nodes.validate_output_node,
        )
        
        builder.add_node(
            "finalize_response",
            self.nodes.finalize_response_node,
        )
        
        # Entry
        
        builder.set_entry_point(
            "load_conversation",
        )
        
        # Edges
        
        builder.add_edge(
            "load_conversation",
            "agent_guardrail",
        )
        
        builder.add_edge(
            "rewrite_query",
            "retrieve_memory",
        )
        
        builder.add_edge(
            "retrieve_memory",
            "retrieve_rag",
        )
        
        builder.add_edge(
            "retrieve_rag",
            "plan",
        )
        
        builder.add_conditional_edges(
            "agent_guardrail",
            self.route_after_agent_guardrail,
            {
                "rewrite_query": "rewrite_query",
                "blocked_response": "blocked_response",
            },
        )
        
        builder.add_conditional_edges(
            "plan",
            self.route_after_plan,
            {
                "tool": "execute_tool",
                "answer": "generate_answer",
            },
        )
        
        builder.add_edge(
            "execute_tool",
            "generate_answer",
        )
        
        builder.add_edge(
            "generate_answer",
            "validate_output",
        )
        
        builder.add_edge(
            "validate_output",
            "finalize_response",
        )

        builder.add_edge(
            "blocked_response", "finalize_response"
            )
        
        builder.add_edge(
            "finalize_response",
            END,
        )

        return builder.compile()