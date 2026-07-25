

from api.models.reranked_document import RerankedDocument


class RelevanceFilter:
    """
    Filters reranked documents using a minimum
    relevance score while ensuring enough
    documents remain for the LLM.
    """

    def filter(
        self,
        documents: list[RerankedDocument],
        score_threshold: float,
        minimum_documents: int = 2
    ) -> list[RerankedDocument]:

        # ==========================================
        # Empty Input
        # ==========================================

        if not documents:
            return []
        
        
        # Ensure at least one document is preserved
        
        minimum_documents = max(1, minimum_documents)


        # ==========================================
        # Filter by Threshold
        # ==========================================

        filtered_documents = [

            document

            for document in documents

            if document.rerank_score >= score_threshold

        ]

        # ==========================================
        # Fallback
        # ==========================================

        if len(filtered_documents) >= minimum_documents:

            return filtered_documents

        # ==========================================
        # Ensure Minimum Context
        # ==========================================

        return documents[:minimum_documents]