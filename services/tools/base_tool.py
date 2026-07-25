from abc import ABC
from abc import abstractmethod

from models.tool_definition import ToolDefinition
from models.tool_result import ToolResult


class BaseTool(ABC):

    @property
    @abstractmethod
    def definition(self) -> ToolDefinition:
        """
        Returns the metadata describing this tool.
        """
        pass

    @abstractmethod
    def execute(self, **kwargs) -> ToolResult:
        """
        Execute the tool and return a structured result.
        """
        pass