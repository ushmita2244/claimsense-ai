from google import genai

from core.config.settings import settings

client = genai.Client(api_key=settings.GOOGLE_API_KEY)

text = """
Health insurance covers hospitalization expenses
including surgeries and ICU admission.
"""

response = client.models.embed_content(
    model=settings.EMBEDDING_MODEL,
    contents=text
)

embedding = response.embeddings[0].values

print(f"Embedding Length: {len(embedding)}")
print(type(embedding))
print(type(embedding[0]))
print(embedding[:10])