
import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖"
)

st.title("AI Assistant")
st.caption("Powered by LangGraph and Gemini/Groq")


# Maintain conversation history in the UI
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Input box
question = st.chat_input("Ask something...")


if question:

    # Show user question
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    # Call FastAPI
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    f"{API_URL}/chat",
                    json={"question": question},
                    timeout=90
                )

                response.raise_for_status()

                answer = response.json()["answer"]

                st.write(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except requests.RequestException as error:

                st.error(f"API error: {error}")
