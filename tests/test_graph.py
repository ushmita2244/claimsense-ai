from graph.graph_service import GraphService
from graph.state import AgentState
from pprint import pprint
from core.service_container import ServiceContainer

def main():

    container = ServiceContainer()
    graph = GraphService(container=container)
    

    state = AgentState(
        question="What is Lung Cancer, give its 2 causes.",
        session_id="test-session",
        conversation_history="",
    )

    result = graph.run(state)

    print("\n========== RESULT ==========\n")
    print(result["final_answer"])
    pprint(result)


if __name__ == "__main__":
    main()