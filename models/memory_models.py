from pydantic import BaseModel, Field
from models.memory_category import MemoryCategory

class MemoryRecord(BaseModel):
    """
    Represents a durable semantic memory stored for a user session.
    """

    memory: str
    
    category: MemoryCategory

    session_id: str


class RetrievedMemory(BaseModel):
    """
    Memory retrieved from the vector store.
    """

    content: str

    score: float
    
    category: MemoryCategory


class RetrieveMemoryRequest(BaseModel):
    """
    Request to retrieve memories.
    """

    query: str

    session_id: str

    top_k: int = Field(default=3, ge=1)