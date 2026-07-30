from graph.graph_service import GraphService
from graph.state import AgentState

class AgentService:

    def __init__(
        self,
        graph_service: GraphService,
    ):
        self.graph_service = graph_service

    def generate_response(
        self,
        prompt: str,
        session_id: str = "default",
    ) -> str:

        state: AgentState = {
            "question": prompt,
            "original_question": prompt,
            "session_id": session_id,
        }

        result = self.graph_service.run(state)

        return result["final_answer"]