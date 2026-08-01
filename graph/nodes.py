from core.service_container import ServiceContainer
from graph.state import AgentState



class GraphNodes:
    """
    LangGraph node implementations.

    Each node is responsible only for orchestrating a single step.
    All business logic lives inside the services.
    """

    def __init__(self, container: ServiceContainer) -> None:
        self.container = container
        
        
    def load_conversation_node(
        self,
        state: AgentState,
    ) -> dict:


        history = self.container.conversation_manager.get_history(
            session_id=state["session_id"],
        )

        window = self.container.conversation_window.build(history)

        conversation_history =  self.container.history_formatter.format(
            window
        )

        return {
            "conversation_history": conversation_history,
        }
        

    def rewrite_query_node(self, state: AgentState) -> dict:
        

        rewritten_question = self.container.query_rewriter.rewrite(
            question=state["question"],
            conversation_history=state["conversation_history"],
        )

        return {
            "rewritten_question": rewritten_question,
        }
        
            
            
    def retrieve_memory_node(self, state: AgentState) -> dict:
        
        
        retrieved_memories = self.container.memory_service.retrieve_memories(
            query = state["rewritten_question"],
            session_id = state["session_id"],
        )
        
        return {
            "retrieved_memories" : retrieved_memories
        }
        
    
    def agent_guardrail_node(
        self,
        state: AgentState,
    ) -> dict:


        result = (
            self.container.agent_guardrail_service.validate(
                question=state["question"],
            )
        )

        return {
            "guardrail_result": result,
        }
    
        
        
    def retrieve_rag_node(self, state: AgentState,) -> dict:
        

        retrieval_response = self.container.rag_service.retrieve(
            query=state["rewritten_question"]
        )

        retrieval_context = (
            self.container.rag_service.build_retrieval_context(
                rewritten_question=state["rewritten_question"],
                retrieval_response=retrieval_response,
            )
        )

        return {
            "retrieval_context": retrieval_context,
        }
        
        
    
    def plan_node(
        self,
        state: AgentState,
    ) -> dict:
        
        planner_result = self.container.planner_service.plan(
            query=state["rewritten_question"]
        )
        
        print(planner_result)

        return {
            "planner_result": planner_result,
        }
        
    
    
    def execute_tool_node(
        self,
        state: AgentState,
    ) -> dict:

        planner_result = state["planner_result"]
        
        retrieval_context = state["retrieval_context"]

        tool_request = planner_result.tool_request
        
        if tool_request is None:
            raise ValueError(
                "Planner returned no tool request."
            )

        tool_result = self.container.tool_executor.execute(
            request=tool_request,
            session_id=state["session_id"],
            conversation_history=state["conversation_history"],
            semantic_memories=state["retrieved_memories"],
            retrieval_context=retrieval_context,
        )

        return {
            "tool_result": tool_result,
        }
        
        
    def generate_answer_node(
        self,
        state: AgentState,
    ) -> dict:
        
        planner_result = state["planner_result"]
        
        if planner_result.type == "answer":
            
            return {
                "final_answer" : planner_result.response
            }
        
        response = (
            self.container.response_generation_service.generate_from_tool(
                question= state["question"],
                tool_request= planner_result.tool_request,
                tool_result= state["tool_result"],
            )
        )
        
        return {
            "final_answer" : response,
            "citations": state["tool_result"].metadata.get("citations", []),
        }
        
        
    def validate_output_node(
        self,
        state: AgentState,
    ) -> dict:

        validated_response = (
            self.container.output_validation_service.validate(
                response=state["final_answer"],
            )
        )

        return {
            "final_answer": validated_response,
        }
        
        
    def finalize_response_node(
        self,
        state: AgentState,
    ) -> dict:
        
        self.container.response_finalization_service.finalize(
            session_id=state["session_id"],
            question=state["question"],
            response=state["final_answer"],
        )
        

        return {}
    
    
    def blocked_response_node(
        self,
        state: AgentState,
    ) -> dict:

        guardrail_result = state["guardrail_result"]

        if guardrail_result.allowed:
            raise ValueError(
                "blocked_response_node called for an allowed request."
            )

        return {
            "final_answer": (
                "Prompt injection detected : I can't process requests that attempt to manipulate or override my instructions."

                "I'm only able to answer healthcare-related questions. "
                f"{guardrail_result.reason}"
            )
        }
    
    
    def guardrails_node(self, state: AgentState) -> dict:
        
        guardrail_result = (
            self.container.knowledgebase_guardrail_service.validate(
                question=state["rewritten_question"],
                semantic_memories=state["retrieved_memories"],
            )
        )
        return {
            "guardrail_result": guardrail_result,
        }
