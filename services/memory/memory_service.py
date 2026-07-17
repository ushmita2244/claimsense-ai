from models.conversation_history import ConversationHistory


class MemoryService:
    """
    Stores conversations for active sessions.
    """

    def __init__(self):

        self._sessions: dict[str, ConversationHistory] = {}

    def get_history(
        self,
        session_id: str
    ) -> ConversationHistory:
        """
        Return the conversation history for a session.
        Creates one if it does not exist.
        """

        if session_id not in self._sessions:

            self._sessions[session_id] = ConversationHistory()

        return self._sessions[session_id]

    def clear(
        self,
        session_id: str
    ) -> None:
        """
        Clear a conversation.
        """

        self._sessions.pop(
            session_id,
            None
        )

    def clear_all(self) -> None:
        """
        Remove all conversations.
        """

        self._sessions.clear()