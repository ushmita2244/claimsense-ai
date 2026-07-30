from models.conversation_history import ConversationHistory
from services.memory.memory_repository import MemoryRepository
from models.memory_models import (
    MemoryRecord,
    RetrieveMemoryRequest,
    RetrievedMemory,
)
from services.memory.memory_extractor import MemoryExtractor
from services.memory.memory_retrieval_policy import MemoryRetrievalPolicy
from models.memory_category import MemoryCategory
from services.memory.memory_selector import MemorySelector

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
        self.memory_extractor = MemoryExtractor()

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

        result = self.memory_extractor.extract(
            question=question,
            answer=answer,
        )
        
        print("\n========== MEMORY EXTRACTION ==========")
        print(f"Question      : {question}")
        print(f"Should Store : {result.should_store}")
        print(f"Memory       : {result.memory}")
        print("=======================================\n")
        
        if not result.should_store:
            print("Memory skipped.")
            return
        
        # For now, create the record here
        record = MemoryRecord(
            memory=result.memory,
            category=result.category,
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
        Retrieve only the semantic memories relevant to the current query.
        """

        # ==========================================
        # Classify the query
        # ==========================================

        category = MemoryRetrievalPolicy.classify(query)

        if category == MemoryCategory.NONE:
            return []

        # ==========================================
        # Retrieve candidate memories
        # ==========================================

        request = RetrieveMemoryRequest(
            query=query,
            session_id=session_id,
            top_k=top_k,
        )

        retrieved_memories = self.memory_repository.retrieve(
            request
        )

        # ==========================================
        # Select only relevant memories
        # ==========================================

        selected_memories = MemorySelector.select(
            category=category,
            memories=retrieved_memories,
        )

        return selected_memories