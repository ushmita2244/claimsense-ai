import pytest

from models.web_search_models import (
    SearchResult,
    WebSearchResponse,
)
from services.web_search.web_search_response_formatter import (
    WebSearchResponseFormatter,
)


class TestWebSearchResponseFormatter:

    def test_format_with_single_source(self):

        response = WebSearchResponse(
            answer="Lung cancer treatment includes surgery.",
            sources=[
                SearchResult(
                    title="FDA",
                    url="https://www.fda.gov",
                    content="FDA content",
                )
            ],
        )

        formatted = WebSearchResponseFormatter.format(response)

        assert "Medical Web Search Summary" in formatted
        assert "Lung cancer treatment includes surgery." in formatted
        assert "Sources" in formatted
        assert "1. FDA" in formatted
        assert "https://www.fda.gov" in formatted

    def test_format_with_multiple_sources(self):

        response = WebSearchResponse(
            answer="Treatment options are available.",
            sources=[
                SearchResult(
                    title="FDA",
                    url="https://www.fda.gov",
                    content="content1",
                ),
                SearchResult(
                    title="WHO",
                    url="https://www.who.int",
                    content="content2",
                ),
            ],
        )

        formatted = WebSearchResponseFormatter.format(response)

        assert "1. FDA" in formatted
        assert "2. WHO" in formatted
        assert "https://www.fda.gov" in formatted
        assert "https://www.who.int" in formatted

    def test_format_without_sources(self):

        response = WebSearchResponse(
            answer="No sources available.",
            sources=[],
        )

        formatted = WebSearchResponseFormatter.format(response)

        assert "Medical Web Search Summary" in formatted
        assert "No sources available." in formatted

        assert "Sources" not in formatted
        assert "URL:" not in formatted

    def test_source_order_is_preserved(self):

        response = WebSearchResponse(
            answer="Summary",
            sources=[
                SearchResult(
                    title="First",
                    url="https://one.com",
                    content="",
                ),
                SearchResult(
                    title="Second",
                    url="https://two.com",
                    content="",
                ),
                SearchResult(
                    title="Third",
                    url="https://three.com",
                    content="",
                ),
            ],
        )

        formatted = WebSearchResponseFormatter.format(response)

        first = formatted.index("1. First")
        second = formatted.index("2. Second")
        third = formatted.index("3. Third")

        assert first < second < third