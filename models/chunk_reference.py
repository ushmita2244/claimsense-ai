from dataclasses import dataclass


@dataclass
class ChunkReference:
    """
    Represents one retrieved chunk belonging to a source document.
    """

    chunk_number: int

    distance: float