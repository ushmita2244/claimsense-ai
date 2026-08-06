import streamlit as st
from models.agent_response import AIInsights
from models.knowledge_source import KnowledgeSource
from ui.components.metric_card import render_metric_card

SOURCE_ICONS = {
    KnowledgeSource.ENTERPRISE_KB: "📄",
    KnowledgeSource.CONVERSATION_MEMORY: "💬",
    KnowledgeSource.WEB_SEARCH: "🌐",
}

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
            
                # =====================================================
        # Knowledge Sources
        # =====================================================

        if insights.knowledge_sources:

            st.markdown("#### 📚 Knowledge Sources")

            for source in insights.knowledge_sources:
                
                icon = SOURCE_ICONS.get(source, "•")

                st.markdown(f"{icon} {source.value}")
                
        else:
            st.caption("No external knowledge sources used.")
                

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