from services.guardrails.output_guardrail_service import OutputGuardrailService


class OutputValidationService:

    def __init__(
        self,
        output_guardrail: OutputGuardrailService,
    ):
        self.output_guardrail = output_guardrail

    def validate(
        self,
        response: str,
    ) -> str:

        return self.output_guardrail.validate(
            response
        ).response