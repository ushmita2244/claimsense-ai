from services.memory.conversation_manager import ConversationManager
from services.memory.history_formatter import HistoryFormatter


def main():

    manager = ConversationManager()

    session = "demo"

    manager.add_user_message(
        session,
        "What causes breast cancer?"
    )

    manager.add_assistant_message(
        session,
        "Breast cancer has several risk factors."
    )

    manager.add_user_message(
        session,
        "What are its symptoms?"
    )

    history = manager.get_history(
        session
    )

    formatted = HistoryFormatter.format(
        history
    )

    print(formatted)


if __name__ == "__main__":
    main()