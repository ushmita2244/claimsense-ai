class WebSearchPromptBuilder:
    """
    Builds the prompt used by the LLM to generate the final
    answer from medical web search results.
    """

    @staticmethod
    def build(
        question: str,
        search_results: str
    ) -> str:
        """
        Build the prompt for summarizing medical web search results.

        Args:
            question: User's original question.
            search_results: Combined search results from Tavily.

        Returns:
            Prompt for the LLM.
        """

        return f"""
You are ClaimSense-AI, an Enterprise Healthcare Copilot.

Your task is to answer the user's question ONLY using the provided medical web search results.

Instructions
------------

1. Answer ONLY using the provided search results.
2. Do NOT invent or assume information.
3. If the search results are insufficient, clearly state that the available information is insufficient.
4. Produce a concise, factual, and well-structured answer.
5. Do NOT mention Tavily, web search or search engines.
6. Preserve important medical terminology.
7. Do NOT generate citations in the answer.
8. The sources will be added separately.

==================================================
RESPONSE LENGTH
==================================================

- Keep responses concise whenever possible.
- If the search results contain many items, summarize instead of listing everything.
- Highlight the most important or most recent information first.
- Group similar items together.
- Avoid repeating similar information.
- Unless the user explicitly asks for a complete list, do NOT enumerate every search result.
- Aim for approximately 300–600 words for large result sets.

User Question
-------------

{question}

Medical Web Search Results
--------------------------

{search_results}
""".strip()