import streamlit as st

st.set_page_config(
    page_title="Prashant Kumar | AI Engineer",
    page_icon="🤖",
    layout="wide",
)

home = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
)

projects = st.Page(
    "pages/1_Projects.py",
    title="Projects",
    icon="💻",
)

skills = st.Page(
    "pages/skills.py",
    title="Skills",
    icon="🧠",
)

experience = st.Page(
    "pages/experience.py",
    title="Experience",
    icon="💼",
)

chatbot = st.Page(
    "pages/chatbot.py",
    title="AI Chat",
    icon="🤖",
)

contact = st.Page(
    "pages/contact.py",
    title="Contact",
    icon="📬",
)

pg = st.navigation(
    [
        home,
        projects,
        skills,
        experience,
        chatbot,
        contact,
    ],
    position="top",
)

pg.run()