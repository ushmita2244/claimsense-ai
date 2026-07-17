from services.memory.conversation_manager import ConversationManager
from services.memory.history_formatter import HistoryFormatter
from services.rewriting.query_rewriter import QueryRewriter


def main():

    manager = ConversationManager()

    rewriter = QueryRewriter()

    session = "demo"

    print("=" * 80)
    print("QUERY REWRITER PLAYGROUND")
    print("=" * 80)

    while True:

        question = input("\nQuestion (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        history = manager.get_history(session)

        formatted_history = HistoryFormatter.format(
            history
        )

        rewritten_question = rewriter.rewrite(
            question=question,
            conversation_history=formatted_history
        )

        print("\n" + "-" * 80)

        print("Original Question")
        print(question)

        print("\nRewritten Question")
        print(rewritten_question)

        manager.add_user_message(
            session_id=session,
            content=question
        )

        manager.add_assistant_message(
            session_id=session,
            content=f"(Rewritten) {rewritten_question}"
        )


if __name__ == "__main__":
    main()