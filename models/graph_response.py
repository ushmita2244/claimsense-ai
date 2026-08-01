from dataclasses import dataclass
from typing import Any
from graph.state import AgentState
from models.agent_response import AIInsights


@dataclass
class GraphResponse:
    state: AgentState
    insights: AIInsights
    citations: list[Any]