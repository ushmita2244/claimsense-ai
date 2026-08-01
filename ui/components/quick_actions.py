import streamlit as st


def render_quick_actions():
    """
    Render suggested healthcare prompts on the landing page.
    """

    st.markdown("### 🚀 Try one of these")

    suggestions = [
    (
        "🩺 Disease Information",
        "Explain the symptoms, diagnosis, treatment, and prevention of Type 2 Diabetes."
    ),
    (
        "💊 Drug Interaction",
        "Can Metformin be safely taken together with Ibuprofen?"
    ),
    (
        "📚 Medical Concept",
        "Explain how insulin resistance develops and why it occurs."
    ),
    (
        "📊 Clinical Calculation",
        "Calculate the BMI of a 24-year-old female weighing 78 kg with a height of 5 feet 4 inches."
    ),
    (
        "🌐 Latest Research",
        "What are the latest WHO guidelines for COVID-19 prevention and vaccination?"
    ),
    (
        "🧠 AI Memory",
        "Uses previous conversations to personalize answers, summarize what we've discussed about diabetes."
    )
]

    cols = st.columns(2)

    for index, (title, prompt) in enumerate(suggestions):

        with cols[index % 2]:

            if st.button(
                title,
                key=f"suggestion_{index}",
                use_container_width=True,
            ):
                st.session_state.selected_prompt = prompt
                st.rerun()