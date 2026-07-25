from unittest.mock import Mock

from services.tools.knowledge_base_tool import KnowledgeBaseTool

from models.rag_response import RAGResponse
from models.tool_result import ToolResult
import pytest

def test_definition():

    tool = KnowledgeBaseTool(Mock())

    definition = tool.definition

    assert definition.name == "knowledge_base"

    assert "knowledge base" in definition.description.lower()

    assert len(definition.parameters) == 1

    parameter = definition.parameters[0]

    assert parameter.name == "question"

    assert parameter.type == "string"

    assert parameter.required is True
    

def test_execute():

    rag_service = Mock()

    rag_service.ask.return_value = RAGResponse(
        question="What is deductible?",
        answer="A deductible is the amount paid before insurance begins.",
        retrieved_documents=["doc1", "doc2"],
        evaluation={"score": 0.98}
    )

    tool = KnowledgeBaseTool(rag_service)

    result = tool.execute(
        question="What is deductible?"
    )

    rag_service.ask.assert_called_once_with(
        question="What is deductible?"
    )

    assert isinstance(result, ToolResult)

    assert result.output == (
        "A deductible is the amount paid before insurance begins."
    )

    assert result.metadata["retrieved_documents"] == [
        "doc1",
        "doc2"
    ]

    assert result.metadata["evaluation"] == {
        "score": 0.98
    }
    

def test_execute_with_no_documents():

    rag_service = Mock()

    rag_service.ask.return_value = RAGResponse(
        question="Unknown question",
        answer="I couldn't find relevant information.",
        retrieved_documents=[],
        evaluation=None
    )

    tool = KnowledgeBaseTool(rag_service)

    result = tool.execute(
        question="Unknown question"
    )

    assert result.output == (
        "I couldn't find relevant information."
    )

    assert result.metadata["retrieved_documents"] == []

    assert result.metadata["evaluation"] is None
    
    
import pytest


def test_execute_propagates_exception():

    rag_service = Mock()

    rag_service.ask.side_effect = RuntimeError(
        "RAG failed"
    )

    tool = KnowledgeBaseTool(rag_service)

    with pytest.raises(RuntimeError):

        tool.execute(
            question="Hello"
        )