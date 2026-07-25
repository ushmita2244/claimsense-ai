from pydantic import BaseModel, Field


class OutputGuardrailResult(BaseModel):
    """
    Result returned by the Output Guardrail.
    """

    is_valid: bool

    response: str

    violations: list[str] = Field(default_factory=list)