from services.llm.gemini_service import GeminiService

llm = GeminiService()

response = llm.generate_response("Tell 3 facts about AI engineering.")

print(response)