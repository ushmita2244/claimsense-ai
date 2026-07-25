import pytest

from models.tool_request import ToolRequest

from services.tools.tool_executor import ToolExecutor
from services.tools.tool_registry import ToolRegistry
from services.tools.calculator_tool import CalculatorTool


@pytest.fixture
def tool_executor():

    registry = ToolRegistry()

    registry.register_tool(
        CalculatorTool()
    )

    return ToolExecutor(registry)


def test_execute_calculator_tool(tool_executor):

    request = ToolRequest(
        tool_name="calculator",
        arguments={
            "expression": "25 * 6"
        }
    )

    result = tool_executor.execute(request)

    assert result.output == "150"

    assert result.metadata["expression"] == "25 * 6"


def test_execute_parentheses(tool_executor):

    request = ToolRequest(
        tool_name="calculator",
        arguments={
            "expression": "(18 + 7) * 4"
        }
    )

    result = tool_executor.execute(request)

    assert result.output == "100"


def test_execute_invalid_expression(tool_executor):

    request = ToolRequest(
        tool_name="calculator",
        arguments={
            "expression": "abc+xyz"
        }
    )

    result = tool_executor.execute(request)

    assert result.output == "abc + xyz"


def test_unknown_tool(tool_executor):

    request = ToolRequest(
        tool_name="weather",
        arguments={}
    )

    with pytest.raises(ValueError) as exc:

        tool_executor.execute(request)

    assert str(exc.value) == "Unknown tool: weather"


def test_list_tools(tool_executor):

    tools = tool_executor.list_tools()

    assert len(tools) == 1

    assert tools[0].name == "calculator"

    assert tools[0].description == "Evaluates mathematical expressions."
    

def test_execute_passes_arguments(tool_executor):

    request = ToolRequest(
        tool_name="calculator",
        arguments={
            "expression": "5 ** 3"
        }
    )

    result = tool_executor.execute(request)

    assert result.output == "125"