from enum import Enum


class MemoryCategory(str, Enum):

    NONE = "none"

    IDENTITY = "identity"

    PROJECT = "project"

    GOAL = "goal"

    PREFERENCE = "preference"

    WORKFLOW = "workflow"

    HISTORY = "history"