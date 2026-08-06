from models.output_guardrail_models import (
    OutputGuardrailResult,
)
import opik

class OutputGuardrailService:
    """
    Validates the final LLM response before it is
    returned to the user.
    """

    MAX_RESPONSE_LENGTH = 10000

    ABSOLUTE_CLAIMS = [
        "guaranteed",
        "100%",
        "always",
        "never",
        "no side effects",
        "completely safe",
        "miracle cure",
        "instantly",
        "works for everyone",
        "will definitely",
        "will cure",
        "cures",
    ]
    
    FALLBACK_RESPONSE = (
        "I couldn't generate a response that meets the application's "
        "safety requirements. Please consult a qualified healthcare "
        "professional for medical advice."
    )

    DISCLAIMER = (
        "\n\n⚠️ **Medical Disclaimer:** "
        "This information is for educational purposes only and "
        "should not replace professional medical advice. "
        "Consult a qualified healthcare provider for diagnosis "
        "or treatment decisions."
    )

    @opik.track(
        type="guardrail"
    )
    def validate(
        self,
        response: str,
    ) -> OutputGuardrailResult:
        """
        Validate the LLM response.
        """

        violations: list[str] = []

        response = response.strip()

        # ==========================================
        # Empty Response
        # ==========================================

        if not response:

            violations.append("Empty response.")

        # ==========================================
        # Response Too Long
        # ==========================================

        if len(response) > self.MAX_RESPONSE_LENGTH:

            response = (
                response[: self.MAX_RESPONSE_LENGTH]
                + "\n\n..."
                + "\n(Response truncated.)"
            )

        # ==========================================
        # Absolute Medical Claims
        # ==========================================

        lower_response = response.lower()

        for phrase in self.ABSOLUTE_CLAIMS:

            if phrase in lower_response:

                violations.append(
                    f"Absolute medical claim detected: '{phrase}'."
                )

        # ==========================================
        # Return
        # ==========================================

        if violations:

            return OutputGuardrailResult(
                is_valid=False,
                response=self.FALLBACK_RESPONSE,
                violations=violations,
            )

        medical_keywords = [
            "medication",
            "drug",
            "treatment",
            "therapy",
            "dose",
            "tablet",
            "capsule",
            "chemotherapy",
            "antibiotic",
            "insulin",
        ]

        if any(keyword in lower_response for keyword in medical_keywords):

            response += self.DISCLAIMER

        result =  OutputGuardrailResult(
            is_valid=True,
            response=response,
        )

        opik.update_current_span(
            metadata={
                "guardrail_type": "output",
                "is_valid": result.is_valid,
                "violations": result.violations,
                "response_length": len(response),
            }
        )

        return result