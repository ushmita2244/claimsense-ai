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

    print(f"Documents Retrieved : {response.evaluation.diagnostics.total_documents}")
    print(f"Top Distance        : {response.evaluation.diagnostics.top_distance:.4f}")
    print(f"Average Distance    : {response.evaluation.diagnostics.average_distance:.4f}")
    print(f"Retrieval Quality   : {response.evaluation.diagnostics.retrieval_quality}")

    print("\nSources")

    for source in response.evaluation.diagnostics.sources:
        print(f"• {source}")
    
    
    performance = response.evaluation.performance
    
    print("\n" + "=" * 80)
    print("PERFORMANCE METRICS")
    print("=" * 80)

    print(
        f"Embedding Time : {performance.embedding_time * 1000:.2f} ms"
    )

    print(
        f"Retrieval Time : {performance.retrieval_time * 1000:.2f} ms"
    )

    print(
        f"Prompt Time    : {performance.prompt_time * 1000:.2f} ms"
    )

    print(
        f"LLM Time       : {performance.llm_time:.2f} sec"
    )

    print(
        f"Total Time     : {performance.total_time:.2f} sec"
    )
    
    

    print("\n" + "=" * 80)
    print("SOURCES")
    print("=" * 80)
    
    for index, citation in enumerate(response.evaluation.citations, start=1):
    
        print(f"\n[{index}] {citation.source}")
    
        for chunk in citation.chunks:
        
            print(
                f"    Chunk {chunk.chunk_number:<3}"
                f" Distance : {chunk.distance:.4f}"
            )
    
    
    stats = response.evaluation.answer_statistics

    print("\n" + "=" * 80)
    print("ANSWER STATISTICS")
    print("=" * 80)
    
    print(f"Characters : {stats.character_count}")
    print(f"Words      : {stats.word_count}")
    print(f"Lines      : {stats.line_count}")
    

    print("\n" + "=" * 80)
    print("ANSWER")
    print("=" * 80)
    print(response.answer)