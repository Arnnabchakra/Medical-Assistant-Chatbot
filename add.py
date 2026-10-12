
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
- You are NOT a doctor.
- Do NOT diagnose medical conditions.
- Do NOT prescribe medicines.
- Provide general medical information only.
- Always include a safety disclaimer.
- Explain medicines and symptoms in simple language.
- Recommend professional medical care when appropriate.
"""

# ---------- API CONFIGURATION ----------
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    try:
        api_key = st.secrets.get("GROQ_API_KEY")
    except Exception:
        api_key = None

if not api_key:
    st.error(
        "Groq API key not found. "
        "Configure GROQ_API_KEY in your environment or Streamlit secrets."
    )
    st.stop()

client = Groq(api_key=api_key)


# ---------- CHATBOT FUNCTION ----------
def medical_chatbot(user_input):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


# ---------- UI ----------
st.title("🩺 Medical Assistant Chatbot")
st.caption("Medicine Information + Non-Diagnostic Symptom Guidance")

st.warning(
    "⚠️ This chatbot does not provide medical diagnoses "
    "or replace a healthcare professional. "
    "Seek urgent medical care for emergency symptoms."
)

# ---------- CHAT HISTORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- USER INPUT ----------
user_input = st.chat_input(
    "Ask about a medicine or describe your symptoms..."
)

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = medical_chatbot(user_input)
                st.markdown(response)

                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )

            except Exception:
                st.error(
                    "Sorry, the chatbot could not generate a response. "
                    "Please check your API configuration and app logs."
                )
