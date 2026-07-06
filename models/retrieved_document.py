from dataclasses import dataclass


@dataclass
class RetrievedDocument:
    """
    Represents one document retrieved
    from the vector database.
    """

    text: str

    source: str

    chunk_number: int

    distance: float