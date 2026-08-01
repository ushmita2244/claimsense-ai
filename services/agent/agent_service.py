from graph.graph_service import GraphService
from graph.state import AgentState
from models.agent_response import AgentResponse

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
    ) -> AgentResponse:

        state: AgentState = {
            "question": prompt,
            "original_question": prompt,
            "session_id": session_id,
        }

        graph_response = self.graph_service.run(state)

        return AgentResponse(
            answer=graph_response.state["final_answer"],
            insights=graph_response.insights,
            citations=graph_response.citations,
        )