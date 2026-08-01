import uuid

import streamlit as st

from src.bootstrap import build_agent
from ui.utils.title_generator import generate_title
from ui.components.sidebar import render_sidebar
from datetime import datetime
from ui.components.ai_insights import render_ai_insights
from models.agent_response import AgentResponse, AIInsights
from ui.components.hero import render_hero
from ui.components.styles import load_css
from ui.components.quick_actions import render_quick_actions
from ui.components.chat_message import render_chat_message


st.set_page_config(
    page_title="ClaimSense AI",
    page_icon="🏥",
    layout="wide",
)

load_css()


@st.cache_resource
def get_agent():
    return build_agent()


agent_service = get_agent()


# =====================================================
# Session State
# =====================================================

if "conversations" not in st.session_state:
    st.session_state.conversations = {}

if "current_session_id" not in st.session_state:

    session_id = str(uuid.uuid4())

    st.session_state.current_session_id = session_id

    st.session_state.conversations[session_id] = {
        "title": "New Chat",
        "messages": [],
        "created_at": datetime.now(),
    }
    
    
current_session = st.session_state.conversations[
    st.session_state.current_session_id
]

messages = current_session["messages"]


# =====================================================
# Sidebar
# =====================================================

render_sidebar()

# =====================================================
# Header / Landing Page
# =====================================================

if not messages:
    render_hero()
    render_quick_actions()
else:
    st.title("🏥 ClaimSense AI")
    st.caption("Enterprise Healthcare AI Copilot")

st.divider()


# =====================================================
# Display Previous Messages
# =====================================================

for message in messages:

    render_chat_message(
        role=message["role"],
        content=message["content"],
    )

    if (
        message["role"] == "assistant"
        and "insights" in message
    ):
        render_ai_insights(
            insights=message["insights"],
        )
        
        # Chat input

selected_prompt = st.session_state.pop(
    "selected_prompt",
    None,
)

prompt = selected_prompt or st.chat_input(
    "Ask a healthcare question..."
)

if prompt:

    # Display user message

    messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )
    
    if current_session["title"] == "New Chat":
        current_session["title"] = generate_title(prompt)

    render_chat_message(
        role="user",
        content=prompt,
    )

    # Generate assistant response

    with st.chat_message("assistant"):

        with st.spinner("Analyzing medical knowledge..."):

            try:

                response = agent_service.generate_response(
                    prompt=prompt,
                    session_id=st.session_state.current_session_id,
                )

            except Exception as e:

                st.error(str(e))

                response = AgentResponse(
                    answer="Sorry, something went wrong while generating the response.",
                    insights=AIInsights(),
                )

        render_chat_message(
            role="assistant",
            content=response.answer,
        )
        
        render_ai_insights(
            insights=response.insights,
        )

    messages.append(
        {
            "role": "assistant",
            "content": response.answer,
            "insights": response.insights,
        }
    )