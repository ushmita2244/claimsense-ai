from unittest.mock import Mock

from models.planner_result import PlannerResult

from services.agent.agent_service import AgentService


def test_agent_returns_direct_answer():

    llm = Mock()
    tool_executor = Mock()

    planner_prompt_builder = Mock()
    planner_parser = Mock()
    tool_result_prompt_builder = Mock()

    planner_prompt_builder.build.return_value = "planner prompt"

    planner_parser.parse.return_value = PlannerResult(
        type="answer",
        response="Hello! How can I help you today?"
    )

    llm.generate_response.return_value = "planner response"

    tool_executor.list_tools.return_value = []

    agent = AgentService(
        llm=llm,
        tool_executor=tool_executor,
        planner_prompt_builder=planner_prompt_builder,
        planner_parser=planner_parser,
        tool_result_prompt_builder=tool_result_prompt_builder
    )

    response = agent.generate_response("Hello")

    assert response == "Hello! How can I help you today?"

    planner_prompt_builder.build.assert_called_once()
    planner_parser.parse.assert_called_once()

    tool_executor.execute.assert_not_called()
    tool_result_prompt_builder.build.assert_not_called()

    assert llm.generate_response.call_count == 1