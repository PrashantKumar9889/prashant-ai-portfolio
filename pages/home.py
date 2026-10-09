import streamlit as st
from backend.api_client import get_profile
from backend.routes import profile

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

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    .hero {
        padding: 50px 10px 30px 10px;
    }

    .hero-title {
        font-size: 52px;
        font-weight: 700;
        line-height: 1.1;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 24px;
        font-weight: 500;
        margin-bottom: 20px;
    }

    .hero-description {
        font-size: 18px;
        line-height: 1.7;
        max-width: 850px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>

    .profile-pic {
        width: 220px;
        height: 220px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #ffffff;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

col1, col2 = st.columns([3, 1])

with col1:
    profile = get_profile()

    st.markdown(f"# {profile['name']}")

    st.markdown(
        f"### {profile['title']}"
    )

    st.write(profile['description'])

with col2:

    st.image(
        "assets/profile.jpg",
        width=220
    )

# --------------------------------------------------
# CORE SKILLS
# --------------------------------------------------

import json

st.divider()

st.subheader("Core AI Engineering Skills")

with open("data/skills.json", "r", encoding="utf-8") as file:
    skills_data = json.load(file)

skills = skills_data["skills"]

cols = st.columns(10)

for index, skill in enumerate(skills):
    with cols[index % 10]:
        st.markdown(f"**{skill}**")


# --------------------------------------------------
# FEATURED PROJECTS
# --------------------------------------------------

import json

st.divider()

st.subheader("Featured Projects")

with open("data/projects.json", "r", encoding="utf-8") as file:
    projects_data = json.load(file)

projects = projects_data["projects"]

for i in range(0, len(projects), 2):

    col1, col2 = st.columns(2)

    with col1:

        project = projects[i]

        with st.container(border=True):

            st.markdown(f"### {project['title']}")

            st.write(project["description"])

            st.caption(
                " • ".join(project["tech"])
            )

            if project["github"]:
                st.link_button(
                    "💻 GitHub",
                    project["github"]
                )

            if project["demo"]:
                st.link_button(
                    "🚀 Live Demo",
                    project["demo"]
                )

    if i + 1 < len(projects):

        with col2:

            project = projects[i + 1]

            with st.container(border=True):

                st.markdown(f"### {project['title']}")

                st.write(project["description"])

                st.caption(
                    " • ".join(project["tech"])
                )

                if project["github"]:
                    st.link_button(
                        "💻 GitHub",
                        project["github"]
                    )

                if project["demo"]:
                    st.link_button(
                        "🚀 Live Demo",
                        project["demo"]
                    )

                    
# --------------------------------------------------
# QUICK LINKS
# --------------------------------------------------

st.divider()

st.subheader("Connect With Me")

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button(
        "💻 GitHub",
        "https://github.com/PrashantKumar9889",
        use_container_width=True
    )

with col2:
    st.link_button(
        "🔗 LinkedIn",
        "https://www.linkedin.com/in/prashant-kumar-64101b304/",
        use_container_width=True
    )

with col3:
    st.link_button(
        "📄 Download Resume",
        "https://drive.google.com/file/d/19icStjX0YwGibc9RfUZler6YHwa6ygpD/view?usp=sharing",
        use_container_width=True
    )

# --------------------------------------------------
# TEST
# --------------------------------------------------

st.divider()

st.write("Portfolio is running successfully.")