from services.rag.rag_service import RAGService


def print_response(response):

    print("\n" + "=" * 100)

    print("QUESTION")

    print("-" * 100)

    print(response.question)

    print("\nANSWER")

    print("-" * 100)

    print(response.answer)


def main():

    rag = RAGService()

    session_id = "demo_session"

    print("=" * 100)
    print("CONVERSATIONAL RAG DEMO")
    print("=" * 100)

    while True:

        question = input("\nQuestion (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        response = rag.ask(
            question=question,
            session_id=session_id
        )

        print_response(response)


if __name__ == "__main__":
    main()
    