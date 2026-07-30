from core.service_container import ServiceContainer
from graph.graph_service import GraphService
from services.agent.agent_service import AgentService


def build_agent() -> AgentService:

    container = ServiceContainer()

    graph_service = GraphService(container)

    return AgentService(
        graph_service=graph_service,
    )