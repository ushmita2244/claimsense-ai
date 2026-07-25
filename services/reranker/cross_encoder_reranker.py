from sentence_transformers import CrossEncoder

from models.retrieved_document import RetrievedDocument
from api.models.reranked_document import RerankedDocument


class CrossEncoderReranker:
    """
    Uses a Cross-Encoder model to rerank retrieved documents.
    """

    def __init__(
        self,
        model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"
    ):
        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        documents: list[RetrievedDocument],
        top_k: int | None = None
    ) -> list[RerankedDocument]:

        if not documents:
            return []

        sentence_pairs = [
            (query, doc.text)
            for doc in documents
        ]

        scores = self.model.predict(sentence_pairs)

        reranked_documents = [
            RerankedDocument(
                document=doc,
                rerank_score=float(score)
            )
            for doc, score in zip(documents, scores)
        ]

        reranked_documents.sort(
            key=lambda document: document.rerank_score,
            reverse=True
        )

        if top_k:
            reranked_documents = reranked_documents[:top_k]

        return reranked_documents