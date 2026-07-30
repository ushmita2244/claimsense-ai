from dataclasses import dataclass
from models.retrieval_quality import RetrievalQuality


@dataclass
class RetrievalDiagnostics:
    """
    Stores information about the retrieval process.
    """

    total_documents: int

    top_distance: float

    average_distance: float

    sources: list[str]

    retrieval_quality: RetrievalQuality