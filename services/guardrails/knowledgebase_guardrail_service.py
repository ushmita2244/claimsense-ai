import re

import opik

from models.guardrail_result import GuardrailResult
from models.memory_models import RetrievedMemory


class KnowledgeBaseGuardrailService:
    """
    Validates whether a user question is allowed
    to enter the RAG pipeline.
    """

    def __init__(self):

        self.healthcare_keywords = {

            "cancer",
            "tumor",
            "tumour",
            "oncology",
            "breast",
            "lung",
            "colon",
            "chemotherapy",
            "radiation",
            "diagnosis",
            "diagnose",
            "treatment",
            "therapy",
            "symptom",
            "symptoms",
            "disease",
            "patient",
            "medical",
            "medicine",
            "doctor",
            "hospital",
            "screening",
            "biopsy",
            "mri",
            "ct",
            "pet",
            "hpv"
        }

        self.blocked_patterns = [

            "ignore previous instructions",
            "ignore all instructions",
            "forget previous instructions",
            "forget everything",
            "system prompt",
            "reveal your prompt",
            "show your prompt",
            "developer message",
            "act as chatgpt",
            "jailbreak",
            "bypass",
            "override instructions"
        ]

    @opik.track(type="tool")
    def validate(
        self,
        question: str,
        semantic_memories: list[RetrievedMemory] | None = None,
    ) -> GuardrailResult:
        """
        Validate whether a question should
        enter the RAG pipeline.
        """

        question = question.strip()

        # ==========================================
        # Empty Query Check
        # ==========================================

        if not question:

            return GuardrailResult(
                allowed=False,
                reason="Empty question."
            )

        # ==========================================
        # Prompt Injection Check
        # ==========================================

        lowered = question.lower()

        for pattern in self.blocked_patterns:

            if pattern in lowered:

                return GuardrailResult(
                    allowed=False,
                    reason="Prompt injection detected."
                )

        # ==========================================
        # Domain Check
        # ==========================================

        words = set(
            re.findall(
                r"\b[a-zA-Z]+\b",
                lowered
            )
        )
        
        # If we already have relevant semantic memories,
        # allow the request to continue even if it isn't healthcare.

        if semantic_memories:
            return GuardrailResult(
                allowed=True,
                reason="Semantic memory query."
            )
        
        if self._is_healthcare_question(words):

            return GuardrailResult(
                allowed=True,
                reason="Healthcare question."
            )
            

        return GuardrailResult(
            allowed=False,
            reason="Question is outside the supported healthcare domain."
        )
        
    def _is_healthcare_question(
        self,
        words: set[str]
    ) -> bool:

        return bool(
            words.intersection(
                self.healthcare_keywords
            )
        )
    
    