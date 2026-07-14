from dataclasses import dataclass

from models.retrieval_result import RetrievalResult


@dataclass
class BenchmarkReport:
    """
    Final benchmark statistics.
    """

    total_queries: int

    successful_retrievals: int

    success_rate: float

    average_precision: float

    average_recall: float

    mean_reciprocal_rank: float

    results: list[RetrievalResult]