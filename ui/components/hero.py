import streamlit as st


def render_hero():

    # ==================================================
    # Hero Banner
    # ==================================================

    st.markdown(
        """
<div class="hero">

<div class="hero-title">
🏥 ClaimSense AI
</div>

<div class="hero-subtitle">
Enterprise Healthcare Intelligence Platform
</div>

<div style="margin-top:18px;font-size:17px;">

🧠 AI Agents&nbsp;&nbsp;&nbsp;&nbsp;
📚 Enterprise RAG&nbsp;&nbsp;&nbsp;&nbsp;
🌐 Medical Search&nbsp;&nbsp;&nbsp;&nbsp;
💾 Long-Term Memory&nbsp;&nbsp;&nbsp;&nbsp;
⚡ LangGraph

</div>

</div>
""",
        unsafe_allow_html=True,
    )

    # ==================================================
    # Section Heading
    # ==================================================

    st.markdown(
        """
<div class="section-title">
✨ What can ClaimSense AI help you with?
</div>
""",
        unsafe_allow_html=True,
    )

    # ==================================================
    # Feature Cards
    # ==================================================

    row1 = st.columns(3)

    with row1[0]:
        st.markdown(
            """
<div class="feature">

<div class="feature-icon">🩺</div>

<div class="feature-title">
Disease Intelligence
</div>

<div class="feature-desc">
Understand diseases, symptoms, diagnosis,
clinical guidelines and treatments.
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    with row1[1]:
        st.markdown(
            """
<div class="feature">

<div class="feature-icon">💊</div>

<div class="feature-title">
Drug Interaction
</div>

<div class="feature-desc">
Analyze medication interactions,
contraindications and safety.
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    with row1[2]:
        st.markdown(
            """
<div class="feature">

<div class="feature-icon">📄</div>

<div class="feature-title">
Claims Support
</div>

<div class="feature-desc">
Understand insurance policies,
claims and prior authorization.
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    row2 = st.columns(3)

    with row2[0]:
        st.markdown(
            """
<div class="feature">

<div class="feature-icon">📊</div>

<div class="feature-title">
Clinical Calculator
</div>

<div class="feature-desc">
BMI, dosage calculations,
clinical formulas and more.
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    with row2[1]:
        st.markdown(
            """
<div class="feature">

<div class="feature-icon">🌍</div>

<div class="feature-title">
Medical Research
</div>

<div class="feature-desc">
Search trusted medical evidence,
guidelines and publications.
</div>

</div>
""",
            unsafe_allow_html=True,
        )

    with row2[2]:
        st.markdown(
            """
<div class="feature">

<div class="feature-icon">🧠</div>

<div class="feature-title">
AI Memory
</div>

<div class="feature-desc">
Remembers previous conversations
to provide personalized responses.
</div>

</div>
""",
            unsafe_allow_html=True,
        )