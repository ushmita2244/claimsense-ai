from services.rag.rag_service import RAGService

rag = RAGService()

print("=" * 80)
print("Healthcare AI Copilot")
print("=" * 80)

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    response = rag.ask(question)

    print("\n" + "=" * 80)
    print("QUESTION")
    print("=" * 80)
    print(response.question)

    print("\n" + "=" * 80)
    print("RETRIEVED DOCUMENTS")
    print("=" * 80)

    for index, document in enumerate(response.retrieved_documents, start=1):

        print(f"\nDocument {index}")
        print("-" * 80)

        print(f"Source        : {document.source}")
        print(f"Chunk Number  : {document.chunk_number}")
        print(f"Distance      : {document.distance:.4f}")

        print("\nText:")
        print(document.text)

        print("-" * 80)
        
        
    print("\n" + "=" * 80)
    print("RETRIEVAL DIAGNOSTICS")
    print("=" * 80)

    print(f"Documents Retrieved : {response.diagnostics.total_documents}")
    print(f"Top Distance        : {response.diagnostics.top_distance:.4f}")
    print(f"Average Distance    : {response.diagnostics.average_distance:.4f}")
    print(f"Retrieval Quality   : {response.diagnostics.retrieval_quality}")

    print("\nSources")

    for source in response.diagnostics.sources:
        print(f"• {source}")
    

    print("\n" + "=" * 80)
    print("ANSWER")
    print("=" * 80)
    print(response.answer)