from dataclasses import dataclass

from models.evaluation_report import EvaluationReport
from models.retrieved_document import RetrievedDocument
from typing import Optional


@dataclass
class RAGResponse:
    """
    Final response returned by the RAG pipeline.
    """

    question: str

    retrieved_documents: list[RetrievedDocument]

    evaluation: Optional[EvaluationReport] = None

    answer: str = ""