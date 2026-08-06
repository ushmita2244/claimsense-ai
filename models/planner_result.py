from typing import Literal

from pydantic import BaseModel

from models.tool_request import ToolRequest


class PlannerResult(BaseModel):
    """
    Represents the planner's structured decision.
    """

    type: Literal[
        "tool",
        "answer"
    ]

    tool_request: ToolRequest | None = None

    response: str | None = None
    