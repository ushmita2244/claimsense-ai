import pytest

from services.memory.memory_extractor import MemoryExtractor
from models.memory_category import MemoryCategory


class TestMemoryExtractor:

    def setup_method(self):
        self.extractor = MemoryExtractor()

    @pytest.mark.parametrize(
        "question, expected_memory, expected_category",
        [
            # ---------- Identity ----------
            (
                "I am a Data Engineer",
                "User is a Data Engineer.",
                MemoryCategory.IDENTITY,
            ),
            (
                "I'm a Software Engineer",
                "User is a Software Engineer.",
                MemoryCategory.IDENTITY,
            ),
            (
                "My role is Backend Developer",
                "User is Backend Developer.",
                MemoryCategory.IDENTITY,
            ),
            (
                "I work as Data Scientist",
                "User is Data Scientist.",
                MemoryCategory.IDENTITY,
            ),

            # ---------- Preference ----------
            (
                "I prefer Python",
                "User prefers Python.",
                MemoryCategory.PREFERENCE,
            ),
            (
                "Always write clean code",
                "User always write clean code.",
                MemoryCategory.PREFERENCE,
            ),
            (
                "Never use tabs",
                "User never use tabs.",
                MemoryCategory.PREFERENCE,
            ),

            # ---------- Project ----------
            (
                "I am building ClaimSense AI",
                "User is building ClaimSense AI.",
                MemoryCategory.PROJECT,
            ),
            (
                "I'm working on an enterprise chatbot",
                "User is working on an enterprise chatbot.",
                MemoryCategory.PROJECT,
            ),
            (
                "I am developing an AI assistant",
                "User is developing an AI assistant.",
                MemoryCategory.PROJECT,
            ),
            (
                "I'm creating a RAG application",
                "User is creating a RAG application.",
                MemoryCategory.PROJECT,
            ),

            # ---------- Goal ----------
            (
                "I want to become an AI Engineer",
                "User wants to become an AI Engineer.",
                MemoryCategory.GOAL,
            ),
            (
                "I am preparing for interviews",
                "User is preparing for interviews.",
                MemoryCategory.GOAL,
            ),
            (
                "I'm preparing for GATE",
                "User is preparing for GATE.",
                MemoryCategory.GOAL,
            ),
            (
                "My goal is to switch to an AI Engineer role",
                "User's goal is to switch to an AI Engineer role.",
                MemoryCategory.GOAL,
            ),
        ],
    )
    def test_extract_memory(
        self,
        question,
        expected_memory,
        expected_category,
    ):

        result = self.extractor.extract(
            question=question,
            answer="Dummy answer",
        )

        assert result.should_store is True
        assert result.memory == expected_memory
        assert result.category == expected_category

    @pytest.mark.parametrize(
        "question",
        [
            "How is the weather today?",
            "What is Python?",
            "Tell me a joke.",
            "Explain SQL joins.",
            "Who is the Prime Minister of India?",
        ],
    )
    def test_no_memory_extracted(
        self,
        question,
    ):

        result = self.extractor.extract(
            question=question,
            answer="Dummy answer",
        )

        assert result.should_store is False
        assert result.memory is None
        assert result.category is None