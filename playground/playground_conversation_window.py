from services.memory.conversation_manager import ConversationManager
from services.memory.conversation_window import ConversationWindow
from services.memory.history_formatter import HistoryFormatter


def main():

    manager = ConversationManager()

    window = ConversationWindow(
        max_messages=4
    )

    session = "demo"

    for i in range(1, 7):

        manager.add_user_message(
            session,
            f"Question {i}"
        )

        manager.add_assistant_message(
            session,
            f"Answer {i}"
        )

    history = manager.get_history(session)

    print("=" * 80)
    print("FULL HISTORY")
    print("=" * 80)

    print(
        HistoryFormatter.format(
            history
        )
    )

    print("\n")

    print("=" * 80)
    print("WINDOW")
    print("=" * 80)

    window_history = window.build(
        history
    )

    print(
        HistoryFormatter.format(
            window_history
        )
    )


if __name__ == "__main__":
    main()