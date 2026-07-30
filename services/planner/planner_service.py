from services.llm.base_llm import BaseLLM
from services.prompts.tool_planner_prompt import ToolPlannerPrompt
from services.parser.planner_response_parser import PlannerResponseParser
from services.tools.tool_executor import ToolExecutor
from models.planner_result import PlannerResult


class PlannerService:

    def __init__(
        self,
        llm: BaseLLM,
        tool_executor: ToolExecutor,
    ):

        self.llm = llm
        self.tool_executor = tool_executor

    def plan(
        self,
        query: str,
    ) -> PlannerResult:

        planner_prompt = ToolPlannerPrompt.build(
            query=query,
            tools=self.tool_executor.list_tools(),
        )

        planner_response = self.llm.generate_response(
            planner_prompt
        )

        return PlannerResponseParser.parse(
            planner_response
        )