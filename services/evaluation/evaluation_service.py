from models.evaluation_report import EvaluationReport
from models.performance_metrics import PerformanceMetrics
from models.retrieval_diagnostics import RetrievalDiagnostics
from models.source_attribution import SourceAttribution
from models.answer_statistics import AnswerStatistics


class EvaluationService:
    """
    Creates a complete evaluation report
    for a RAG response.
    """

    def build(
        self,
        diagnostics: RetrievalDiagnostics,
        performance: PerformanceMetrics,
        citations: list[SourceAttribution],
        answer_statistics : AnswerStatistics
    ) -> EvaluationReport:

        return EvaluationReport(
            diagnostics=diagnostics,
            performance=performance,
            citations=citations,
            answer_statistics=answer_statistics
        )