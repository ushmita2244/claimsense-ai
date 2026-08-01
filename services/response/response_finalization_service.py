from services.memory.conversation_manager import ConversationManager
from services.memory.memory_service import MemoryService


class ResponseFinalizationService:

    def __init__(
        self,
        conversation_manager: ConversationManager,
        memory_service: MemoryService,
    ):
        self.conversation_manager = conversation_manager
        self.memory_service = memory_service

    def finalize(
        self,
        session_id: str,
        question: str,
        response: str,
    ) -> None:
        
        # Store user message
        self.conversation_manager.add_user_message(
            session_id=session_id,
            content=question,
        )

        self.conversation_manager.add_assistant_message(
            session_id=session_id,
            content=response,
        )

        self.memory_service.store_memory(
            question=question,
            answer=response,
            session_id=session_id,
        )

        