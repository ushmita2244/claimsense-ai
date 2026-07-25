from pydantic import BaseModel, Field


class ToolRequest(BaseModel):
    """
    Represents a request to execute a tool.
    """

    tool_name: str = Field(
        ...,
        description="Name of the tool to execute."
    )

    arguments: dict = Field(
        default_factory=dict,
        description="Arguments passed to the tool."
    )