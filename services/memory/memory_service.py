from models.conversation_history import ConversationHistory
from services.memory.memory_repository import MemoryRepository
from models.memory_models import (
    MemoryRecord,
    RetrieveMemoryRequest,
    RetrievedMemory,
)

class MemoryService:
    """
    Stores conversations for active sessions.
    """

    def __init__(
        self, 
        memory_repository: MemoryRepository | None = None,
        ):

        self._conversation_sessions: dict[str, ConversationHistory] = {}
        
        self.memory_repository = (
            memory_repository
            if memory_repository is not None
            else MemoryRepository()
        )

    def get_history(
        self,
        session_id: str
    ) -> ConversationHistory:
        """
        Return the conversation history for a session.
        Creates one if it does not exist.
        """

        if session_id not in self._conversation_sessions:

            self._conversation_sessions[session_id] = ConversationHistory()

        return self._conversation_sessions[session_id]

    def clear(
        self,
        session_id: str
    ) -> None:
        """
        Clear a conversation.
        """

        self._conversation_sessions.pop(
            session_id,
            None
        )

    def clear_all(self) -> None:
        """
        Remove all conversations.
        """

        self._conversation_sessions.clear()
        
        
    def store_memory(
        self,
        question: str,
        answer: str,
        session_id: str,
    ) -> None:
        """
        Store a conversation in semantic memory.
        """

        record = MemoryRecord(
            question=question,
            answer=answer,
            session_id=session_id,
        )

        self.memory_repository.store(record)
        
        
    def retrieve_memories(
        self,
        query: str,
        session_id: str,
        top_k: int = 3,
    ) -> list[RetrievedMemory]:
        """
        Retrieve the most relevant semantic memories for the current session.
        """

        request = RetrieveMemoryRequest(
            query=query,
            session_id=session_id,
            top_k=top_k,
        )

        return self.memory_repository.retrieve(request)