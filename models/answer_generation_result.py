from dataclasses import dataclass
from typing import Any

from models.retrieved_document import RetrievedDocument
from models.answer_source import AnswerSource


@dataclass
class AnswerGenerationResult:
    """
    Represents the output of any answer generation strategy.
    """

    answer: str

    answer_source: AnswerSource

    citations: list[Any]

    retrieved_documents: list[RetrievedDocument]

    prompt_time: float

    llm_time: float