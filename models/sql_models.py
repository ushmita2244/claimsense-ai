from typing import Any

from pydantic import BaseModel, Field

class SQLGenerationRequest(BaseModel):
    question: str


class SQLGenerationResponse(BaseModel):
    sql_query: str

class SQLRequest(BaseModel):
    """
    Request object for SQL execution.
    """

    query: str

class SQLResponse(BaseModel):
    """
    Response returned by SQLService after executing a query.
    """

    query: str
    columns: list[str] = Field(default_factory=list)
    rows: list[list[Any]] = Field(default_factory=list)
    row_count: int = 0
    execution_time_ms: float = 0.0

