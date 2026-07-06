from dataclasses import dataclass

from models.retrieved_document import RetrievedDocument
from models.retrieval_diagnostics import RetrievalDiagnostics


@dataclass
class RAGResponse:

    question: str

    retrieved_documents: list[RetrievedDocument]

    diagnostics: RetrievalDiagnostics

    answer: str
    