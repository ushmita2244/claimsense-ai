from models.tool_request import ToolRequest
from services.tools.calculator_tool import CalculatorTool
from services.tools.tool_executor import ToolExecutor
from services.tools.tool_registry import ToolRegistry
from services.tools.knowledge_base_tool import KnowledgeBaseTool
from services.rag.rag_service import RAGService


def main():

    # ==========================================
    # Register Tools
    # ==========================================

    registry = ToolRegistry()

    registry.register_tool(
        CalculatorTool()
    )
    
    registry.register_tool(
    KnowledgeBaseTool(RAGService())
    )

    # ==========================================
    # Create Executor
    # ==========================================

    executor = ToolExecutor(
        tool_registry=registry
    )

    # ==========================================
    # Tool Request
    # ==========================================
    # -------- Calculator Example --------

    # request = ToolRequest(
    #     tool_name="calculator",
    #     arguments={
    #         "expression": "(12 + 8) * 5"
    #     }
    # )
    # -------- Knowledge Base Example --------
    request = ToolRequest(
        tool_name="knowledge_base",
        arguments={
            "question": "What is lung cancer?"
        }
    )


    # ==========================================
    # Execute Tool
    # ==========================================

    result = executor.execute(request)

    # ==========================================
    # Display Results
    # ==========================================

    print("=" * 80)
    print("TOOL EXECUTION")
    print("=" * 80)

    print(f"Tool Name : {request.tool_name}")
    print(f"Arguments : {request.arguments}")
    print(f"Result    : {result}")

    print("\nOutput")
    print("-" * 80)
    print(result.output)

    print("\nMetadata")
    print("-" * 80)
    print(result.metadata)

    print("=" * 80)
    
if __name__ == "__main__":
    main()