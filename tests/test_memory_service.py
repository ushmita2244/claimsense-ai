from unittest.mock import Mock, patch

from models.conversation_history import ConversationHistory
from models.memory_category import MemoryCategory
from models.memory_models import (
    RetrievedMemory,
)
from models.memory_extraction_result import MemoryExtractionResult

from services.memory.memory_service import MemoryService


class TestMemoryService:

    # ==================================================
    # Conversation history
    # ==================================================

    def test_get_history_creates_session(self):

        service = MemoryService()

        history = service.get_history("session-1")

        assert isinstance(history, ConversationHistory)

    def test_get_history_returns_same_instance(self):

        service = MemoryService()

        history1 = service.get_history("session-1")
        history2 = service.get_history("session-1")

        assert history1 is history2

    def test_clear_session(self):

        service = MemoryService()

        history1 = service.get_history("session-1")

        service.clear("session-1")

        history2 = service.get_history("session-1")

        assert history1 is not history2

    def test_clear_all_sessions(self):

        service = MemoryService()

        service.get_history("a")
        service.get_history("b")

        service.clear_all()

        assert service._conversation_sessions == {}

    # ==================================================
    # Store memory
    # ==================================================

    def test_store_memory(self):

        mock_repository = Mock()

        service = MemoryService(
            memory_repository=mock_repository,
        )

        service.memory_extractor = Mock()

        service.memory_extractor.extract.return_value = (
            MemoryExtractionResult(
                should_store=True,
                memory="User prefers Python.",
                category=MemoryCategory.PREFERENCE,
            )
        )

        service.store_memory(
            question="I prefer Python.",
            answer="Okay.",
            session_id="session-123",
        )

        service.memory_extractor.extract.assert_called_once_with(
            question="I prefer Python.",
            answer="Okay.",
        )

        mock_repository.store.assert_called_once()

        record = mock_repository.store.call_args.args[0]

        assert record.memory == "User prefers Python."
        assert record.category == MemoryCategory.PREFERENCE
        assert record.session_id == "session-123"

    def test_store_memory_skips_when_not_required(self):

        mock_repository = Mock()

        service = MemoryService(
            memory_repository=mock_repository,
        )

        service.memory_extractor = Mock()

        service.memory_extractor.extract.return_value = (
            MemoryExtractionResult(
                should_store=False,
                memory=None,
                category=None,
            )
        )

        service.store_memory(
            question="Hello",
            answer="Hi",
            session_id="session-123",
        )

        mock_repository.store.assert_not_called()

    # ==================================================
    # Retrieve memory
    # ==================================================

    @patch(
        "services.memory.memory_service.MemorySelector.select"
    )
    @patch(
        "services.memory.memory_service.MemoryRetrievalPolicy.classify"
    )
    def test_retrieve_memories(
        self,
        mock_classify,
        mock_select,
    ):

        mock_repository = Mock()

        service = MemoryService(
            memory_repository=mock_repository,
        )

        mock_classify.return_value = MemoryCategory.PREFERENCE

        retrieved = [
            RetrievedMemory(
                content="User prefers Python.",
                score=0.1,
                category=MemoryCategory.PREFERENCE,
            )
        ]

        selected = retrieved

        mock_repository.retrieve.return_value = retrieved

        mock_select.return_value = selected

        result = service.retrieve_memories(
            query="What do I prefer?",
            session_id="session-123",
        )

        assert result == selected

        mock_repository.retrieve.assert_called_once()

        mock_select.assert_called_once_with(
            category=MemoryCategory.PREFERENCE,
            memories=retrieved,
        )

    @patch(
        "services.memory.memory_service.MemoryRetrievalPolicy.classify"
    )
    def test_retrieve_returns_empty_for_none_category(
        self,
        mock_classify,
    ):

        mock_repository = Mock()

        service = MemoryService(
            memory_repository=mock_repository,
        )

        mock_classify.return_value = MemoryCategory.NONE

        result = service.retrieve_memories(
            query="Explain Python.",
            session_id="session-123",
        )

        assert result == []

        mock_repository.retrieve.assert_not_called()