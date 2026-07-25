from typing import Any

from pydantic import BaseModel, Field


class ToolResult(BaseModel):
    """
    Standard result returned by every tool.
    """

    output: str

    metadata: dict[str, Any] = Field(default_factory=dict)