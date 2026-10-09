
import requests
import streamlit as st
from backend.api_client import send_chat_message

st.title("🤖 AI Chat")
st.caption("Ask questions about my background, skills, and projects.")

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# Display previous messages.
for message in st.session_state.chat_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle a new question.
if prompt := st.chat_input("Ask me about my projects or experience..."):
    st.session_state.chat_messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching my portfolio and generating an answer..."):
            try:
                answer = send_chat_message(prompt)
                st.markdown(answer)

                st.session_state.chat_messages.append(
                    {"role": "assistant", "content": answer}
                )

            except requests.RequestException:
                st.error(
                    "Could not connect to the AI service. "
                    "Please check that the FastAPI backend is running."
                )
            except Exception as exc:
                st.error(f"Chatbot error: {exc}")