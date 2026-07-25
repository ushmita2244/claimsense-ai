from unittest.mock import Mock

from models.tool_request import ToolRequest
from models.planner_result import PlannerResult

from services.agent.agent_service import AgentService
from services.tools.calculator_tool import CalculatorTool
from models.tool_result import ToolResult

def test_generate_response_without_tool():

    llm = Mock()
    tool_executor = Mock()
    
    tool_executor.list_tools.return_value = [
    CalculatorTool().definition
    ]

    llm.generate_response.return_value = """
    {
        "type": "answer",
        "response": "Machine Learning is a subset of AI."
    }
    """

    agent = AgentService(
        llm=llm,
        tool_executor=tool_executor
    )

    response = agent.generate_response(
        "What is Machine Learning?"
    )

    assert response == "Machine Learning is a subset of AI."

    tool_executor.execute.assert_not_called()

    assert llm.generate_response.call_count == 1
    
def test_generate_response_with_tool():

    llm = Mock()
    tool_executor = Mock()

    llm.generate_response.side_effect = [

        """
        {
            "type":"tool",
            "tool_name":"calculator",
            "arguments":{
                "expression":"25*6"
            }
        }
        """,

        "The answer is 150."
    ]

    tool_executor.list_tools.return_value = []

    tool_executor.execute.return_value = ToolResult(
    output="150",
    metadata={}
    )

    agent = AgentService(
        llm=llm,
        tool_executor=tool_executor
    )

    response = agent.generate_response(
        "What is 25*6?"
    )

    assert response == "The answer is 150."

    tool_executor.execute.assert_called_once()

    assert llm.generate_response.call_count == 2
    
import pytest

from unittest.mock import patch


def test_tool_without_tool_request():

    llm = Mock()
    tool_executor = Mock()

    agent = AgentService(
        llm=llm,
        tool_executor=tool_executor
    )

    planner_result = PlannerResult(
        type="tool",
        tool_request=None
    )

    with patch(
        "services.agent.agent_service.PlannerResponseParser.parse",
        return_value=planner_result
    ):

        llm.generate_response.return_value = "{}"

        tool_executor.list_tools.return_value = []

        with pytest.raises(ValueError):

            agent.generate_response("25*6")
            
def test_invalid_planner_type():

    llm = Mock()
    tool_executor = Mock()

    agent = AgentService(
        llm=llm,
        tool_executor=tool_executor
    )

    planner_result = PlannerResult.model_construct(
        type="invalid",
        tool_request=None,
        response=None
    )

    with patch(
        "services.agent.agent_service.PlannerResponseParser.parse",
        return_value=planner_result
    ):

        llm.generate_response.return_value = "{}"

        tool_executor.list_tools.return_value = []

        with pytest.raises(ValueError):

            agent.generate_response("Hello")