from unittest.mock import Mock

from models.memory_models import (
    MemoryRecord,
    RetrieveMemoryRequest,
)

from services.memory.memory_repository import (
    MemoryRepository,
)

def test_store_memory():

    mock_embedding = Mock()

    mock_embedding.generate_embedding.return_value = [0.1, 0.2, 0.3]

    mock_chroma = Mock()

    repository = MemoryRepository(
        chroma_service=mock_chroma,
        embedding_service=mock_embedding,
    )

    record = MemoryRecord(
        question="I have diabetes",
        answer="Follow a healthy diet.",
        session_id="session-123",
    )

    repository.store(record)

    mock_embedding.generate_embedding.assert_called_once()

    mock_chroma.add_document.assert_called_once()

    args = mock_chroma.add_document.call_args.kwargs

    assert "Question:" in args["text"]

    assert "Answer:" in args["text"]

    assert args["metadata"] == {
        "session_id": "session-123"
    }
    

def test_retrieve_memory():

    mock_embedding = Mock()

    mock_embedding.generate_embedding.return_value = [0.1, 0.2]

    mock_chroma = Mock()

    mock_chroma.search.return_value = {
        "documents": [
            [
                "Question: Diabetes\nAnswer: Healthy diet"
            ]
        ],
        "distances": [
            [
                0.14
            ]
        ],
    }

    repository = MemoryRepository(
        chroma_service=mock_chroma,
        embedding_service=mock_embedding,
    )

    request = RetrieveMemoryRequest(
        query="diet",
        session_id="session-123",
    )

    memories = repository.retrieve(request)

    assert len(memories) == 1

    assert memories[0].content.startswith("Question:")

    assert memories[0].score == 0.14
    
    
def test_retrieve_empty():

    mock_embedding = Mock()

    mock_embedding.generate_embedding.return_value = [0.1]

    mock_chroma = Mock()

    mock_chroma.search.return_value = {
        "documents": [[]],
        "distances": [[]],
    }

    repository = MemoryRepository(
        chroma_service=mock_chroma,
        embedding_service=mock_embedding,
    )

    request = RetrieveMemoryRequest(
        query="diet",
        session_id="session-123",
    )

    memories = repository.retrieve(request)

    assert memories == []
    
    
def test_session_filter():

    mock_embedding = Mock()

    mock_embedding.generate_embedding.return_value = [0.2]

    mock_chroma = Mock()

    mock_chroma.search.return_value = {
        "documents": [[]],
        "distances": [[]],
    }

    repository = MemoryRepository(
        chroma_service=mock_chroma,
        embedding_service=mock_embedding,
    )

    request = RetrieveMemoryRequest(
        query="diet",
        session_id="abc123",
    )

    repository.retrieve(request)

    mock_chroma.search.assert_called_once_with(
        query_embedding=[0.2],
        top_k=3,
        where={
            "session_id": "abc123"
        },
    )