from dataclasses import dataclass

from models.retrieved_document import RetrievedDocument


@dataclass
class RerankedDocument:
    """
    Represents a retrieved document after reranking.
    """

    document: RetrievedDocument
    rerank_score: float