import pytest

from models.memory_category import MemoryCategory
from services.memory.memory_retrieval_policy import MemoryRetrievalPolicy


class TestMemoryRetrievalPolicy:

    @pytest.mark.parametrize(
        "question, expected_category",
        [
            # ---------- Identity ----------
            (
                "Who am I?",
                MemoryCategory.IDENTITY,
            ),
            (
                "What do you know about me?",
                MemoryCategory.IDENTITY,
            ),
            (
                "Where do I work?",
                MemoryCategory.IDENTITY,
            ),

            # ---------- Preference ----------
            (
                "What do I prefer?",
                MemoryCategory.PREFERENCE,
            ),
            (
                "What are my preferences?",
                MemoryCategory.PREFERENCE,
            ),

            # ---------- Project ----------
            (
                "What am I building?",
                MemoryCategory.PROJECT,
            ),
            (
                "Do you remember my project?",
                MemoryCategory.PROJECT,
            ),

            # ---------- Goal ----------
            (
                "What is my goal?",
                MemoryCategory.GOAL,
            ),
            (
                "What am I preparing for?",
                MemoryCategory.GOAL,
            ),

            # ---------- Workflow ----------
            (
                "What is my workflow?",
                MemoryCategory.WORKFLOW,
            ),
            (
                "How do I usually write code?",
                MemoryCategory.WORKFLOW,
            ),

            # ---------- History ----------
            (
                "What did we discuss yesterday?",
                MemoryCategory.HISTORY,
            ),
            (
                "Remind me what we talked about.",
                MemoryCategory.HISTORY,
            ),
        ],
    )
    def test_classify(
        self,
        question,
        expected_category,
    ):

        category = MemoryRetrievalPolicy.classify(question)

        assert category == expected_category

    @pytest.mark.parametrize(
        "question",
        [
            "Explain Python decorators.",
            "What is machine learning?",
            "How does SQL JOIN work?",
            "Tell me a joke.",
            "What is LangChain?",
        ],
    )
    def test_returns_none_for_unrelated_queries(
        self,
        question,
    ):

        category = MemoryRetrievalPolicy.classify(question)

        assert category == MemoryCategory.NONE