class MemoryExtractionPrompt:

    @staticmethod
    def build(
        question: str,
        answer: str,
    ) -> str:

        return f"""
You are responsible for extracting long-term semantic memories.

Your job is to decide whether the conversation contains durable information
that will improve future interactions.

Store ONLY information that is useful in future conversations.

Examples of memories to store:

✓ User role
✓ User profession
✓ User expertise
✓ User preferences
✓ User communication style
✓ User ongoing project
✓ User long-term goals
✓ User organisation
✓ User workflow preferences

Do NOT store:

✗ Greetings
✗ Small talk
✗ Jokes
✗ Temporary facts
✗ Random personal trivia
✗ One-time requests
✗ Questions themselves

Conversation

User:
{question}

Assistant:
{answer}

Return ONLY valid JSON.

Example 1

{{
    "should_store": true,
    "memory": "User is an oncologist."
}}

Example 2

{{
    "should_store": true,
    "memory": "User prefers concise explanations."
}}

Example 3

{{
    "should_store": false,
    "memory": ""
}}
"""