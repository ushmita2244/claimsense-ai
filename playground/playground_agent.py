from services.agent.agent_service import AgentService

from services.llm.gemini_service import GeminiService

from services.tools.tool_registry import ToolRegistry
from services.tools.tool_executor import ToolExecutor
from services.tools.calculator_tool import CalculatorTool
from services.tools.knowledge_base_tool import KnowledgeBaseTool
from services.rag.rag_service import RAGService


def main():

    registry = ToolRegistry()

    registry.register_tool(
        CalculatorTool()
    )
    
    registry.register_tool(
    KnowledgeBaseTool(
        RAGService()
    )
)

    tool_executor = ToolExecutor(
        registry
    )

    llm = GeminiService()

    agent = AgentService(
        llm=llm,
        tool_executor=tool_executor
    )

    queries = [

    "What is sqrt(144)?",

    "Calculate 5**8",

    "What is (2+3)*(4+5)",

    "Calculate 100/0",

    "Calculate abc+xyz",

    "Who is Elon Musk?",

    "Explain Gradient Descent.",
    
    "What is chemotherapy?",

    "Explain breast cancer staging.",
    
    "What are the causes of lung cancer?"
    
    ]

    for index, query in enumerate(queries, start=1):

        print("=" * 80)
        print(f"TEST {index}")
        print("=" * 80)

        print(f"\nUser Query:\n{query}\n")

        try:

            response = agent.generate_response(query)

            print("Final Response")
            print("-" * 80)
            print(response)

        except Exception as exc:

            print("ERROR")
            print("-" * 80)
            print(exc)


if __name__ == "__main__":
    main()