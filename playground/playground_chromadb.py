from google import genai

from core.config.settings import settings

from services.vector_db.chroma_service import ChromaService

client = genai.Client(
    api_key=settings.GOOGLE_API_KEY
)

vector_db = ChromaService()

documents = [
    "Health insurance covers hospitalization expenses including surgeries.",

    "Cancer prevention includes regular screening and healthy lifestyle.",

    "Diabetes patients should monitor blood sugar regularly.",

    "Heart disease risk can be reduced by exercising daily.",

    "Travel insurance covers flight cancellation and baggage loss.",

    "Hospital admission requires prior authorization from the insurance company.",

    "Vaccination helps prevent infectious diseases."
]

for index, document in enumerate(documents):
    response = client.models.embed_content( model=settings.EMBEDDING_MODEL, contents=document)

    embedding = response.embeddings[0].values
    
    vector_db.add_document(
    doc_id=f"doc_{index}",
    text=document,
    embedding=embedding)
    
query = "Does insurance pay hospital bills?"

query_response = client.models.embed_content(
    model=settings.EMBEDDING_MODEL,
    contents=query
)

query_embedding = query_response.embeddings[0].values

results = vector_db.search(
    query_embedding=query_embedding,
    top_k=3
)

print(results)

print("=" * 80)
print("TOP RESULTS")
print("=" * 80)

for document in results["documents"][0]:
    print(document)
    print("-" * 80)
