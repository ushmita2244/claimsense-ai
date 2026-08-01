def generate_title(first_message: str) -> str:
    """
    Generate a short conversation title from the first user message.
    """

    title = first_message.strip()

    if len(title) > 40:
        title = title[:40].rstrip() + "..."

    return title