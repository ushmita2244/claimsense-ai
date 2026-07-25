import pytest
from unittest.mock import MagicMock

from models.web_search_models import (
    SearchResult,
    WebSearchResponse,
)

from services.tools.medical_web_search_tool import (
    MedicalWebSearchTool,
)


class TestMedicalWebSearchTool:

    def test_execute_success(self):
        """
        Verify that the tool returns a formatted ToolResult.
        """

        mock_service = MagicMock()

        mock_service.search.return_value = WebSearchResponse(
            answer="FDA approved a new lung cancer treatment.",
            sources=[
                SearchResult(
                    title="FDA",
                    url="https://www.fda.gov",
                    content="FDA content",
                )
            ],
        )

        tool = MedicalWebSearchTool(
            web_search_service=mock_service
        )

        result = tool.execute(
            question="Latest FDA-approved treatment"
        )

        assert isinstance(result.output, str)

        assert "Medical Web Search Summary" in result.output

        assert "FDA approved a new lung cancer treatment." in result.output

        mock_service.search.assert_called_once()

    def test_execute_invalid_question_none(self):
        """
        Verify that None is rejected.
        """

        tool = MedicalWebSearchTool(
            web_search_service=MagicMock()
        )

        with pytest.raises(
            ValueError,
            match="non-empty string",
        ):
            tool.execute(question=None)

    def test_execute_invalid_question_empty(self):
        """
        Verify that an empty string is rejected.
        """

        tool = MedicalWebSearchTool(
            web_search_service=MagicMock()
        )

        with pytest.raises(
            ValueError,
            match="non-empty string",
        ):
            tool.execute(question="")

    def test_execute_invalid_question_whitespace(self):
        """
        Verify that whitespace-only strings are rejected.
        """

        tool = MedicalWebSearchTool(
            web_search_service=MagicMock()
        )

        with pytest.raises(
            ValueError,
            match="non-empty string",
        ):
            tool.execute(question="   ")

    def test_execute_service_failure(self):
        """
        Verify that service exceptions are propagated.
        """

        mock_service = MagicMock()

        mock_service.search.side_effect = RuntimeError(
            "Medical web search failed."
        )

        tool = MedicalWebSearchTool(
            web_search_service=mock_service
        )

        with pytest.raises(
            RuntimeError,
            match="Medical web search failed.",
        ):
            tool.execute(question="Cancer")