import uuid
from datetime import datetime
import streamlit as st


def delete_conversation(session_id: str):
    """
    Delete a conversation and update the active session.
    """

    conversations = st.session_state.conversations

    if session_id not in conversations:
        return

    del conversations[session_id]

    # No conversations remaining
    if not conversations:

        new_session = str(uuid.uuid4())

        conversations[new_session] = {
            "title": "New Chat",
            "messages": [],
            "created_at": datetime.now(),
        }

        st.session_state.current_session_id = new_session

    # Deleted currently opened conversation
    elif session_id == st.session_state.current_session_id:

        st.session_state.current_session_id = next(
            iter(conversations)
        )

    st.rerun()