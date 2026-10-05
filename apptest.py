import streamlit as st

st.set_page_config(
    page_title="Prashant Kumar | AI Engineer",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
    """
    <style>
    .hero-title {
        font-size: 50px;
        font-weight: bold;
    }

    .hero-subtitle {
        font-size: 24px;
    }

    .hero-description {
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-title">
        Prashant Kumar
    </div>

    <div class="hero-subtitle">
        AI Engineer | GenAI | RAG | LLM Applications
    </div>

    <div class="hero-description">
        I build AI-powered applications using Python, RAG, LLMs,
        FastAPI and modern AI engineering techniques.
    </div>
    """,
    unsafe_allow_html=True
)