from tavily import TavilyClient

from core.config.settings import settings

from models.web_search_models import (
    SearchResult,
    WebSearchRequest,
    WebSearchResponse,
)
from services.llm.base_llm import BaseLLM
from services.llm.gemini_service import GeminiService
from services.web_search.web_search_prompt_builder import (
    WebSearchPromptBuilder,
)


class WebSearchService:
    """
    Service responsible for performing medical web searches
    and generating a summarized response.
    """

    MAX_RESULTS = 5

    def __init__(
        self,
        client: TavilyClient | None = None,
        llm: BaseLLM | None = None,
        ):

        self.client = (
            client
            if client is not None
            else TavilyClient(
                api_key=settings.TAVILY_API_KEY
            )
        )

        self.llm = llm or GeminiService()

    def search(
        self,
        request: WebSearchRequest,
    ) -> WebSearchResponse:
        """
        Search the web and summarize the results.

        Args:
            request: Medical web search request.

        Returns:
            Structured web search response.
        """

        # ==========================================
        # Search Web
        # ==========================================

        try:
            response = self.client.search(
                query=request.question,
                search_depth="advanced",
                max_results=self.MAX_RESULTS,
                include_answer=False,
                include_images=False,
            )

        except Exception as exc:
            raise RuntimeError(
                "Medical web search failed."
            ) from exc

        # ==========================================
        # Convert Search Results
        # ==========================================

        search_results = self._convert_results(response)

        # ==========================================
        # Build Search Context
        # ==========================================

        search_context = self._build_search_context(
            search_results
        )

        # ==========================================
        # Build Prompt
        # ==========================================

        prompt = WebSearchPromptBuilder.build(
            question=request.question,
            search_results=search_context,
        )

        # ==========================================
        # Generate Summary
        # ==========================================

        answer = self.llm.generate_response(
            prompt
        )

        # ==========================================
        # Return Response
        # ==========================================

        return WebSearchResponse(
            answer=answer,
            sources=search_results,
        )

    def _convert_results(
        self,
        response: dict,
    ) -> list[SearchResult]:
        """
        Convert Tavily response into SearchResult models.
        """

        search_results: list[SearchResult] = []

        for result in response.get("results", []):

            search_results.append(
                SearchResult(
                    title=result.get("title", ""),
                    url=result.get("url", ""),
                    content=result.get("content", ""),
                )
            )

        return search_results

    def _build_search_context(
        self,
        search_results: list[SearchResult],
    ) -> str:
        """
        Build the context that will be provided to the LLM.
        """

        sections: list[str] = []

        for result in search_results:

            sections.append(
                f"""
Title:
{result.title}

Content:
{result.content}
""".strip()
            )

        return "\n\n".join(sections)