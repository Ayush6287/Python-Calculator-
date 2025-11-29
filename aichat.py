import streamlit as st
from openai import OpenAI

st.title("OpenAI Chat App")

# Initialize OpenAI client with secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set default model
if "openai_model" not in st.session_state:
    st.session_state.openai_model = "gpt-4o-mini"  # Or "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]
