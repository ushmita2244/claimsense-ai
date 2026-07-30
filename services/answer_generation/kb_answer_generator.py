from core.utils.timer import Timer

from models.answer_generation_result import AnswerGenerationResult
from models.answer_source import AnswerSource

from services.attribution.attribution_service import AttributionService
from services.llm.gemini_service import GeminiService
from services.prompts.rag_prompt import RAGPrompt

from services.answer_generation.answer_generator import AnswerGenerator


class KBAnswerGenerator(AnswerGenerator):

    def __init__(self):

        self.llm = GeminiService()

        self.attribution = AttributionService()

    def generate(
        self,
        question,
        retrieved_documents,
        conversation_history,
        semantic_memories,
    ) -> AnswerGenerationResult:

        citations = self.attribution.build(
            retrieved_documents
        )

        with Timer() as timer:

            prompt = RAGPrompt.build(
                question=question,
                context=retrieved_documents,
                conversation_history=conversation_history,
                semantic_memories=semantic_memories or [],
            )

        prompt_time = timer.elapsed

        with Timer() as timer:

            answer = self.llm.generate_response(
                prompt
            )

        llm_time = timer.elapsed

        return AnswerGenerationResult(
            answer=answer,
            answer_source=AnswerSource.KNOWLEDGE_BASE,
            citations=citations,
            retrieved_documents=retrieved_documents,
            prompt_time=prompt_time,
            llm_time=llm_time,
        )