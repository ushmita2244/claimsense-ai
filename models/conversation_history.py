from pydantic import BaseModel, Field

from models.conversation_message import ConversationMessage


class ConversationHistory(BaseModel):
    """
    Represents an entire conversation.
    """

    messages: list[ConversationMessage] = Field(
        default_factory=list
    )