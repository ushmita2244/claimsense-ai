import pytest

from services.guardrails.output_guardrail_service import (
    OutputGuardrailService,
)


class TestOutputGuardrailService:

    @pytest.fixture
    def service(self):
        return OutputGuardrailService()

    def test_valid_response(self, service):

        response = (
            "Treatment options depend on the patient's diagnosis."
        )

        result = service.validate(response)

        assert result.is_valid is True
        assert result.response == response
        assert result.violations == []

    def test_empty_response(self, service):

        result = service.validate("")

        assert result.is_valid is False
        assert result.response == service.FALLBACK_RESPONSE
        assert "Empty response." in result.violations

    def test_absolute_claim(self, service):

        result = service.validate(
            "This medicine will cure cancer."
        )

        assert result.is_valid is False

        assert any(
            "will cure" in violation
            for violation in result.violations
        )

    def test_response_too_long(self, service):

        response = "A" * (service.MAX_RESPONSE_LENGTH + 1)

        result = service.validate(response)

        assert result.is_valid is False

        assert (
            "Response exceeds maximum length."
            in result.violations
        )

    def test_multiple_violations(self, service):

        response = (
            "This treatment is guaranteed to cure cancer. "
            * 500
        )

        result = service.validate(response)

        assert result.is_valid is False

        assert len(result.violations) >= 2