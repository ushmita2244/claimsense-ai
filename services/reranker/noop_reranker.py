from api.models.reranked_document import RerankedDocument
from models.retrieved_document import RetrievedDocument


class NoOpReranker:
    """
    Lightweight reranker.

    Keeps the retrieval order without loading
    any ML model.
    """

    def rerank(
        self,
        query: str,
        documents: list[RetrievedDocument],
        top_k: int | None = None,
    ) -> list[RerankedDocument]:

        results = [
            RerankedDocument(
                document=document,
                rerank_score=1.0,
            )
            for document in documents
        ]

        if top_k:
            return results[:top_k]

        return results