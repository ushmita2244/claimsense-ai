from services.ingestion.ingestion_service import IngestionService

ingestion = IngestionService()

ingestion.vector_db.clear()

results = ingestion.ingest_directory(
    "data/raw"
)

print("=" * 80)
print("DIRECTORY INGESTION SUMMARY")
print("=" * 80)

total_chunks = 0

for result in results:

    print()

    print(f"PDF : {result['file_name']}")

    print(f"Chunks : {result['chunks_created']}")

    total_chunks += result["chunks_created"]

print()

print("=" * 80)

print(f"TOTAL PDFs : {len(results)}")

print(f"TOTAL CHUNKS : {total_chunks}")

print("=" * 80)