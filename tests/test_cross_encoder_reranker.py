from unittest.mock import MagicMock, patch

from api.models.reranked_document import RerankedDocument
from models.retrieved_document import RetrievedDocument
from services.reranker.cross_encoder_reranker import CrossEncoderReranker


class TestCrossEncoderReranker:

    @patch("services.reranker.cross_encoder_reranker.CrossEncoder")
    def test_returns_empty_list_when_no_documents(
        self,
        mock_cross_encoder
    ):

        reranker = CrossEncoderReranker()

        result = reranker.rerank(
            query="What causes cancer?",
            documents=[]
        )

        assert result == []

    @patch("services.reranker.cross_encoder_reranker.CrossEncoder")
    def test_returns_reranked_documents(
        self,
        mock_cross_encoder
    ):

        model = MagicMock()

        model.predict.return_value = [
            0.4,
            0.9,
            0.2
        ]

        mock_cross_encoder.return_value = model

        reranker = CrossEncoderReranker()

        documents = [

            RetrievedDocument(
                text="Document A",
                source="A.pdf",
                chunk_number=1,
                distance=0.12
            ),

            RetrievedDocument(
                text="Document B",
                source="B.pdf",
                chunk_number=2,
                distance=0.18
            ),

            RetrievedDocument(
                text="Document C",
                source="C.pdf",
                chunk_number=3,
                distance=0.20
            )

        ]

        result = reranker.rerank(
            query="What causes cancer?",
            documents=documents
        )

        assert len(result) == 3

        assert isinstance(
            result[0],
            RerankedDocument
        )

        assert result[0].document.text == "Document B"
        assert result[1].document.text == "Document A"
        assert result[2].document.text == "Document C"

    @patch("services.reranker.cross_encoder_reranker.CrossEncoder")
    def test_top_k_limits_results(
        self,
        mock_cross_encoder
    ):

        model = MagicMock()

        model.predict.return_value = [
            0.2,
            0.7,
            0.5
        ]

        mock_cross_encoder.return_value = model

        reranker = CrossEncoderReranker()

        documents = [

            RetrievedDocument(
                text="A",
                source="a.pdf",
                chunk_number=1,
                distance=0.1
            ),

            RetrievedDocument(
                text="B",
                source="b.pdf",
                chunk_number=2,
                distance=0.2
            ),

            RetrievedDocument(
                text="C",
                source="c.pdf",
                chunk_number=3,
                distance=0.3
            )

        ]

        result = reranker.rerank(
            query="Cancer",
            documents=documents,
            top_k=2
        )

        assert len(result) == 2

        assert result[0].document.text == "B"
        assert result[1].document.text == "C"

    @patch("services.reranker.cross_encoder_reranker.CrossEncoder")
    def test_predict_called_once(
        self,
        mock_cross_encoder
    ):

        model = MagicMock()

        model.predict.return_value = [
            0.5
        ]

        mock_cross_encoder.return_value = model

        reranker = CrossEncoderReranker()

        documents = [

            RetrievedDocument(
                text="Document",
                source="doc.pdf",
                chunk_number=1,
                distance=0.1
            )

        ]

        reranker.rerank(
            query="Cancer",
            documents=documents
        )

        model.predict.assert_called_once()