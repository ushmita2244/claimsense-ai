import opik

from services.llm.gemini_service import GeminiService


class QueryRewriter:
    """
    Rewrites conversational follow-up questions into
    standalone questions for retrieval.
    """

    def __init__(self):

        self.llm = GeminiService()

    @opik.track(type="tool")
    def rewrite(
        self,
        question: str,
        conversation_history: str
    ) -> str:
        """
        Rewrite a conversational question into a standalone query.
        """

        if not conversation_history.strip():

            return question

        prompt = f"""
You are a query rewriting assistant.

Your job is to rewrite follow-up questions into complete standalone questions.

Rules:

- Preserve the original meaning.
- Use the previous conversation only to resolve references.
- Do not answer the question.
- Return ONLY the rewritten question.
- If the question is already standalone, return it unchanged.

=========================
PREVIOUS CONVERSATION
=========================

{conversation_history}

=========================
FOLLOW-UP QUESTION
=========================

{question}

=========================
STANDALONE QUESTION
=========================
"""

        rewritten_question = self.llm.generate_response(
            prompt
        )

        return rewritten_question.strip()