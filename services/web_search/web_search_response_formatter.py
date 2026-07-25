from models.web_search_models import WebSearchResponse


class WebSearchResponseFormatter:
    """
    Formats the web search response into a readable string that
    can be consumed by the final LLM prompt.
    """

    @staticmethod
    def format(
        response: WebSearchResponse
    ) -> str:
        """
        Format the web search response.

        Args:
            response: Structured web search response.

        Returns:
            Formatted string.
        """

        lines: list[str] = [
            "Medical Web Search Summary",
            "==========================",
            "",
            response.answer
        ]

        if response.sources:

            lines.extend([
                "",
                "Sources",
                "-------"
            ])

            for index, source in enumerate(response.sources, start=1):

                lines.extend([
                    f"{index}. {source.title}",
                    f"URL: {source.url}",
                    ""
                ])

        return "\n".join(lines).strip()