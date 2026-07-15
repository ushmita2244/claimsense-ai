from litellm import query

from services.embeddings.embedding_service import EmbeddingService
from services.retrieval.retriever import Retriever
from services.retrieval.bm25_service import BM25Service
from services.retrieval.hybrid_retriever import HybridRetriever


def print_results(title, documents):

    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    for rank, document in enumerate(documents, start=1):

        print(f"\nRank {rank}")

        print(f"Source : {document.source}")

        print(f"Chunk  : {document.chunk_number}")

        print(f"Distance : {document.distance:.4f}")

        print("-" * 80)

        print(document.text[:350])


def main():

    vector_retriever = Retriever()

    bm25 = BM25Service()

    hybrid = HybridRetriever()

    while True:

        print("\n")

        query = input("Question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        # ======================================
        # Vector Search
        # ======================================

        vector_response = vector_retriever.retrieve(
        query=query,
        top_k=3
        )

        vector_documents = vector_response.documents

        # ======================================
        # BM25 Search
        # ======================================

        bm25_documents = bm25.search(
            query=query,
            top_k=3
        )

        # ======================================
        # Hybrid Search
        # ======================================

        hybrid_response = hybrid.retrieve(
        query=query,
        top_k=3
        )

        hybrid_documents = hybrid_response.documents

        # ======================================
        # Display
        # ======================================

        print_results(
            "VECTOR SEARCH",
            vector_documents
        )

        print_results(
            "BM25 SEARCH",
            bm25_documents
        )

        print_results(
            "HYBRID SEARCH",
            hybrid_documents
        )


if __name__ == "__main__":
    main()