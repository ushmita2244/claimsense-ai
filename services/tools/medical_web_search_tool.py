from models.tool_definition import (
    ToolDefinition,
    ToolParameter,
)

from models.tool_result import ToolResult

from models.web_search_models import (
    WebSearchRequest,
)

from services.tools.base_tool import BaseTool

from services.web_search.web_search_service import (
    WebSearchService,
)

from services.web_search.web_search_response_formatter import (
    WebSearchResponseFormatter,
)


class MedicalWebSearchTool(BaseTool):
    """
    Tool responsible for searching up-to-date medical
    information from trusted web sources.
    """

    def __init__(
        self,
        web_search_service: WebSearchService | None = None,
            ):

        self.web_search_service = (
            web_search_service
            if web_search_service is not None
            else WebSearchService()
        )

    @property
    def definition(self) -> ToolDefinition:

        return ToolDefinition(
            name="medical_web_search",
            description=(
                "Searches trusted medical web sources for "
                "recent healthcare information."
            ),
            parameters=[
                ToolParameter(
                    name="question",
                    type="string",
                    required=True,
                    description="Medical question to search."
                )
            ]
        )

    def execute(
        self,
        **kwargs,
    ) -> ToolResult:
        """
        Execute the Medical Web Search Tool.
        """

        # ==========================================
        # Validate Input
        # ==========================================

        question = kwargs.get("question")

        if not isinstance(question, str) or not question.strip():
            raise ValueError(
                "The 'question' argument must be a non-empty string."
            )

        # ==========================================
        # Search Web
        # ==========================================

        response = self.web_search_service.search(
            WebSearchRequest(
                question=question
            )
        )

        # ==========================================
        # Format Response
        # ==========================================

        formatted_response = (
            WebSearchResponseFormatter.format(
                response
            )
        )

        # ==========================================
        # Return Tool Result
        # ==========================================

        return ToolResult(
            output=formatted_response,
        )