from models.tool_request import ToolRequest

from services.tools.tool_registry import ToolRegistry
from models.tool_result import ToolResult


class ToolExecutor:

    def __init__(
        self,
        registry: ToolRegistry
    ):

        self.registry = registry

    def execute(
        self,
        request: ToolRequest,
        **execution_context,
    )-> ToolResult:

        tool = self.registry.get_tool(
            request.tool_name
        )

        if tool is None:

            raise ValueError(
                f"Unknown tool: {request.tool_name}"
            )

        arguments = request.arguments or {}
        
        arguments.update(execution_context)
        
        return tool.execute(
            **arguments
        )

    def list_tools(self):

        return self.registry.list_tools()