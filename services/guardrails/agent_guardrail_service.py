import opik

from models.guardrail_result import GuardrailResult


class AgentGuardrailService:
    """
    Performs global safety validation before a request
    reaches the planner.

    Responsibilities:
    - Empty input validation
    - Prompt injection detection
    - Jailbreak detection
    - Dangerous instruction detection

    It does NOT perform domain validation.
    
    Represents the result of a guardrail validation.
    """

    def __init__(self):

        self.blocked_patterns = [

            # Prompt Injection
            "ignore previous instructions",
            "ignore all instructions",
            "forget previous instructions",
            "forget everything",
            "system prompt",
            "developer prompt",
            "developer message",
            "reveal your prompt",
            "show your prompt",

            # Jailbreak Attempts
            "jailbreak",
            "bypass",
            "override instructions",
            "act as chatgpt",
            "act as system",

            # Dangerous Instructions
            "drop table",
            "delete database",
            "truncate table",
            "rm -rf",
            "shutdown system",
        ]

    @opik.track(type="tool")
    def validate(
        self,
        question: str
    ) -> GuardrailResult:
        """
        Validate whether a request is safe to enter
        the agent workflow.
        """

        question = question.strip()

        if not question:
            return GuardrailResult(
                allowed=False,
                reason="Empty question."
            )

        lowered = question.lower()

        for pattern in self.blocked_patterns:

            if pattern in lowered:

                return GuardrailResult(
                    allowed=False,
                    reason="Unsafe request detected."
                )

        return GuardrailResult(
            allowed=True
        )