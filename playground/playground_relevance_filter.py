from services.retrieval.hybrid_retriever import HybridRetriever
from services.reranker.cross_encoder_reranker import CrossEncoderReranker
from services.reranker.relevance_filter import RelevanceFilter


def main():

    query = "What can cause cancer?"

    # ==========================================
    # Hybrid Retrieval
    # ==========================================

    retriever = HybridRetriever()

    retrieval_response = retriever.retrieve(
        query=query,
        top_k=5
    )

    # ==========================================
    # Cross Encoder Reranking
    # ==========================================

    reranker = CrossEncoderReranker()

    reranked_documents = reranker.rerank(
        query=query,
        documents=retrieval_response.documents,
        top_k=5
    )

    # ==========================================
    # Relevance Filtering
    # ==========================================

    relevance_filter = RelevanceFilter()

    filtered_documents = relevance_filter.filter(
        documents=reranked_documents,
        score_threshold=0.0,
        minimum_documents=2
    )

    # ==========================================
    # Results
    # ==========================================

    print("=" * 80)
    print("FILTERED DOCUMENTS")
    print("=" * 80)

    print(f"Retrieved Documents : {len(retrieval_response.documents)}")
    print(f"Reranked Documents  : {len(reranked_documents)}")
    print(f"Filtered Documents  : {len(filtered_documents)}")

    print("=" * 80)

    for index, reranked_document in enumerate(filtered_documents, start=1):

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