class RAGPrompt:
    """
    Prompt template for Retrieval-Augmented Generation.
    """

    @staticmethod
    def build(
        question: str,
        context: list[str]
    ) -> str:
        """
        Build a prompt using retrieved context.
        """

        context_text = "\n\n".join(context)

        return f"""
You are an expert Healthcare AI Assistant.

Answer the user's question ONLY using the information provided in the context below.

If the answer is not present in the context, respond exactly with:

"I don't have enough information from the provided documents."

Do not make up information.
Do not use outside knowledge.

=========================
CONTEXT
=========================

{context_text}

=========================
QUESTION
=========================

{question}

=========================
ANSWER
=========================
"""