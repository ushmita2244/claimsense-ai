from services.vector_db.chroma_service import ChromaService

db = ChromaService()

results = db.collection.get(
    include=["documents", "metadatas"]
)

for text, metadata in zip(
    results["documents"],
    results["metadatas"]
):

    print("=" * 80)
    
    print(f"Source : {metadata['source']}")
    print(f"Chunk {metadata['chunk_number']}")

    print("=" * 80)

    preview = text.replace("\n", " ")

    if len(preview) > 350:
        preview = preview[:350] + "..."

    print(preview)

    print()