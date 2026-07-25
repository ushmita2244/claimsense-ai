from services.tools.base_tool import BaseTool
from models.tool_definition import ToolDefinition

class ToolRegistry:

    def __init__(self):

        self._tools: dict[str, BaseTool] = {}

    def register_tool(
        self,
        tool: BaseTool
    ):
        if tool.definition.name in self._tools:
            raise ValueError(
                f"Tool '{tool.definition.name}' is already registered."
            )
        
        self._tools[
            tool.definition.name
        ] = tool

    def get_tool(
        self,
        tool_name: str
    ) -> BaseTool | None:

        return self._tools.get(tool_name)

    def has_tool(
        self,
        tool_name: str
    ) -> bool:

        return tool_name in self._tools

    def list_tools(
        self,
    ) -> list[ToolDefinition]:

        return [
            tool.definition
            for tool in self._tools.values()
        ]