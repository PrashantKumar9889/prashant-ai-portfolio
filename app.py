import streamlit as st


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Prashant Kumar | AI Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* ==================================================
       MAIN CONTENT CONTAINER
       ================================================== */

    .block-container {
        max-width: 1100px;
        margin-left: auto;
        margin-right: auto;
        padding-top: 1rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }


    /* ==================================================
       HIDE DEFAULT STREAMLIT NAVIGATION
       ================================================== */

    [data-testid="stSidebarNav"] {
        display: none;
    }


    /* ==================================================
       CUSTOM NAVBAR
       ================================================== */

    .custom-navbar {
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 8px;
        padding: 12px 0 20px 0;
        margin-bottom: 10px;
        border-bottom: 1px solid rgba(128, 128, 128, 0.20);
    }


    /* ==================================================
       NAVBAR BUTTONS
       ================================================== */

    .nav-button button {
        border: none !important;
        background: transparent !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        padding: 8px 14px !important;
        border-radius: 8px !important;
    }


    .nav-button button:hover {
        background: rgba(128, 128, 128, 0.12) !important;
    }


    /* ==================================================
       MOBILE RESPONSIVE
       ================================================== */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .custom-navbar {
            gap: 2px;
            flex-wrap: wrap;
        }

        .nav-button button {
            font-size: 13px !important;
            padding: 6px 8px !important;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# PAGE DEFINITIONS
# --------------------------------------------------

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


# --------------------------------------------------
# STREAMLIT NAVIGATION
# --------------------------------------------------

pg = st.navigation(
    [
        home,
        projects,
        skills,
        experience,
        chatbot,
        contact,
    ],
    position="hidden",
)


# --------------------------------------------------
# CUSTOM CENTERED NAVBAR
# --------------------------------------------------

st.markdown(
    '<div class="custom-navbar">',
    unsafe_allow_html=True,
)


col1, col2, col3, col4, col5, col6 = st.columns(
    [1, 1, 1, 1, 1, 1]
)


with col1:
    if st.button(
        "🏠 Home",
        use_container_width=True,
    ):
        st.switch_page(home)


with col2:
    if st.button(
        "💻 Projects",
        use_container_width=True,
    ):
        st.switch_page(projects)


with col3:
    if st.button(
        "🧠 Skills",
        use_container_width=True,
    ):
        st.switch_page(skills)


with col4:
    if st.button(
        "💼 Experience",
        use_container_width=True,
    ):
        st.switch_page(experience)


with col5:
    if st.button(
        "🤖 AI Chat",
        use_container_width=True,
    ):
        st.switch_page(chatbot)


with col6:
    if st.button(
        "📬 Contact",
        use_container_width=True,
    ):
        st.switch_page(contact)


st.markdown(
    "</div>",
    unsafe_allow_html=True,
)


# --------------------------------------------------
# RUN CURRENT PAGE
# --------------------------------------------------

pg.run()