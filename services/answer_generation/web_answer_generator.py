from core.utils.timer import Timer

from models.answer_generation_result import AnswerGenerationResult
from models.answer_source import AnswerSource
from models.web_search_models import WebSearchRequest

from services.answer_generation.answer_generator import AnswerGenerator
from services.web_search.web_search_service import WebSearchService


class WebAnswerGenerator(AnswerGenerator):

    def __init__(self):

        self.web_search = WebSearchService()

    def generate(
        self,
        question,
        retrieved_documents,
        conversation_history,
        semantic_memories,
    ) -> AnswerGenerationResult:

        with Timer() as timer:

            response = self.web_search.search(
                WebSearchRequest(
                    question=question
                )
            )

        return AnswerGenerationResult(
            answer=response.answer,
            answer_source=AnswerSource.WEB_SEARCH,
            citations=response.sources,
            retrieved_documents=[],
            prompt_time=0.0,
            llm_time=timer.elapsed,
        )