import streamlit as st


FEATURES = [
    (
        "🩺",
        "Disease Intelligence",
        "Understand diseases, symptoms, diagnosis and treatments.",
        "Explain Type 2 Diabetes in simple language.",
    ),
    (
        "💊",
        "Drug Interaction",
        "Analyze medication interactions and contraindications.",
        "Can Paracetamol and Ibuprofen be taken together?",
    ),
    (
        "📄",
        "Claims Support",
        "Understand healthcare insurance policies and claims.",
        "Explain prior authorization in health insurance.",
    ),
    (
        "📊",
        "Clinical Calculator",
        "BMI, dosage calculations and medical formulas.",
        "Calculate BMI for a 24-year-old female weighing 60 kg and height 165 cm.",
    ),
    (
        "🌍",
        "Medical Research",
        "Search recent medical guidelines and research.",
        "Latest WHO guidelines on COVID-19.",
    ),
    (
        "🧠",
        "AI Memory",
        "Uses previous conversations to personalize answers.",
        "Summarize what we've discussed about diabetes.",
    ),
]


def render_feature_cards():

    st.markdown("## ✨ What can ClaimSense AI help you with?")

    for i in range(0, len(FEATURES), 3):

        cols = st.columns(3)

        for col, feature in zip(cols, FEATURES[i:i+3]):

            icon, title, desc, prompt = feature

            with col:

                st.markdown(
                    f"""
### {icon} {title}

{desc}
"""
                )

                if st.button(
                    "Start →",
                    key=f"feature_{title}",
                    use_container_width=True,
                ):
                    st.session_state.selected_prompt = prompt
                    st.rerun()