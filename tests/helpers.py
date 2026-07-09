from models.retrieved_document import RetrievedDocument

def make_document(
    text="Sample",
    source="sample.pdf",
    chunk_number=1,
    distance=0.1,
):
    return RetrievedDocument(
        text=text,
        source=source,
        chunk_number=chunk_number,
        distance=distance,
    )