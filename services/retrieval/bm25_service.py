from oauthlib.uri_validate import query
from rank_bm25 import BM25Okapi

from models.retrieved_document import RetrievedDocument
from services.vector_db.chroma_service import ChromaService


class BM25Service:
    """
    BM25 keyword search service.
    """

    def __init__(self):

        self.vector_db = ChromaService()

        self.documents = []

        self.tokenized_documents = []

        self.bm25 = None

        self._build_index()

    def _build_index(self):
        """
        Load all documents from ChromaDB and build the BM25 index.
        """

        results = self.vector_db.collection.get(
            include=[
                "documents",
                "metadatas"
            ]
        )

        for text, metadata in zip(
            results["documents"],
            results["metadatas"]
        ):

            document = RetrievedDocument(
                text=text,
                source=metadata["source"],
                chunk_number=metadata["chunk_number"],
                distance=0.0
            )

            self.documents.append(document)

            self.tokenized_documents.append(
                text.lower().split()
            )

        self.bm25 = BM25Okapi(
            self.tokenized_documents
        )
        
    
    def search(
    self,
    query: str,
    top_k: int = 3
    ) -> list[RetrievedDocument]:
        """
        Search the BM25 index using a keyword query.
        """

    # ==========================================
    # Tokenize Query
    # ==========================================

        query_tokens = query.lower().split()

    # ==========================================
    # Calculate BM25 Scores
    # ==========================================

        scores = self.bm25.get_scores(
        query_tokens
        )

    # ==========================================
    # Rank Documents
    # ==========================================

        ranked_results = sorted(
        zip(scores, self.documents),
        key=lambda item: item[0],
        reverse=True
        )

    # ==========================================
    # Return Top K
    # ==========================================

        return [
            document
            for _, document in ranked_results[:top_k]
        ]