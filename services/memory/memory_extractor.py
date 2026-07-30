import re

from models.memory_extraction_result import MemoryExtractionResult
from models.memory_category import MemoryCategory


class MemoryExtractor:
    """
    Extracts durable semantic memories using deterministic rules.

    Only long-term useful information is stored.
    """

    def extract(
        self,
        question: str,
        answer: str,
    ) -> MemoryExtractionResult:

        _ = answer  # Reserved for future use

        text = question.strip()

        extractors = [
            self._extract_preference,
            self._extract_project,
            self._extract_goal,
            self._extract_identity,
        ]

        for extractor in extractors:

            result = extractor(text)

            if result:
                return result

        return MemoryExtractionResult(
            should_store=False,
            memory=None,
            category=None,
        )

    # ==================================================
    # Identity
    # ==================================================

    def _extract_identity(
        self,
        text: str,
    ) -> MemoryExtractionResult | None:

        patterns = [
            r"^i\s+am\s+((?:an?|the)\s+.+)$",
            r"^i'm\s+((?:an?|the)\s+.+)$",
            r"^my\s+role\s+is\s+(.+)$",
            r"^i\s+work\s+as\s+(.+)$",
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE,
            )

            if match:

                role = self._normalize_sentence(
                    match.group(1)
                )

                return self._build_result(
                    memory=f"User is {role}",
                    category=MemoryCategory.IDENTITY,
                )

        return None

    # ==================================================
    # Preference
    # ==================================================

    def _extract_preference(
        self,
        text: str,
    ) -> MemoryExtractionResult | None:

        patterns = [
            (
                r"^always\s+(.+)$",
                lambda value: f"User always {value}",
            ),
            (
                r"^never\s+(.+)$",
                lambda value: f"User never {value}",
            ),
            (
                r"^i\s+prefer\s+(.+)$",
                lambda value: f"User prefers {value}",
            ),
        ]

        for pattern, formatter in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE,
            )

            if match:

                preference = self._normalize_sentence(
                    match.group(1)
                )

                return self._build_result(
                    memory=formatter(preference),
                    category=MemoryCategory.PREFERENCE,
                )

        return None

    # ==================================================
    # Project
    # ==================================================

    def _extract_project(
        self,
        text: str,
    ) -> MemoryExtractionResult | None:

        patterns = [
            r"^i\s+am\s+(building\s+.+)$",
            r"^i'm\s+(building\s+.+)$",

            r"^i\s+am\s+(working\s+on\s+.+)$",
            r"^i'm\s+(working\s+on\s+.+)$",

            r"^i\s+am\s+(developing\s+.+)$",
            r"^i'm\s+(developing\s+.+)$",

            r"^i\s+am\s+(creating\s+.+)$",
            r"^i'm\s+(creating\s+.+)$",
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE,
            )

            if match:

                project = self._normalize_sentence(
                    match.group(1)
                )

                return self._build_result(
                    memory=f"User is {project}",
                    category=MemoryCategory.PROJECT,
                )

        return None

    # ==================================================
    # Goal
    # ==================================================

    def _extract_goal(
        self,
        text: str,
    ) -> MemoryExtractionResult | None:

        patterns = [
            (
                r"^i\s+want\s+to\s+(.+)$",
                lambda goal: f"User wants to {goal}",
            ),
            (
                r"^i\s+am\s+preparing\s+for\s+(.+)$",
                lambda goal: f"User is preparing for {goal}",
            ),
            (
                r"^i'm\s+preparing\s+for\s+(.+)$",
                lambda goal: f"User is preparing for {goal}",
            ),
            (
                r"^my\s+goal\s+is\s+(.+)$",
                lambda goal: f"User's goal is {goal}",
            ),
        ]

        for pattern, formatter in patterns:

            match = re.search(
                pattern,
                text,
                re.IGNORECASE,
            )

            if match:

                goal = self._normalize_sentence(
                    match.group(1)
                )

                return self._build_result(
                    memory=formatter(goal),
                    category=MemoryCategory.GOAL,
                )

        return None

    # ==================================================
    # Helpers
    # ==================================================

    @staticmethod
    def _normalize_sentence(
        text: str,
    ) -> str:

        return text.strip().rstrip(".")

    @staticmethod
    def _build_result(
        memory: str,
        category: MemoryCategory,
    ) -> MemoryExtractionResult:

        return MemoryExtractionResult(
            should_store=True,
            memory=f"{memory}.",
            category=category,
        )