from dataclasses import dataclass, field
from typing import Any
from models.knowledge_source import KnowledgeSource


@dataclass
class AIInsights:
    
    planner: str = "-"
    tool: str = "-"
    retrieval_quality: str = "-"
    memory_count: int = 0
    embedding_time: float = 0.0
    retrieval_time: float = 0.0
    prompt_time: float = 0.0
    llm_time: float = 0.0
    total_latency: float = 0.0
    knowledge_sources: list[KnowledgeSource] = field(default_factory=list)


@dataclass
class AgentResponse:

    answer: str
    insights: AIInsights
    citations: list[Any] = field(default_factory=list)