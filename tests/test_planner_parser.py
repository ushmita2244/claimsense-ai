import json

import pytest

from services.parser.planner_response_parser import PlannerResponseParser


def test_parse_tool_response():

    response = json.dumps(
        {
            "type": "tool",
            "tool_name": "calculator",
            "arguments": {
                "expression": "25 * 6"
            }
        }
    )

    result = PlannerResponseParser.parse(response)

    assert result.type == "tool"
    assert result.tool_request is not None
    assert result.tool_request.tool_name == "calculator"
    assert result.tool_request.arguments == {
        "expression": "25 * 6"
    }
    assert result.response is None


def test_parse_answer_response():

    response = json.dumps(
        {
            "type": "answer",
            "response": "Machine Learning is a subset of AI."
        }
    )

    result = PlannerResponseParser.parse(response)

    assert result.type == "answer"
    assert result.response == "Machine Learning is a subset of AI."
    assert result.tool_request is None


def test_invalid_json():

    with pytest.raises(ValueError):
        PlannerResponseParser.parse("This is not JSON")


def test_missing_type():

    response = json.dumps(
        {
            "response": "Hello"
        }
    )

    with pytest.raises(ValueError):
        PlannerResponseParser.parse(response)


def test_invalid_type():

    response = json.dumps(
        {
            "type": "invalid_type",
            "response": "Hello"
        }
    )

    with pytest.raises(ValueError):
        PlannerResponseParser.parse(response)


def test_tool_without_request():

    response = json.dumps(
        {
            "type": "tool"
        }
    )

    with pytest.raises(ValueError):
        PlannerResponseParser.parse(response)


def test_answer_without_response():

    response = json.dumps(
        {
            "type": "answer"
        }
    )

    with pytest.raises(ValueError):
        PlannerResponseParser.parse(response)