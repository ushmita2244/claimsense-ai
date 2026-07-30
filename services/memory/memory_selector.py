from models.memory_category import MemoryCategory
from models.memory_models import RetrievedMemory


class MemorySelector:
    """
    Selects only the semantic memories relevant to the
    requested memory category.
    """

    @classmethod
    def select(
        cls,
        category: MemoryCategory,
        memories: list[RetrievedMemory],
    ) -> list[RetrievedMemory]:
        """
        Select memories belonging to the requested category.
        """

        if not memories:
            return []

        # History queries should receive all retrieved memories.
        if category == MemoryCategory.HISTORY:
            return memories

        return [
            memory
            for memory in memories
            if memory.category == category
        ]