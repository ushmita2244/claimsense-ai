from models.conversation_history import ConversationHistory


class ConversationWindow:
    """
    Returns the most recent messages
    from a conversation.
    """

    def __init__(
        self,
        max_messages: int = 6
    ):

        self.max_messages = max_messages

    def build(
        self,
        history: ConversationHistory
    ) -> ConversationHistory:
        """
        Return only the most recent messages.
        """

        return ConversationHistory(

            messages=history.messages[-self.max_messages:]

        )