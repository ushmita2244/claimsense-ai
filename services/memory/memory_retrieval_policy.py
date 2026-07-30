import re

from models.memory_category import MemoryCategory


class MemoryRetrievalPolicy:
    """
    Determines which semantic memory category should be
    retrieved for the current user query.
    """

    @classmethod
    def classify(
        cls,
        question: str,
    ) -> MemoryCategory:

        text = question.lower().strip()

        if cls._is_identity_query(text):
            return MemoryCategory.IDENTITY

        if cls._is_preference_query(text):
            return MemoryCategory.PREFERENCE

        if cls._is_project_query(text):
            return MemoryCategory.PROJECT

        if cls._is_goal_query(text):
            return MemoryCategory.GOAL

        if cls._is_workflow_query(text):
            return MemoryCategory.WORKFLOW

        if cls._is_history_query(text):
            return MemoryCategory.HISTORY

        return MemoryCategory.NONE

    @staticmethod
    def _matches_patterns(
        text: str,
        patterns: list[str],
    ) -> bool:
        """
        Returns True if any regex pattern matches the text.
        """

        return any(
            re.search(pattern, text)
            for pattern in patterns
        )

    @classmethod
    def _is_identity_query(
        cls,
        text: str,
    ) -> bool:

        patterns = [
            r"\bwho am i\b",
            r"\bwhat do you know about me\b",
            r"\bwhat do you remember about me\b",
            r"\bmy role\b",
            r"\bwhere do i work\b",
            r"\bwho do i work for\b",
            r"\bwhat company do i work for\b",
            r"\bwhat company am i working at\b",
        ]

        return cls._matches_patterns(text, patterns)

    @classmethod
    def _is_project_query(
        cls,
        text: str,
    ) -> bool:

        patterns = [
            r"\bmy project\b",
            r"\bwhat project am i\b",
            r"\bwhat am i building\b",
            r"\bwhat am i working on\b",
            r"\bwhat application am i developing\b",
            r"\bremind me what i'm building\b",
            r"\bdo you remember my project\b",
            r"\bwhat project do you remember\b",
        ]

        return cls._matches_patterns(text, patterns)

    @classmethod
    def _is_goal_query(
        cls,
        text: str,
    ) -> bool:

        patterns = [
            r"\bmy goal\b",
            r"\bwhat is my goal\b",
            r"\bmy career goal\b",
            r"\bwhat am i preparing for\b",
            r"\bwhat am i learning\b",
            r"\bwhat am i trying to become\b",
            r"\bdo you remember my goal\b",
        ]

        return cls._matches_patterns(text, patterns)

    @classmethod
    def _is_preference_query(
        cls,
        text: str,
    ) -> bool:

        patterns = [
            r"\bmy preferences\b",
            r"\bwhat are my preferences\b",
            r"\bwhat do i prefer\b",
            r"\bwhat is my preferred\b",
            r"\bdo you remember my preferences\b",
        ]

        return cls._matches_patterns(text, patterns)

    @classmethod
    def _is_workflow_query(
        cls,
        text: str,
    ) -> bool:

        patterns = [
            r"\bmy workflow\b",
            r"\bmy approach\b",
            r"\bmy process\b",
            r"\bmy coding style\b",
            r"\bhow do i usually\b",
            r"\bhow do i prefer to\b",
        ]

        return cls._matches_patterns(text, patterns)

    @classmethod
    def _is_history_query(
        cls,
        text: str,
    ) -> bool:

        patterns = [
            r"\bwhat did i tell you\b",
            r"\bdo you remember\b",
            r"\bremember when\b",
            r"\bwhat do you remember\b",
            r"\bwhat did we discuss\b",
            r"\bwhat did we talk about\b",
            r"\bremind me\b",
            r"\bearlier\b",
            r"\bbefore\b",
        ]

        return cls._matches_patterns(text, patterns)