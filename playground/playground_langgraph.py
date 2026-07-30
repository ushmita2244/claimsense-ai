from graph.graph_service import GraphService

graph_service = GraphService()

result = graph_service.run(
    {
        "question": "What are its symptoms?",
        "conversation_history": """
User: Tell me about diabetes.
Assistant: Diabetes is a chronic disease.
""",
        "session_id": "test-session",
    }
)

print(result)