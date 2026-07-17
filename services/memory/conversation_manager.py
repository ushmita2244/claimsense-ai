from models.conversation_message import ConversationMessage
from models.conversation_history import ConversationHistory

from services.memory.memory_service import MemoryService


class ConversationManager:
    """
    Manages conversations for active sessions.
    """

    def __init__(self):

        self.memory = MemoryService()

    def add_user_message(
        self,
        session_id: str,
        content: str
    ) -> None:
        """
        Add a user message to the conversation.
        """

        history = self.memory.get_history(
            session_id
        )

        history.messages.append(

            ConversationMessage(
                role="user",
                content=content
            )

        )

    def add_assistant_message(
        self,
        session_id: str,
        content: str
    ) -> None:
        """
        Add an assistant response.
        """

        history = self.memory.get_history(
            session_id
        )

        history.messages.append(

            ConversationMessage(
                role="assistant",
                content=content
            )

        )

    def get_history(
        self,
        session_id: str
    ) -> ConversationHistory:
        """
        Return a conversation.
        """

        return self.memory.get_history(
            session_id
        )

    def clear(
        self,
        session_id: str
    ) -> None:
        """
        Delete a conversation.
        """

        self.memory.clear(
            session_id
        )