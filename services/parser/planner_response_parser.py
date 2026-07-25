import json

from models.planner_result import PlannerResult
from models.tool_request import ToolRequest


class PlannerResponseParser:
    """
    Parses the planner's JSON response into a PlannerResult.
    """

    @staticmethod
    def parse(response: str) -> PlannerResult:

        response = response.strip()

        try:
            
            # ==========================================
            # Remove Markdown Code Fences
            # ==========================================

            if response.startswith("```"):

                lines = response.splitlines()

                if lines and lines[0].startswith("```"):
                    lines = lines[1:]

                if lines and lines[-1].startswith("```"):
                    lines = lines[:-1]

                response = "\n".join(lines).strip()

            # ==========================================
            # Parse JSON
            # ==========================================

            data = json.loads(response)

        except json.JSONDecodeError as exc:
            
            print("\n========== CLEANED PLANNER RESPONSE ==========")
            print(response)
            print("==============================================\n")
            
            raise ValueError(
                "Planner returned invalid JSON."
            ) from exc

        response_type = data.get("type")

        if response_type == "tool":

            tool_name = data.get("tool_name")
            arguments = data.get("arguments")

            if tool_name is None:
                raise ValueError(
                    "Planner tool response missing 'tool_name'."
                )

            if arguments is None:
                raise ValueError(
                    "Planner tool response missing 'arguments'."
                )

            return PlannerResult(
                type="tool",
                tool_request=ToolRequest(
                    tool_name=tool_name,
                    arguments=arguments
                )
            )

        if response_type == "answer":

            response_text = data.get("response")

            if response_text is None:
                raise ValueError(
                    "Planner answer response missing 'response'."
                )

            return PlannerResult(
                type="answer",
                response=response_text
            )

        raise ValueError(
            f"Unknown planner response type: {response_type}"
        )