from dataclasses import dataclass


@dataclass
class PerformanceMetrics:
    """
    Stores latency information for each stage
    of the RAG pipeline.
    """

    embedding_time: float

    retrieval_time: float

    prompt_time: float

    llm_time: float

    total_time: float