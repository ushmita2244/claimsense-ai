from datetime import datetime

from pydantic import BaseModel, Field


class ConversationMessage(BaseModel):
    """
    Represents a single message in a conversation.
    """

    role: str

    content: str

    timestamp: datetime = Field(
        default_factory=datetime.now
    )