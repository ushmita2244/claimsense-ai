from abc import ABC, abstractmethod

from models.answer_generation_result import AnswerGenerationResult
from models.memory_models import RetrievedMemory
from models.retrieved_document import RetrievedDocument


class AnswerGenerator(ABC):
    """
    Base class for all answer generation strategies.
    """

    @abstractmethod
    def generate(
        self,
        question: str,
        retrieved_documents: list[RetrievedDocument],
        conversation_history: str,
        semantic_memories: list[RetrievedMemory] | None,
    ) -> AnswerGenerationResult:
        pass