import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

from components.Chat_logic import get_response  # import your logic function

# === Load Gemini API key ===
load_dotenv("./env.txt")
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# === Instantiate Gemini Pro model ===
model = genai.GenerativeModel("gemini-2.5-flash")

# === Streamlit setup ===
st.set_page_config(page_title="HelioPal AI Chatbot", layout="centered")
st.title("🔆 HelioPal Chatbot")
st.markdown(
    '<h3 style="margin-bottom: 50px; color: #666; font-size: 20px;">Ask me about anything solar inverter systems — from sizing to simulation.</h3>',
    unsafe_allow_html=True
)


# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# === Process initial prompt from homepage if exists ===
if "user_input" in st.session_state and st.session_state["user_input"]:
    initial_prompt = st.session_state["user_input"]
    st.session_state.messages.append({"role": "user", "text": initial_prompt})

    # first_call=True because this is the first message in the conversation
    reply = get_response(model, st.session_state.messages, first_call=True)
    st.session_state.messages.append({"role": "assistant", "text": reply})

    st.session_state["user_input"] = ""  # Clear after processing

# Display chat messages from history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["text"])

# Single input box for all user queries at bottom
if prompt := st.chat_input("Type your question here..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "text": prompt})

    # first_call is True only if this is the very first message; else False
    first_call = len(st.session_state.messages) == 1
    reply = get_response(model, st.session_state.messages, first_call=first_call)

    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "text": reply})


# === GitHub Repo Link at the Bottom ===
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        background: transparent;
        font-size: 20px;
        z-index: 100;
    }
    .footer a {
        color: #ffffff;
        text-decoration: none;
    }
    .footer a:hover {
        color: #666;
    }
    </style>

    <div class="footer">
        <a href="https://github.com/Ola-doyin/Helio-AI-Chatbot.git" target="_blank">
            <i class="fab fa-github"></i> GitHub
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Font Awesome for GitHub icon
st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">',
    unsafe_allow_html=True
)
