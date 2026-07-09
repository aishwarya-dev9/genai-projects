import streamlit as st
from ai_helper import generate_email

# -----------------------------
# Configuration
# -----------------------------
TONES = [
    "Professional",
    "Friendly",
    "Apologetic",
    "Direct"
]

st.set_page_config(
    page_title="Local AI Email Assistant",
    page_icon="✉️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("🤖 About")

st.sidebar.info("""
### Local AI Email Assistant

Built using:

- Streamlit
- Ollama
- Llama 3

Runs completely offline.
""")

st.title("✉️ Local AI Email Assistant")

st.write(
    "Transform rough notes into professional emails using a Local LLM."
)

tone = st.selectbox(
    "Choose Email Tone",
    TONES
)

notes = st.text_area(
    "Enter your rough notes",
    height=180
)

if st.button("🚀 Generate Email", use_container_width=True):

    if not notes.strip():
        st.warning("Please enter some notes.")
    else:

        with st.spinner("Generating email..."):

            try:

                email = generate_email(
                    notes=notes,
                    tone=tone
                )

                st.success("Email generated successfully!")

                st.text_area(
                    "Generated Email",
                    email,
                    height=280
                )

                st.download_button(
                    "📥 Download Email",
                    email,
                    "generated_email.txt",
                    "text/plain"
                )

            except Exception as e:
                st.error(e)

st.divider()

st.caption("❤️ Built using Streamlit + Ollama + Llama 3")