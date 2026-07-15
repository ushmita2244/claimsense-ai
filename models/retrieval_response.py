from pydantic import BaseModel

from models.retrieved_document import RetrievedDocument


class RetrievalResponse(BaseModel):
    """
    Result returned by a retriever.
    """

    documents: list[RetrievedDocument]

    embedding_time: float

    retrieval_time: float