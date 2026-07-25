from services.retrieval.hybrid_retriever import HybridRetriever
from services.reranker.cross_encoder_reranker import CrossEncoderReranker


def main():

    query = "What can cause cancer?"

    # Step 1 : Hybrid Retrieval
    retriever = HybridRetriever()

    retrieval_response = retriever.retrieve(
        query=query,
        top_k=5
    )

    # Step 2 : Cross Encoder Reranking
    reranker = CrossEncoderReranker()

    reranked_documents = reranker.rerank(
        query=query,
        documents=retrieval_response.documents,
        top_k=5
    )

    print("=" * 80)
    print("CROSS ENCODER RERANKED RESULTS")
    print("=" * 80)

    for index, reranked_document in enumerate(reranked_documents, start=1):

        document = reranked_document.document

        print(f"\nRank : {index}")
        print(f"Cross Encoder Score : {reranked_document.rerank_score:.4f}")
        print(f"Source : {document.source}")
        print(f"Chunk : {document.chunk_number}")

        print("\nContent:")
        print(document.text[:250])

        print("-" * 80)


if __name__ == "__main__":
    main()