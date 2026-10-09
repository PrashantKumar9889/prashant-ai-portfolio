import json
import streamlit as st
from backend.api_client import get_projects


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Projects | Prashant Kumar",
    page_icon="💻",
    layout="wide"
)


# --------------------------------------------------
# LOAD PROJECTS
# --------------------------------------------------


projects_data = get_projects()
projects = projects_data["projects"]


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("💻 Projects")

st.write(
    """
    A collection of AI engineering, Generative AI and
    data-focused projects that demonstrate my practical
    experience building real-world applications.
    """
)

st.divider()


# --------------------------------------------------
# PROJECT CARDS
# --------------------------------------------------

for project in projects:

    with st.container(border=True):

        # Project title
        st.subheader(project["title"])

        # Description
        st.write(project["description"])

        # Technologies
        st.markdown("**Technologies**")

        tech_text = " • ".join(project["tech"])

        st.caption(tech_text)

        # Buttons
        buttons = []

        if project["github"]:
            buttons.append(("💻 GitHub", project["github"]))

        if project["demo"]:
            buttons.append(("🚀 Live Demo", project["demo"]))

        if buttons:

            columns = st.columns(len(buttons))

            for column, (label, url) in zip(columns, buttons):

                with column:
                    st.link_button(
                        label,
                        url,
                        use_container_width=True
                    )

    st.write("")