# 🩺 Medical Assistant Chatbot (Non-Diagnostic)

A safe and intelligent **Medical Assistant Chatbot** that provides:
- 💊 Medicine information & safety guidance
- 🩺 Symptom checking (non-diagnostic)
- ⚠️ Clear medical disclaimers and safety guardrails

Built using **LLMs (Groq)**, **Streamlit**, and **Python**.

---
<h1 align="center">
  <a href="https://medical-assistant-chatbot-arnnab.streamlit.app/">👉Live Demo👍</a>
</h1>

## 🚀 Features

- Medicine usage, side effects, and precautions
- Non-diagnostic symptom checker
- Advises when to seek medical help
- Chat-style UI using Streamlit
- Secure API key handling via `.env`
- Works with Jupyter Notebook and PyCharm

---

## 🛑 Medical Disclaimer

> This chatbot does **NOT** provide medical diagnosis or treatment.  
> It is intended for **educational and informational purposes only**.  
> Always consult a qualified healthcare professional for medical advice.

---

## 🧠 Tech Stack

- **Python 3.9+**
- **Groq LLM API**
- **Streamlit**
- **python-dotenv**
- **Jupyter Notebook (for experimentation)**

---

## 📂 Project Structure

```text
medical-assistant-chatbot/
├── app.py                  # Streamlit application
├── requirements.txt        # Dependencies
├── README.md               # Project documentation                
└── notebooks/              # API key (not committed)
    └── medical_chatbot.ipynb
