from sympy import SympifyError
from sympy import sympify

from models.knowledge_source import KnowledgeSource
from models.tool_definition import ToolDefinition
from services.tools.base_tool import BaseTool
from models.tool_parameter import ToolParameter
from models.tool_result import ToolResult


class CalculatorTool(BaseTool):

    @property
    def definition(
        self
    ) -> ToolDefinition:

        return ToolDefinition(
            name="calculator",

            description=(
                "Evaluates mathematical expressions."
            ),

            parameters=[
            ToolParameter(
                name="expression",
                description="Mathematical expression to evaluate.",
                type="string",
                required=True
                )
            ]
        )

    def execute(
        self,
        **kwargs
    ):

        expression = kwargs["expression"]

        try:

            result = sympify(expression)

            return ToolResult(
                output=str(result),
                metadata={
                    "expression": expression
                },
                knowledge_sources=[
                    KnowledgeSource.CALCULATOR,
                ],
            )

        except SympifyError:

            return ToolResult(
                output="Invalid mathematical expression.",
                metadata={
                    "expression": expression
                },
                knowledge_sources=[
                    KnowledgeSource.CALCULATOR,
                ],
            )