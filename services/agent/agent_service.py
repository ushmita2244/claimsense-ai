from services.llm.base_llm import BaseLLM
from services.tools.tool_executor import ToolExecutor

from services.prompts.tool_planner_prompt import ToolPlannerPrompt
from services.prompts.tool_result_prompt import ToolResultPrompt

from services.parser.planner_response_parser import PlannerResponseParser
from services.guardrails.agent_guardrail_service import AgentGuardrailService
import opik
from services.guardrails.output_guardrail_service import (
    OutputGuardrailService,
)


class AgentService:

    def __init__(
        self,
        llm: BaseLLM,
        tool_executor: ToolExecutor,
        planner_parser=PlannerResponseParser,
        planner_prompt_builder=ToolPlannerPrompt,
        agent_guardrail=AgentGuardrailService,
        tool_result_prompt_builder=ToolResultPrompt,
        output_guardrail: OutputGuardrailService | None = None,
    ):

        self.llm = llm
        self.tool_executor = tool_executor
        self.planner_prompt_builder = planner_prompt_builder
        self.planner_parser = planner_parser
        self.tool_result_prompt_builder = tool_result_prompt_builder
        self.agent_guardrail = agent_guardrail
        self.output_guardrail = (
            output_guardrail
            if output_guardrail is not None
            else OutputGuardrailService()
        )

    @opik.track(type= "general")
    def generate_response(
        self,
        prompt: str,
        session_id: str = "default"
    ) -> str:
        
        guardrail_result = self.agent_guardrail.validate(prompt)

        if not guardrail_result.allowed:
            return guardrail_result.reason

        planner_prompt = self.planner_prompt_builder.build(

            query=prompt,

            tools=self.tool_executor.list_tools()
        )

        planner_response = self.llm.generate_response(
            planner_prompt
        )
        print("\n========== PLANNER RESPONSE ==========")
        print(planner_response)
        print("======================================\n")

        planner_result = self.planner_parser.parse(
            planner_response
        )

        if planner_result.type == "answer":
            return self._validate_output(
                planner_result.response
            )

        if planner_result.type != "tool":
            raise ValueError(
                f"Unsupported planner response type: {planner_result.type}"
            )

        if planner_result.tool_request is None:
            raise ValueError(
                "Planner returned type='tool' but no ToolRequest was provided."
            )

        tool_request = planner_result.tool_request
        
        if tool_request.tool_name == "knowledge_base":
            tool_request.arguments = tool_request.arguments or {}
            tool_request.arguments["session_id"] = session_id

        tool_result = self.tool_executor.execute(tool_request)

        tool_prompt = self.tool_result_prompt_builder.build(
            question=prompt,
            tool_name=tool_request.tool_name,
            tool_output=tool_result.output,
            metadata=tool_result.metadata
        )

        final_response = self.llm.generate_response(
            tool_prompt
        )

        return self._validate_output(
            final_response
        )
    
    
    def _validate_output(
        self,
        response: str,
    ) -> str:
        
        """
        Validate the final LLM response before returning it.
        """

        return self.output_guardrail.validate(
            response
        ).response