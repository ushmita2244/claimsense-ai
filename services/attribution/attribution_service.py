from models.chunk_reference import ChunkReference
from models.retrieved_document import RetrievedDocument
from models.source_attribution import SourceAttribution
from collections import defaultdict


class AttributionService:
    """
    Groups retrieved chunks by source document.
    """

    def build(
        self,
        documents: list[RetrievedDocument]
    ) -> list[SourceAttribution]:

        grouped_sources = defaultdict(list)

        for document in documents:

            grouped_sources[document.source].append(

                ChunkReference(

                    chunk_number=document.chunk_number,

                    distance=document.distance

                )

            )

        citations = []

        for source, chunks in grouped_sources.items():

            chunks.sort(
                key=lambda chunk: chunk.distance
            )

            citations.append(

                SourceAttribution(

                    source=source,

                    chunks=chunks

                )

            )

        citations.sort(
        key=lambda citation: citation.best_distance
        )

        return citations