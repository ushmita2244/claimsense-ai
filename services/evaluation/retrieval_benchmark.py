from models.benchmark_report import BenchmarkReport
from models.retrieval_test_case import RetrievalTestCase

from services.retrieval.base_retriever import BaseRetriever
from services.evaluation.retrieval_evaluator import RetrievalEvaluator
from services.embeddings.embedding_service import EmbeddingService


class RetrievalBenchmark:
    """
    Executes retrieval benchmark against any retriever and dataset.
    """

    def __init__(
        self,
        retriever: BaseRetriever,
        dataset: list[RetrievalTestCase]
    ):

        self.retriever = retriever
        self.dataset = dataset
        self.evaluator = RetrievalEvaluator()

    def run(
        self,
        top_k: int = 3
    ) -> BenchmarkReport:

        results = []

        successful_retrievals = 0

        precision_sum = 0.0
        recall_sum = 0.0
        reciprocal_rank_sum = 0.0

        for test_case in self.dataset:

            # ==========================================
            # Retrieve Documents
            # ==========================================

            retrieval_response = self.retriever.retrieve(
                query=test_case.question,
                top_k=top_k
            )

            documents = retrieval_response.documents

            # ==========================================
            # Evaluate Retrieval
            # ==========================================

            result = self.evaluator.evaluate(
                test_case=test_case,
                retrieved_documents=documents,
                top_k=top_k
            )

            results.append(result)

            if result.chunk_match:
                successful_retrievals += 1

            precision_sum += result.precision_at_k
            recall_sum += result.recall_at_k
            reciprocal_rank_sum += result.reciprocal_rank

        total_queries = len(self.dataset)

        return BenchmarkReport(

            total_queries=total_queries,

            successful_retrievals=successful_retrievals,

            success_rate=(
                successful_retrievals / total_queries
                if total_queries else 0
            ),

            average_precision=(
                precision_sum / total_queries
                if total_queries else 0
            ),

            average_recall=(
                recall_sum / total_queries
                if total_queries else 0
            ),

            mean_reciprocal_rank=(
                reciprocal_rank_sum / total_queries
                if total_queries else 0
            ),

            results=results
        )