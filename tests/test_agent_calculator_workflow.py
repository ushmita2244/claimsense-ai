from unittest.mock import Mock

from models.planner_result import PlannerResult
from models.tool_request import ToolRequest
from models.tool_result import ToolResult

from services.agent.agent_service import AgentService


def test_agent_executes_calculator_tool():

    llm = Mock()
    tool_executor = Mock()

    planner_prompt_builder = Mock()
    planner_parser = Mock()
    tool_result_prompt_builder = Mock()

    planner_prompt_builder.build.return_value = "planner prompt"

    planner_parser.parse.return_value = PlannerResult(
        type="tool",
        tool_request=ToolRequest(
            tool_name="calculator",
            arguments={
                "expression": "(12 + 8) * 5"
            }
        )
    )

    tool_executor.list_tools.return_value = []

    tool_executor.execute.return_value = ToolResult(
        output="100",
        metadata={
            "expression": "(12 + 8) * 5"
        }
    )

    tool_result_prompt_builder.build.return_value = "tool prompt"

    llm.generate_response.side_effect = [
        "planner response",
        "The answer is 100."
    ]

    agent = AgentService(
        llm=llm,
        tool_executor=tool_executor,
        planner_prompt_builder=planner_prompt_builder,
        planner_parser=planner_parser,
        tool_result_prompt_builder=tool_result_prompt_builder
    )

    response = agent.generate_response(
        "Calculate (12 + 8) * 5"
    )

    assert response == "The answer is 100."

    planner_prompt_builder.build.assert_called_once()
    planner_parser.parse.assert_called_once()
    tool_executor.execute.assert_called_once()
    tool_result_prompt_builder.build.assert_called_once()

    assert llm.generate_response.call_count == 2