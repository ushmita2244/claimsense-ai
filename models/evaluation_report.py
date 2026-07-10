from dataclasses import dataclass

from models.performance_metrics import PerformanceMetrics
from models.retrieval_diagnostics import RetrievalDiagnostics
from models.source_attribution import SourceAttribution
from models.answer_statistics import AnswerStatistics


@dataclass
class EvaluationReport:
    """
    Complete evaluation of one RAG interaction.
    """

    diagnostics: RetrievalDiagnostics

    performance: PerformanceMetrics

    citations: list[SourceAttribution]
    
    answer_statistics: AnswerStatistics