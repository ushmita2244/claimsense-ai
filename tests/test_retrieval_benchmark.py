from services.evaluation.retrieval_benchmark import RetrievalBenchmark

from models.retrieval_response import RetrievalResponse
from models.retrieval_test_case import RetrievalTestCase

from tests.helpers import make_document


class DummyRetriever:

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ) -> RetrievalResponse:

        return RetrievalResponse(

            documents=[
                make_document(
                    chunk_number=5
                )
            ],

            embedding_time=0.01,

            retrieval_time=0.02

        )


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

    report = benchmark.run()

    assert report.successful_retrievals == 0
    assert report.success_rate == 0.0