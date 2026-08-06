from typing import Any

from pydantic import BaseModel, Field

from models.knowledge_source import KnowledgeSource


class ToolResult(BaseModel):
    """
    Standard result returned by every tool.
    """

    output: str

    metadata: dict[str, Any] = Field(default_factory=dict)
    
    knowledge_sources: list[KnowledgeSource] = Field(
        default_factory=list
    )