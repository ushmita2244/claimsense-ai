from models.answer_statistics import AnswerStatistics


class AnswerStatisticsService:
    """
    Computes statistics about the generated answer.
    """

    def analyze(
        self,
        answer: str
    ) -> AnswerStatistics:

        return AnswerStatistics(

            character_count=len(answer),

            word_count=len(answer.split()),

            line_count=len(answer.splitlines())

        )