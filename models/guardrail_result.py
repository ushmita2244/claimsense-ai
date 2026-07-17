from pydantic import BaseModel


class GuardrailResult(BaseModel):
    """
    Result returned by the guardrail service.
    """

    allowed: bool

    reason: str