from dataclasses import dataclass
from models.memory_category import MemoryCategory

@dataclass
class MemoryExtractionResult:
    """
    Result of semantic memory extraction.
    """

    should_store: bool
    memory: str | None = None
    category: MemoryCategory | None = None