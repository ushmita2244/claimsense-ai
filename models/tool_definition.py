from pydantic import BaseModel

from models.tool_parameter import ToolParameter


class ToolDefinition(BaseModel):
    """
    Metadata describing a tool that can be used by the planner.
    """

    name: str

    description: str

    parameters: list[ToolParameter]