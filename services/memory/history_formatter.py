from models.conversation_history import ConversationHistory


class HistoryFormatter:
    """
    Converts conversation history into prompt text.
    """

    @staticmethod
    def format(
        history: ConversationHistory
    ) -> str:

        if not history.messages:
            return ""

        lines = []

        for message in history.messages:

            lines.append(
                f"{message.role.capitalize()}:\n{message.content}"
            )

        return "\n\n".join(lines)