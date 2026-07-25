from pydantic import BaseModel, Field


class MemoryRecord(BaseModel):
    """
    Represents a semantic memory stored for a user session.
    """

    question: str

    answer: str

    session_id: str


class RetrievedMemory(BaseModel):
    """
    Memory retrieved from the vector store.
    """

    content: str

    score: float


class RetrieveMemoryRequest(BaseModel):
    """
    Request to retrieve memories.
    """

    query: str

    session_id: str

    top_k: int = Field(default=3, ge=1)