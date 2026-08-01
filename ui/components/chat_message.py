import streamlit as st


def render_chat_message(
    role: str,
    content: str,
):
    """
    Render a chat message with a custom message bubble.
    Streamlit handles the avatar and sender layout.
    """

    css_class = (
        "user-message"
        if role == "user"
        else "ai-message"
    )

    with st.chat_message(role):

        st.markdown(
            f"""
<div class="{css_class}">
{content}
</div>
""",
            unsafe_allow_html=True,
        )