import streamlit as st

from ui.components.conversation_actions import delete_conversation


@st.dialog("Delete Conversation")
def delete_conversation_dialog(
    session_id: str,
    title: str,
):
    """
    Show a confirmation dialog before deleting a conversation.
    """

    st.warning(
        f"Are you sure you want to delete **{title}**?"
    )

    st.caption("This action cannot be undone.")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Cancel",
            use_container_width=True,
        ):
            st.rerun()

    with col2:

        if st.button(
            "Delete",
            type="primary",
            use_container_width=True,
        ):
            delete_conversation(session_id)
            
            
@st.dialog("Rename Conversation")
def rename_conversation_dialog(
    session_id: str,
    current_title: str,
):
    """
    Rename a conversation.
    """

    new_title = st.text_input(
        "Conversation title",
        value=current_title,
        max_chars=50,
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "Cancel",
            use_container_width=True,
            key=f"cancel_rename_{session_id}",
        ):
            st.rerun()

    with col2:

        if st.button(
            "Save",
            type="primary",
            use_container_width=True,
            key=f"save_rename_{session_id}",
        ):

            new_title = new_title.strip()

            if new_title:

                st.session_state.conversations[session_id]["title"] = new_title

            st.rerun()