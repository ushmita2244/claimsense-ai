from collections import defaultdict

from models.retrieved_document import RetrievedDocument


class ScoreFusionService:
    """
    Combines Vector Search and BM25 rankings using
    Weighted Reciprocal Rank Fusion.
    """

    def fuse(
        self,
        vector_documents: list[RetrievedDocument],
        bm25_documents: list[RetrievedDocument],
        top_k: int = 3,
        rrf_constant: int = 60,
        vector_weight: float = 0.8,
        bm25_weight: float = 0.2
    ) -> list[RetrievedDocument]:

        fused_scores = defaultdict(float)

        document_lookup = {}

        # ==========================================
        # Vector Search Contribution
        # ==========================================

        for rank, document in enumerate(vector_documents, start=1):

            key = (
                document.source,
                document.chunk_number
            )

            score = vector_weight * (
                1 / (rrf_constant + rank + 1)
            )

            fused_scores[key] = fused_scores.get(key, 0) + score

            document_lookup[key] = document

        # ==========================================
        # BM25 Contribution
        # ==========================================

        for rank, document in enumerate(bm25_documents, start=1):

            key = (
                document.source,
                document.chunk_number
            )

            score = bm25_weight * (
                1 / (rrf_constant + rank + 1)
            )

            fused_scores[key] = fused_scores.get(key, 0) + score

            if key not in document_lookup:
                document_lookup[key] = document

        # ==========================================
        # Final Ranking
        # ==========================================

        ranked_documents = sorted(

            fused_scores.items(),

            key=lambda item: item[1],

            reverse=True

        )

        return [

            document_lookup[key]

            for key, _ in ranked_documents[:top_k]

        ]