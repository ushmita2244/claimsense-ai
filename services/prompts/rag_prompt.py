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

Conversation History
====================

User:
...

Assistant:
...

Relevant Previous Conversations
===============================

Memory 1

Question:
I am allergic to penicillin.

Answer:
...

Memory 2

Question:
My father had diabetes.

Answer:
...

Retrieved Context
=================

<Enterprise documents>

Current Question
================

Which antibiotics are commonly used?

Answer
======

Answer the user's question ONLY using the information provided in the retrieved context.

Use the conversation history only to understand references,
follow-up questions, or conversational context.

Use relevant previous conversations to personalize the response
and maintain consistency with earlier interactions.

Use the retrieved context as the primary factual source.

Do NOT invent information.

If retrieved context conflicts with previous conversations,
trust the retrieved context.

If the answer is not present in the retrieved context, respond exactly with:

"I don't have enough information from the provided documents."

Do not make up information.
Do not use outside knowledge.

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