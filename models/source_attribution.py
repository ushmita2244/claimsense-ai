from dataclasses import dataclass

from models.chunk_reference import ChunkReference


@dataclass
class SourceAttribution:
    """
    Represents one source document and all retrieved
    chunks belonging to it.
    """

    source: str

    chunks: list[ChunkReference]
    
    @property
    def best_distance(self) -> float:
        return self.chunks[0].distance