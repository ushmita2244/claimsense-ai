import pytest

from models.memory_category import MemoryCategory
from models.memory_models import RetrievedMemory
from services.memory.memory_selector import MemorySelector


@pytest.fixture
def sample_memories():
    return [
        RetrievedMemory(
            content="User is a Data Engineer.",
            score=0.10,
        ),
        RetrievedMemory(
            content="Building ClaimSense-AI.",
            score=0.20,
        ),
        RetrievedMemory(
            content="Preparing for AI interviews.",
            score=0.30,
        ),
        RetrievedMemory(
            content="User prefers Python.",
            score=0.40,
        ),
        RetrievedMemory(
            content="User prefers clean architecture.",
            score=0.50,
        ),
    ]


def test_returns_empty_when_no_memories():
    result = MemorySelector.select(
        category=MemoryCategory.IDENTITY,
        memories=[],
    )

    assert result == []


def test_select_identity_memories(sample_memories):
    result = MemorySelector.select(
        category=MemoryCategory.IDENTITY,
        memories=sample_memories,
    )

    assert len(result) == 1
    assert result[0].content == "User is a Data Engineer."


def test_select_project_memories(sample_memories):
    result = MemorySelector.select(
        category=MemoryCategory.PROJECT,
        memories=sample_memories,
    )

    assert len(result) == 1
    assert result[0].content == "Building ClaimSense-AI."


def test_select_goal_memories(sample_memories):
    result = MemorySelector.select(
        category=MemoryCategory.GOAL,
        memories=sample_memories,
    )

    assert len(result) == 1
    assert result[0].content == "Preparing for AI interviews."


def test_select_preference_memories(sample_memories):
    result = MemorySelector.select(
        category=MemoryCategory.PREFERENCE,
        memories=sample_memories,
    )

    assert len(result) == 2

    contents = [memory.content for memory in result]

    assert "User prefers Python." in contents
    assert "User prefers clean architecture." in contents


def test_history_returns_all_memories(sample_memories):
    result = MemorySelector.select(
        category=MemoryCategory.HISTORY,
        memories=sample_memories,
    )

    assert result == sample_memories


def test_unknown_category_returns_all_memories(sample_memories):
    result = MemorySelector.select(
        category=None,
        memories=sample_memories,
    )

    assert result == sample_memories