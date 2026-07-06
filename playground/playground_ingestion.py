from services.ingestion.ingestion_service import IngestionService

ingestion = IngestionService()

# Start fresh every time
ingestion.vector_db.clear()

result = ingestion.ingest_pdf(
    "data/raw/2024-guide-to-preventing-cancer-web.pdf"
)

print("=" * 80)
print("INGESTION SUMMARY")
print("=" * 80)

print(f"PDF File              : {result['file_name']}")
print(f"Characters Loaded     : {result['characters_loaded']}")
print(f"Chunks Created        : {result['chunks_created']}")
print(f"Documents Stored      : {result['documents_in_collection']}")

print("=" * 80)