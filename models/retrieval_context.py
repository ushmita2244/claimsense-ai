from dataclasses import dataclass
from typing import Optional

from models.guardrail_result import GuardrailResult
from models.retrieval_diagnostics import RetrievalDiagnostics
from models.retrieved_document import RetrievedDocument


@dataclass
class RetrievalContext:
    """
    Represents the complete retrieval phase of the RAG pipeline.
    """

    rewritten_question: Optional[str] = None

    retrieved_documents: list[RetrievedDocument] | None = None

    diagnostics: Optional[RetrievalDiagnostics] = None

    embedding_time: float = 0.0

    retrieval_time: float = 0.0