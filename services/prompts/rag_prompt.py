from models.retrieved_document import RetrievedDocument

class RAGPrompt:
    """
    Prompt template for Retrieval-Augmented Generation.
    """

    @staticmethod
    def build(
        question: str,
        context: list[RetrievedDocument],
        conversation_history: str = ""
    ) -> str:
        """
        Build a prompt using retrieved context and optional conversation history.
        """

        context_text = "\n\n".join( document.text for document in context )
        
        history_section = ""

        if conversation_history:

            history_section = f"""
            =========================
            PREVIOUS CONVERSATION
            =========================

            {conversation_history}

            """

        return f"""
You are an expert Healthcare AI Assistant.

Answer the user's question ONLY using the information provided in the retrieved context.

Use the previous conversation only to understand references,
follow-up questions, or conversational context.

Do NOT use previous conversation as factual knowledge.

If the answer is not present in the retrieved context, respond exactly with:

"I don't have enough information from the provided documents."

Do not make up information.
Do not use outside knowledge.

{history_section}
=========================
RETRIEVED CONTEXT
=========================

{context_text}

=========================
CURRENT QUESTION
=========================

{question}

=========================
ANSWER
=========================
"""