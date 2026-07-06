from google import genai
from core.config.settings import settings
import numpy as np

client = genai.Client(
    api_key=settings.GOOGLE_API_KEY
)

documents = [

    "Health insurance covers hospitalization expenses including surgeries.",

    "Cancer prevention includes regular screening and healthy lifestyle.",

    "Diabetes patients should monitor blood sugar regularly.",

    "Heart disease risk can be reduced by exercising daily.",

    "Travel insurance covers flight cancellation and baggage loss.",

    "Hospital admission requires prior authorization from the insurance company.",

    "Vaccination helps prevent infectious diseases."
]

knowledge_base = []

for document in documents:

    response = client.models.embed_content(
        model=settings.EMBEDDING_MODEL,
        contents=document
    )

    embedding = response.embeddings[0].values

    knowledge_base.append(
        {
            "text": document,
            "embedding": embedding
        }
    )

# print(knowledge_base[0])

query = "Does insurance pay hospital bills?"

query_response = client.models.embed_content(
    model=settings.EMBEDDING_MODEL,
    contents=query
)

query_embedding = query_response.embeddings[0].values

def cosine_similarity(vec1, vec2):

    vec1 = np.array(vec1)
    vec2 = np.array(vec2)

    dot = np.dot(vec1, vec2)

    mag1 = np.linalg.norm(vec1)

    mag2 = np.linalg.norm(vec2)

    return dot / (mag1 * mag2)


results = []

for item in knowledge_base:

    score = cosine_similarity(
        query_embedding,
        item["embedding"]
    )

    results.append(
        {
            "text": item["text"],
            "score": score
        }
    )
    

results.sort(
    key=lambda x: x["score"],
    reverse=True
)


print("=" * 80)
print("TOP MATCHES")
print("=" * 80)

for result in results[:3]:

    print()

    print(result["text"])

    print(f"Similarity : {result['score']:.4f}")
    
