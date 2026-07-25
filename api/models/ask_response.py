from pydantic import BaseModel


class AskResponse(BaseModel):
    """
    Response returned by the /ask endpoint.
    """

    question: str

    answer: str