import streamlit as st

st.title("Experience")
st.caption("Professional Experience · Enterprise GenAI · Data Engineering")

# Company and role
st.subheader("Delphi Consulting Middle East")
st.caption("Dubai, UAE · Remote Internship · May 2025 – November 2025")

with st.container(border=True):
    st.markdown("### Data Functional Associate & Product Ownership")
    st.markdown(
        """
        **Duration:** 6 Months  
        **Work Areas:** Functional Analysis · Product Ownership Support · GenAI · Data Migration
        """
    )

    st.markdown("#### Company Overview")
    st.write(
        "Delphi Consulting Middle East is a consulting organization based in "
        "Dubai, UAE. During this remote internship, I supported functional "
        "analysis, requirements documentation, data migration validation, "
        "and GenAI chatbot initiatives in collaboration with technical teams "
        "and business stakeholders."
    )

    st.markdown("#### Role & Responsibilities")
    st.markdown(
        """
        - Gathered and documented business and functional requirements.
        - Prepared Business Requirements Documents (BRDs), user stories,
          workflow specifications, and functional documentation.
        - Coordinated with developers, data engineers, and business
          stakeholders to clarify requirements and resolve functional issues.
        - Supported User Acceptance Testing (UAT), data validation,
          discrepancy analysis, and requirements verification.
        - Contributed to GenAI chatbot requirements, RAG workflows,
          prompt design, and Text-to-SQL validation.
        """
    )

# Project 1
st.divider()
st.markdown("### Project 1: DP World Genie Workspace Chatbot")
st.caption("GenAI · RAG · LLM · Text-to-SQL")

with st.container(border=True):
    st.markdown("#### Project Overview")
    st.write(
        "Supported functional requirements and testing for an LLM-powered "
        "Text-to-SQL chatbot designed to enable natural-language data queries "
        "and conversational analytical responses."
    )

    st.markdown("#### Responsibilities")
    st.markdown(
        """
        - Gathered and documented requirements for an LLM-powered Text-to-SQL chatbot.
        - Worked with stakeholders to define RAG workflows, knowledge retrieval
          requirements, and conversational flows.
        - Collaborated with developers on prompt design, document chunking,
          LangChain workflow requirements, and chatbot testing.
        - Validated AI-generated responses, SQL query outputs, user intents,
          and conversational accuracy during UAT.
        - Prepared BRDs, user stories, and functional documentation for
          GenAI features and enterprise chatbot integration.
        """
    )

    st.markdown("**Technologies:** LangChain · RAG · LLM · Text-to-SQL · SQL")

# Project 2
st.divider()
st.markdown("### Project 2: M42 RCM Data Migration")
st.caption("Healthcare Data · Revenue Cycle Management · Databricks → Microsoft Fabric")

with st.container(border=True):
    st.markdown("#### Project Overview")
    st.write(
        "Supported a healthcare data migration initiative for M42 involving "
        "Revenue Cycle Management (RCM) data transition from Databricks "
        "to Microsoft Fabric, including the Globis RCM migration."
    )

    st.markdown("#### Responsibilities")
    st.markdown(
        """
        - Supported RCM data migration and transformation activities.
        - Performed source-to-target validation using SQL and Excel to verify
          field mappings, transformation outputs, and business rules.
        - Conducted data quality checks covering completeness, accuracy,
          validity, consistency, and duplicate records.
        - Collaborated with data engineers and business teams to investigate
          discrepancies and maintain data integrity.
        - Validated business rules and performed post-migration verification.
        - Contributed to migration requirements, validation scenarios,
          and data reconciliation documentation.
        """
    )

    st.markdown(
        "**Technologies:** Azure Databricks · Microsoft Fabric · SQL · Excel · Azure"
    )

# Tools
st.divider()
st.markdown("### Tools & Technologies")

tools = [
    "Microsoft Fabric",
    "Azure Databricks",
    "SQL",
    "Microsoft Excel",
    "Power BI",
    "Azure",
    "Microsoft Teams",
    "SharePoint",
    "LangChain",
    "RAG",
    "LLMs",
    "Text-to-SQL",
]

columns = st.columns(4)
for index, tool in enumerate(tools):
    with columns[index % 4]:
        st.markdown(f"- {tool}")