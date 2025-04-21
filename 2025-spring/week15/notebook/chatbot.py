import streamlit as st
import openai
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv(), override=True)  # read local .env file
openai.api_key = os.environ["OPENAI_API_KEY"]


# Function to get response from OpenAI
def get_completion_from_messages(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.7
    )
    return response.choices[0].message["content"]


# Initialize session state
if "context" not in st.session_state:
    st.session_state.context = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title
st.title("💬 Streamlit Chatbot")
st.markdown("Ask me anything!")

# Text input
user_input = st.text_input("You:", key="input")

# Send button
if st.button("Send") and user_input.strip():
    # Add user message to context
    st.session_state.context.append({"role": "user", "content": user_input})

    # Get assistant response
    response = get_completion_from_messages(st.session_state.context)

    # Add assistant response to context
    st.session_state.context.append({"role": "assistant", "content": response})

    # Save to chat history for UI display
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Assistant", response))

# Display chat history
for role, message in st.session_state.chat_history:
    with st.chat_message(role.lower()):
        st.markdown(message)
