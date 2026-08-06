from enum import Enum


class KnowledgeSource(str, Enum):
    """
    Represents the knowledge sources used
    to generate an answer.
    """

    ENTERPRISE_KB = "Enterprise Knowledge Base"

    CONVERSATION_MEMORY = "Conversation Memory"

    WEB_SEARCH = "Web Search"
    
    SQL_DATABASE = "SQL Database"
    
    CALCULATOR = "Calculator"
    
    GENERAL_MEDICAL_KNOWLEDGE = "general medical knowledge"