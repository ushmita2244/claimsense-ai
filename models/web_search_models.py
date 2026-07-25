from pydantic import BaseModel, Field


class WebSearchRequest(BaseModel):
    """
    Request sent to the Medical Web Search service.
    """

    question: str = Field(
        min_length=1,
        description="User question to search on the web."
    )


class SearchResult(BaseModel):
    """
    Represents a single search result returned by Tavily.
    """

    title: str
    url: str
    content: str


class WebSearchResponse(BaseModel):
    """
    Structured response returned by the Medical Web Search service.
    """

    answer: str
    sources: list[SearchResult]