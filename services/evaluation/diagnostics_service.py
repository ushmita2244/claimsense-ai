from models.retrieval_diagnostics import RetrievalDiagnostics
from models.retrieved_document import RetrievedDocument
from core.config.settings import settings


class DiagnosticsService:
    """
    Computes diagnostics for retrieved documents.
    """

    def analyze(
        self,
        documents: list[RetrievedDocument]
    ) -> RetrievalDiagnostics:

        total_documents = len(documents)

        distances = [
            doc.distance
            for doc in documents
        ]

        top_distance = min(distances)

        average_distance = (
            sum(distances) / len(distances)
        )

        sources = sorted(
            {
                doc.source
                for doc in documents
            }
        )

        if top_distance < settings.EXCELLENT_DISTANCE_THRESHOLD:
            quality = "Excellent"

        elif top_distance < settings.GOOD_DISTANCE_THRESHOLD:
            quality = "Good"

        elif top_distance < settings.AVERAGE_DISTANCE_THRESHOLD:
            quality = "Average"

        else:
            quality = "Poor"

        return RetrievalDiagnostics(
            total_documents=total_documents,
            top_distance=top_distance,
            average_distance=average_distance,
            sources=sources,
            retrieval_quality=quality
        )