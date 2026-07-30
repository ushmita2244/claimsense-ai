from models.retrieval_diagnostics import RetrievalDiagnostics
from models.retrieved_document import RetrievedDocument
from models.retrieval_quality import RetrievalQuality
from core.config.settings import settings


class DiagnosticsService:
    """
    Computes diagnostics for retrieved documents.
    """

    def analyze(
        self,
        documents: list[RetrievedDocument]
    ) -> RetrievalDiagnostics:
        
        if not documents:

            return RetrievalDiagnostics(
                total_documents=0,
                top_distance=float("inf"),
                average_distance=float("inf"),
                sources=[],
                retrieval_quality=RetrievalQuality.POOR,
            )

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
            quality = RetrievalQuality.EXCELLENT

        elif top_distance < settings.GOOD_DISTANCE_THRESHOLD:
            quality = RetrievalQuality.GOOD

        elif top_distance < settings.AVERAGE_DISTANCE_THRESHOLD:
            quality = RetrievalQuality.AVERAGE

        else:
            quality = RetrievalQuality.POOR

        return RetrievalDiagnostics(
            total_documents=total_documents,
            top_distance=top_distance,
            average_distance=average_distance,
            sources=sources,
            retrieval_quality=quality
        )