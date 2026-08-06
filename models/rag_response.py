from dataclasses import dataclass

from models.evaluation_report import EvaluationReport
from models.retrieved_document import RetrievedDocument
from typing import Optional, Any
from models.answer_source import AnswerSource
from models.knowledge_source import KnowledgeSource


@dataclass
class RAGResponse:
    """
    Final response returned by the RAG pipeline.
    """

    question: str

    retrieved_documents: list[RetrievedDocument]
    
    answer_source: AnswerSource
    
    citations: list[Any]
    
    knowledge_sources: list[KnowledgeSource]

    evaluation: Optional[EvaluationReport] = None

    answer: str = ""
    
    
