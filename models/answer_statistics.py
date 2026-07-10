from dataclasses import dataclass


@dataclass
class AnswerStatistics:
    """
    Statistics about the generated answer.
    """

    character_count: int

    word_count: int

    line_count: int