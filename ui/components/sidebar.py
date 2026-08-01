# src/ui/components/sidebar.py

import uuid
import streamlit as st
from ui.components.dialogs import (delete_conversation_dialog,rename_conversation_dialog,)
from datetime import datetime
from ui.utils.conversation_grouping import group_conversations

def render_sidebar():
    """
    Render the application sidebar.
    Returns the currently selected session id.
    """

    with st.sidebar:

        st.title("🏥 ClaimSense AI")

        st.markdown("---")

        if st.button(
            "🆕 New Chat",
            use_container_width=True,
        ):

            session_id = str(uuid.uuid4())

            st.session_state.conversations[session_id] = {
                "title": "New Chat",
                "messages": [],
                "created_at": datetime.now(),
            }

            st.session_state.current_session_id = session_id

            st.rerun()

        st.markdown("---")

        render_conversation_list()

    return st.session_state.current_session_id


def render_conversation_list():
    """
    Render conversations grouped by date.
    """

    groups = group_conversations(
        st.session_state.conversations
    )

    for group_name, conversations in groups.items():

        if not conversations:
            continue

        st.markdown(
            f"**{group_name.upper()}**"
        )

        for session_id, conversation in conversations:

            render_conversation_item(
                session_id,
                conversation,
            )

        st.markdown("---")
        
        
def render_conversation_item(
    session_id: str,
    conversation: dict,
):
    """
    Render a single conversation in the sidebar.
    """

    is_active = (
        session_id
        == st.session_state.current_session_id
    )

    col1, col2 = st.columns([6, 1])

    # -------------------------
    # Conversation Button
    # -------------------------

    with col1:

        title = conversation["title"]

        if is_active:
            title = f"🟢 {title}"

        if st.button(
            title,
            key=f"chat_{session_id}",
            use_container_width=True,
        ):

            st.session_state.current_session_id = session_id
            st.rerun()

    # -------------------------
    # Conversation Actions
    # -------------------------

    with col2:

        with st.popover(
            "⋮",
            use_container_width=True,
        ):

            if st.button(
                "✏ Rename",
                key=f"rename_{session_id}",
                use_container_width=True,
            ):

                rename_conversation_dialog(
                    session_id,
                    conversation["title"],
                )

            if st.button(
                "🗑 Delete",
                key=f"delete_{session_id}",
                use_container_width=True,
            ):
                delete_conversation_dialog(
                    session_id,
                    conversation["title"],
                )