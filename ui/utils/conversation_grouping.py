from collections import OrderedDict
from datetime import datetime, timedelta


def group_conversations(conversations: dict):

    groups = OrderedDict(
        {
            "Today": [],
            "Yesterday": [],
            "Last 7 Days": [],
            "Older": [],
        }
    )

    now = datetime.now()

    for session_id, conversation in reversed(list(conversations.items())):

        created = conversation["created_at"]

        delta = now.date() - created.date()

        if delta.days == 0:
            groups["Today"].append((session_id, conversation))

        elif delta.days == 1:
            groups["Yesterday"].append((session_id, conversation))

        elif delta.days <= 7:
            groups["Last 7 Days"].append((session_id, conversation))

        else:
            groups["Older"].append((session_id, conversation))

    return groups