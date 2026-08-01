import streamlit as st
from models.agent_response import AIInsights
from ui.components.metric_card import render_metric_card

def render_ai_insights(
    insights: AIInsights,
):
    """
    Modern AI Insights dashboard.
    """

    with st.expander(
        "🧠 AI Insights",
        expanded=False,
    ):

        col1, col2 = st.columns(2)

        with col1:
            render_metric_card(
                "Planner",
                insights.planner,
            )

        with col2:
            render_metric_card(
                "Tool",
                insights.tool,
            )

        col1, col2 = st.columns(2)

        with col1:
            render_metric_card(
                "Retrieval",
                insights.retrieval_quality,
            )

        with col2:
            render_metric_card(
                "Memory",
                str(insights.memory_count),
            )

        st.markdown("#### ⚡ Pipeline Performance")

        col1, col2 = st.columns(2)

        with col1:
            render_metric_card(
                "Embedding",
                f"{insights.embedding_time:.3f}s",
            )

        with col2:
            render_metric_card(
                "Retrieval",
                f"{insights.retrieval_time:.3f}s",
            )