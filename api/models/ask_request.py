from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    """
    Request body for the /ask endpoint.
    """

    question: str = Field(
        ...,
        description="User's healthcare question."
    )

    session_id: str = Field(
        ...,
        description="Conversation session ID."
    )