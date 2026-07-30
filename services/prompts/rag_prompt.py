from models.retrieved_document import RetrievedDocument
from models.memory_models import RetrievedMemory


class RAGPrompt:
    """
    Prompt template for Retrieval-Augmented Generation.
    """

    @staticmethod
    def build(
        question: str,
        context: list[RetrievedDocument],
        conversation_history: str = "",
        semantic_memories: list[RetrievedMemory] | None = None,
    ) -> str:
        """
        Build a prompt using retrieved context, conversation history,
        and relevant semantic memories.
        """

        context_text = "\n\n".join(
            f"[Document {i}]\n{document.text}"
            for i, document in enumerate(context, start=1)
        )

        history_section = ""

        if conversation_history:

            history_section = f"""
=========================
PREVIOUS CONVERSATION
=========================

{conversation_history}
"""

        semantic_memory_section = ""

        if semantic_memories:

            memory_blocks = []

            for index, memory in enumerate(
                semantic_memories,
                start=1,
            ):

                memory_blocks.append(
                    f"""
Memory {index}

{memory.content}
""".strip()
                )

            semantic_memory_section = f"""
=========================
RELEVANT PREVIOUS CONVERSATIONS
=========================

{chr(10).join(memory_blocks)}
"""

        return f"""
You are an expert Healthcare AI Assistant.

Answer the user's question ONLY using the information provided in the retrieved context.

Instructions:

Use the following sources of information in priority order:

1. Retrieved enterprise healthcare documents.
2. Relevant semantic memories from previous conversations.
3. Previous conversation history for conversational continuity.

Use semantic memories whenever the user's question asks about:

- Things they told you earlier
- Personal preferences
- Previous discussions
- Follow-up questions

If the retrieved documents do not contain the answer,
but the semantic memories do,
answer using the semantic memories.

Only respond with

"I don't have enough information from the provided documents or previous conversations."
when neither the retrieved documents nor the semantic memories contain the answer.

- Do NOT invent information.
- Do NOT use outside knowledge.
- If the answer is not present in the retrieved context, respond exactly with:

"I don't have enough information from the provided documents."

{history_section}

{semantic_memory_section}

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
        