from models.retrieval_response import RetrievalResponse
from services.retrieval.hybrid_retriever import HybridRetriever
from tests.helpers import make_document


class DummyRetriever:

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ) -> RetrievalResponse:

        return RetrievalResponse(
            documents=[
                make_document(chunk_number=1),
                make_document(chunk_number=2),
                make_document(chunk_number=3),
            ],
            embedding_time=0.10,
            retrieval_time=0.20
        )


class DummyBM25:

    def search(
        self,
        query: str,
        top_k: int = 3
    ):

        return [
            make_document(chunk_number=2),
            make_document(chunk_number=4),
            make_document(chunk_number=5),
        ]


def test_hybrid_returns_retrieval_response():

    hybrid = HybridRetriever()

    hybrid.vector_retriever = DummyRetriever()

    hybrid.bm25_service = DummyBM25()

    response = hybrid.retrieve(
        query="What causes cancer?"
    )

    assert isinstance(response, RetrievalResponse)


def test_hybrid_returns_documents():

    hybrid = HybridRetriever()

    hybrid.vector_retriever = DummyRetriever()

    hybrid.bm25_service = DummyBM25()

    response = hybrid.retrieve(
        query="What causes cancer?"
    )

    assert len(response.documents) == 3


def test_hybrid_respects_top_k():

    hybrid = HybridRetriever()

    hybrid.vector_retriever = DummyRetriever()

    hybrid.bm25_service = DummyBM25()

    response = hybrid.retrieve(
        query="What causes cancer?",
        top_k=2
    )

    assert len(response.documents) == 2


def test_hybrid_returns_timings():

    hybrid = HybridRetriever()

    hybrid.vector_retriever = DummyRetriever()

    hybrid.bm25_service = DummyBM25()

    response = hybrid.retrieve(
        query="What causes cancer?"
    )

    assert response.embedding_time == 0.10

    assert response.retrieval_time == 0.20