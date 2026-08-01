import streamlit as st


def render_metric_card(
    title: str,
    value: str,
):
    """
    Small reusable dashboard card.
    """

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-title">
{title}
</div>

<div class="metric-value">
{value}
</div>

</div>
""",
        unsafe_allow_html=True,
    )