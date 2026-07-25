from typing import Literal

from pydantic import BaseModel


class ToolParameter(BaseModel):
    """
    Represents a single input parameter for a tool.
    """

    name: str
    description: str
    type: Literal[
        "string",
        "integer",
        "number",
        "boolean",
        "array",
        "object"
    ]
    required: bool = True