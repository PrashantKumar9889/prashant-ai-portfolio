import streamlit as st

from backend.api_client import get_skills


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Skills | Prashant Kumar",
    page_icon="🧠",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🧠 Skills")

st.write(
    """
    Technologies and tools I use to build AI, GenAI,
    RAG and backend applications.
    """
)

st.divider()


# --------------------------------------------------
# GET SKILLS FROM FASTAPI
# --------------------------------------------------

skills_data = get_skills()

skills = skills_data["skills"]


# --------------------------------------------------
# DISPLAY SKILLS
# --------------------------------------------------

cols = st.columns(4)

for index, skill in enumerate(skills):

    with cols[index % 4]:

        st.container(
            border=True
        ).write(f"**{skill}**")