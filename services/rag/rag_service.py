from services.prompts.rag_prompt import RAGPrompt

from services.llm.gemini_service import GeminiService
from services.retrieval.retriever import Retriever
from models.rag_response import RAGResponse
from services.evaluation.diagnostics_service import DiagnosticsService

class RAGService:
    """
    Retrieval-Augmented Generation Service.
    """

    def __init__(self):

        self.retriever = Retriever()
        self.llm = GeminiService()
        self.diagnostics = DiagnosticsService()

    def ask(
        self,
        question: str
    ) -> RAGResponse:
        """
        Answer a user's question using Retrieval-Augmented Generation.
        """

        # Retrieve relevant chunks
        retrieved_documents = self.retriever.retrieve(question)
        
        diagnostics = self.diagnostics.analyze( retrieved_documents)

        # Build prompt
        prompt = RAGPrompt.build(
            question=question,
            context=retrieved_documents
        )

        # Generate response
        answer = self.llm.generate_response(prompt)

        return RAGResponse(
            question=question,
            retrieved_documents=retrieved_documents,
            diagnostics=diagnostics,
            answer=answer
            )