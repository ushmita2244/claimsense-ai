from services.llm.base_llm import BaseLLM
from services.prompts.tool_result_prompt import ToolResultPrompt
from models.tool_request import ToolRequest
from models.tool_result import ToolResult


class ResponseGenerationService:

    def __init__(
        self,
        llm: BaseLLM,
    ):

        self.llm = llm
        
    def generate_from_tool(
        self,
        question: str,
        tool_request: ToolRequest,
        tool_result: ToolResult,
    ) -> str:

        tool_prompt = ToolResultPrompt.build(
            question=question,
            tool_name=tool_request.tool_name,
            tool_output=tool_result.output,
            metadata=tool_result.metadata,
        )

        return self.llm.generate_response(
            tool_prompt
        )