from unittest.mock import Mock

from models.memory_category import MemoryCategory
from models.memory_models import (
    MemoryRecord,
    RetrieveMemoryRequest,
)

from services.memory.memory_repository import MemoryRepository


class TestMemoryRepository:

    def test_store_memory(self):

        mock_embedding = Mock()
        mock_embedding.generate_embedding.return_value = [0.1, 0.2, 0.3]

        mock_chroma = Mock()

        repository = MemoryRepository(
            chroma_service=mock_chroma,
            embedding_service=mock_embedding,
        )

        record = MemoryRecord(
            memory="User prefers Python.",
            category=MemoryCategory.PREFERENCE,
            session_id="session-123",
        )

        repository.store(record)

        mock_embedding.generate_embedding.assert_called_once_with(
            "User prefers Python."
        )

        mock_chroma.add_document.assert_called_once()

        args = mock_chroma.add_document.call_args.kwargs

        assert args["text"] == "User prefers Python."

        assert args["embedding"] == [0.1, 0.2, 0.3]

        assert args["metadata"] == {
            "session_id": "session-123",
            "category": "preference",
        }

    def test_retrieve_memory(self):

        mock_embedding = Mock()
        mock_embedding.generate_embedding.return_value = [0.5, 0.6]

        mock_chroma = Mock()

        mock_chroma.search.return_value = {
            "documents": [
                [
                    "User prefers Python."
                ]
            ],
            "distances": [
                [
                    0.18
                ]
            ],
            "metadatas": [
                [
                    {
                        "category": "preference"
                    }
                ]
            ],
        }

        repository = MemoryRepository(
            chroma_service=mock_chroma,
            embedding_service=mock_embedding,
        )

        request = RetrieveMemoryRequest(
            query="What do I prefer?",
            session_id="session-123",
        )

        memories = repository.retrieve(request)

        assert len(memories) == 1

        assert memories[0].content == "User prefers Python."

        assert memories[0].score == 0.18

        assert memories[0].category == MemoryCategory.PREFERENCE

    def test_retrieve_empty(self):

        mock_embedding = Mock()
        mock_embedding.generate_embedding.return_value = [0.1]

        mock_chroma = Mock()

        mock_chroma.search.return_value = {
            "documents": [[]],
            "distances": [[]],
            "metadatas": [[]],
        }

        repository = MemoryRepository(
            chroma_service=mock_chroma,
            embedding_service=mock_embedding,
        )

        request = RetrieveMemoryRequest(
            query="Anything",
            session_id="session-123",
        )

        memories = repository.retrieve(request)

        assert memories == []

    def test_similarity_threshold(self):

        mock_embedding = Mock()
        mock_embedding.generate_embedding.return_value = [0.1]

        mock_chroma = Mock()

        mock_chroma.search.return_value = {
            "documents": [
                [
                    "Relevant memory",
                    "Irrelevant memory",
                ]
            ],
            "distances": [
                [
                    0.20,
                    0.95,
                ]
            ],
            "metadatas": [
                [
                    {
                        "category": "goal",
                    },
                    {
                        "category": "goal",
                    },
                ]
            ],
        }

        repository = MemoryRepository(
            chroma_service=mock_chroma,
            embedding_service=mock_embedding,
        )

        request = RetrieveMemoryRequest(
            query="goal",
            session_id="session-123",
        )

        memories = repository.retrieve(request)

        assert len(memories) == 1

        assert memories[0].content == "Relevant memory"

    def test_session_filter(self):

        mock_embedding = Mock()
        mock_embedding.generate_embedding.return_value = [0.2]

        mock_chroma = Mock()

        mock_chroma.search.return_value = {
            "documents": [[]],
            "distances": [[]],
            "metadatas": [[]],
        }

        repository = MemoryRepository(
            chroma_service=mock_chroma,
            embedding_service=mock_embedding,
        )

        request = RetrieveMemoryRequest(
            query="goal",
            session_id="abc123",
        )

        repository.retrieve(request)

        mock_chroma.search.assert_called_once_with(
            query_embedding=[0.2],
            top_k=3,
            where={
                "session_id": "abc123",
            },
        )