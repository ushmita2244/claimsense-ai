from services.evaluation.retrieval_benchmark import RetrievalBenchmark
from models.retrieval_test_case import RetrievalTestCase
from tests.helpers import make_document


class DummyRetriever:

    def retrieve(self, query_embedding, top_k=3):

        return [
            make_document(
                chunk_number=5
            )
        ]


class DummyEmbeddingService:

    def generate_embedding(self, text):

        return [0.1, 0.2, 0.3]


def test_benchmark_runs():

    dataset = [

        RetrievalTestCase(
            question="Question",
            expected_source="sample.pdf",
            expected_chunks=[5]
        )

    ]

    benchmark = RetrievalBenchmark(
        retriever=DummyRetriever(),
        dataset=dataset
    )

    benchmark.embedding_service = DummyEmbeddingService()

    report = benchmark.run()

    assert report.total_queries == 1
    assert report.successful_retrievals == 1
    assert report.success_rate == 1.0
    
def test_failed_benchmark():

    dataset = [

        RetrievalTestCase(
            question="Question",
            expected_source="sample.pdf",
            expected_chunks=[99]
        )

    ]

    benchmark = RetrievalBenchmark(
        retriever=DummyRetriever(),
        dataset=dataset
    )

    benchmark.embedding_service = DummyEmbeddingService()

    report = benchmark.run()

    assert report.successful_retrievals == 0
    assert report.success_rate == 0