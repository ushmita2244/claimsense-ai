from api.models.reranked_document import RerankedDocument
from models.retrieved_document import RetrievedDocument
from services.reranker.relevance_filter import RelevanceFilter


class TestRelevanceFilter:

    def setup_method(self):

        self.filter = RelevanceFilter()

    def create_document(
        self,
        text: str,
        score: float
    ) -> RerankedDocument:

        return RerankedDocument(

            document=RetrievedDocument(
                text=text,
                source="test.pdf",
                chunk_number=1,
                distance=0.1
            ),

            rerank_score=score
        )

    # ==========================================
    # Empty Input
    # ==========================================

    def test_returns_empty_list_when_no_documents(self):

        result = self.filter.filter(
            documents=[],
            score_threshold=0.0,
            minimum_documents=2
        )

        assert result == []

    # ==========================================
    # All Documents Above Threshold
    # ==========================================

    def test_returns_all_documents_when_all_above_threshold(self):

        documents = [

            self.create_document("A", 9.0),
            self.create_document("B", 7.0),
            self.create_document("C", 5.0)

        ]

        result = self.filter.filter(
            documents=documents,
            score_threshold=2.0,
            minimum_documents=2
        )

        assert len(result) == 3

        assert result[0].document.text == "A"
        assert result[1].document.text == "B"
        assert result[2].document.text == "C"

    # ==========================================
    # Some Documents Filtered
    # ==========================================

    def test_filters_documents_below_threshold(self):

        documents = [

            self.create_document("A", 9.0),
            self.create_document("B", 5.0),
            self.create_document("C", 1.0),
            self.create_document("D", -2.0)

        ]

        result = self.filter.filter(
            documents=documents,
            score_threshold=2.0,
            minimum_documents=2
        )

        assert len(result) == 2

        assert result[0].document.text == "A"
        assert result[1].document.text == "B"

    # ==========================================
    # Fallback
    # ==========================================

    def test_returns_minimum_documents_when_threshold_filters_everything(self):

        documents = [

            self.create_document("A", 0.5),
            self.create_document("B", 0.2),
            self.create_document("C", -1.5)

        ]

        result = self.filter.filter(
            documents=documents,
            score_threshold=2.0,
            minimum_documents=2
        )

        assert len(result) == 2

        assert result[0].document.text == "A"
        assert result[1].document.text == "B"

    # ==========================================
    # Fallback With Fewer Documents
    # ==========================================

    def test_returns_available_documents_when_less_than_minimum(self):

        documents = [

            self.create_document("A", 0.5)

        ]

        result = self.filter.filter(
            documents=documents,
            score_threshold=2.0,
            minimum_documents=2
        )

        assert len(result) == 1

        assert result[0].document.text == "A"