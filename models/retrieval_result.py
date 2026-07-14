from dataclasses import dataclass

from models.retrieved_document import RetrievedDocument
from models.retrieval_test_case import RetrievalTestCase


@dataclass
class RetrievalResult:
    """
    Stores the retrieval output for one benchmark query.
    """

    test_case: RetrievalTestCase

    retrieved_documents: list[RetrievedDocument]

    document_match: bool

    chunk_match: bool

    precision_at_k: float

    recall_at_k: float

    reciprocal_rank: float