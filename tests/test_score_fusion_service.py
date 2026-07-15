from services.retrieval.score_fusion_service import ScoreFusionService
from tests.helpers import make_document


def test_common_document_gets_higher_rank():
    """
    A document returned by both retrievers should rank first.
    """

    fusion = ScoreFusionService()

    vector_documents = [
        make_document(source="WHO.pdf", chunk_number=1),
        make_document(source="WHO.pdf", chunk_number=2),
        make_document(source="WHO.pdf", chunk_number=3),
    ]

    bm25_documents = [
        make_document(source="WHO.pdf", chunk_number=2),
        make_document(source="WHO.pdf", chunk_number=4),
        make_document(source="WHO.pdf", chunk_number=5),
    ]

    results = fusion.fuse(
        vector_documents=vector_documents,
        bm25_documents=bm25_documents,
        top_k=3
    )

    assert results[0].chunk_number == 2


def test_top_k_results_returned():
    """
    Fusion should return only top_k documents.
    """

    fusion = ScoreFusionService()

    vector_documents = [
        make_document(chunk_number=1),
        make_document(chunk_number=2),
        make_document(chunk_number=3),
    ]

    bm25_documents = [
        make_document(chunk_number=4),
        make_document(chunk_number=5),
        make_document(chunk_number=6),
    ]

    results = fusion.fuse(
        vector_documents=vector_documents,
        bm25_documents=bm25_documents,
        top_k=2
    )

    assert len(results) == 2


def test_unique_documents_are_preserved():
    """
    Documents appearing in only one retriever should still appear.
    """

    fusion = ScoreFusionService()

    vector_documents = [
        make_document(chunk_number=1),
    ]

    bm25_documents = [
        make_document(chunk_number=2),
    ]

    results = fusion.fuse(
        vector_documents=vector_documents,
        bm25_documents=bm25_documents,
        top_k=2
    )

    chunks = sorted(
        document.chunk_number
        for document in results
    )

    assert chunks == [1, 2]


def test_duplicate_documents_removed():
    """
    Duplicate documents should appear only once.
    """

    fusion = ScoreFusionService()

    vector_documents = [
        make_document(chunk_number=5),
    ]

    bm25_documents = [
        make_document(chunk_number=5),
    ]

    results = fusion.fuse(
        vector_documents=vector_documents,
        bm25_documents=bm25_documents,
        top_k=3
    )

    assert len(results) == 1


def test_empty_inputs():
    """
    Empty retrieval results should return an empty list.
    """

    fusion = ScoreFusionService()

    results = fusion.fuse(
        vector_documents=[],
        bm25_documents=[],
        top_k=3
    )

    assert results == []