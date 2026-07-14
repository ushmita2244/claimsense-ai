from services.evaluation.retrieval_evaluator import RetrievalEvaluator
from models.retrieval_test_case import RetrievalTestCase
from tests.helpers import make_document


def test_document_match():

    evaluator = RetrievalEvaluator()

    test_case = RetrievalTestCase(
        question="test",
        expected_source="sample.pdf",
        expected_chunks=[2]
    )

    documents = [
        make_document(
            source="sample.pdf",
            chunk_number=5
        )
    ]

    result = evaluator.evaluate(
        test_case=test_case,
        retrieved_documents=documents,
        top_k=3
    )

    assert result.document_match is True


def test_chunk_match():

    evaluator = RetrievalEvaluator()

    test_case = RetrievalTestCase(
        question="test",
        expected_source="sample.pdf",
        expected_chunks=[2]
    )

    documents = [
        make_document(
            source="sample.pdf",
            chunk_number=2
        )
    ]

    result = evaluator.evaluate(
        test_case=test_case,
        retrieved_documents=documents,
        top_k=3
    )

    assert result.chunk_match is True


def test_precision():

    evaluator = RetrievalEvaluator()

    test_case = RetrievalTestCase(
        question="test",
        expected_source="sample.pdf",
        expected_chunks=[1, 2]
    )

    documents = [
        make_document(source="sample.pdf", chunk_number=1),
        make_document(source="sample.pdf", chunk_number=2),
        make_document(source="sample.pdf", chunk_number=9),
    ]

    result = evaluator.evaluate(
        test_case=test_case,
        retrieved_documents=documents,
        top_k=3
    )

    assert result.precision_at_k == 2 / 3


def test_recall():

    evaluator = RetrievalEvaluator()

    test_case = RetrievalTestCase(
        question="test",
        expected_source="sample.pdf",
        expected_chunks=[1, 2, 3]
    )

    documents = [
        make_document(source="sample.pdf", chunk_number=1),
        make_document(source="sample.pdf", chunk_number=2),
    ]

    result = evaluator.evaluate(
        test_case=test_case,
        retrieved_documents=documents,
        top_k=3
    )

    assert result.recall_at_k == 2 / 3


def test_reciprocal_rank():

    evaluator = RetrievalEvaluator()

    test_case = RetrievalTestCase(
        question="test",
        expected_source="sample.pdf",
        expected_chunks=[8]
    )

    documents = [
        make_document(chunk_number=1),
        make_document(chunk_number=8),
        make_document(chunk_number=9),
    ]

    result = evaluator.evaluate(
        test_case=test_case,
        retrieved_documents=documents,
        top_k=3
    )

    assert result.reciprocal_rank == 0.5


def test_no_match():

    evaluator = RetrievalEvaluator()

    test_case = RetrievalTestCase(
        question="test",
        expected_source="sample.pdf",
        expected_chunks=[50]
    )

    documents = [
        make_document(chunk_number=1),
        make_document(chunk_number=2),
        make_document(chunk_number=3),
    ]

    result = evaluator.evaluate(
        test_case=test_case,
        retrieved_documents=documents,
        top_k=3
    )

    assert result.document_match is True
    assert result.chunk_match is False
    assert result.precision_at_k == 0
    assert result.recall_at_k == 0
    assert result.reciprocal_rank == 0