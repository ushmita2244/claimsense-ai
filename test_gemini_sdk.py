from google import genai
from core.config.settings import settings

print("Starting...")

client = genai.Client(api_key=settings.GOOGLE_API_KEY)

print("Client created...")

response = client.models.generate_content(
    model=settings.MODEL_NAME,
    contents="Tell me 3 facts about AI engineering."
)

print("Response received...")
print(response.text)