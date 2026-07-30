from enum import Enum


class AnswerSource(str, Enum):
    """
    Represents the next action after retrieval.
    """

    KNOWLEDGE_BASE = "knowledge_base"
    
    WEB_SEARCH = "web_search"
    
    GUARDRAIL = "guardrail"