import streamlit as st
from groq import Groq
import os

# ---------- CONFIG ----------
st.set_page_config(
    page_title="Medical Assistant Chatbot",
    page_icon="🩺"
)

SYSTEM_PROMPT = """
You are a Medical Assistant Chatbot.

RULES:
- You are NOT a doctor
- Do NOT diagnose
- Do NOT prescribe
- Provide general info only
- Always add a safety disclaimer

You can:
• Explain medicines
• Discuss symptoms (non-diagnostic)
• Suggest when to see a doctor
"""

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def medical_chatbot(user_input):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

# ---------- UI ----------
st.title("🩺 Medical Assistant Chatbot")
st.caption("Medicine Info + Symptom Checker (Non-Diagnostic)")

st.warning(
    "⚠️ This chatbot does NOT provide medical diagnosis. "
    "Always consult a qualified healthcare professional."
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Describe your symptoms or ask about a medicine...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = medical_chatbot(user_input)
            st.markdown(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
