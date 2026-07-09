from dataclasses import dataclass

from models.retrieved_document import RetrievedDocument
from models.retrieval_diagnostics import RetrievalDiagnostics
from models.performance_metrics import PerformanceMetrics


@dataclass
class RAGResponse:

    question: str

    retrieved_documents: list[RetrievedDocument]

    diagnostics: RetrievalDiagnostics
    
    performance: PerformanceMetrics

    answer: str
    