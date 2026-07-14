from abc import ABC, abstractmethod

from models.retrieved_document import RetrievedDocument


class BaseRetriever(ABC):
    """
    Interface for all retrieval strategies.
    """

    @abstractmethod
    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ) -> list[RetrievedDocument]:
        """
        Retrieve relevant documents.
        """
        pass