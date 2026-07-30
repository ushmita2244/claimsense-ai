from enum import Enum


class RetrievalQuality(str, Enum):

    EXCELLENT = "Excellent"

    GOOD = "Good"

    AVERAGE = "Average"

    POOR = "Poor"