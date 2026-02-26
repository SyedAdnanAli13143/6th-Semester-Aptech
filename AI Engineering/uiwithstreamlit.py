# ============================================================
# Business Problem: Small startups can't afford separate AI tools
# for customer support, HR screening, and sales coaching.
# This single app gives them 3 AI assistants in one dashboard,
# powered by a local LLM (Ollama) — zero API cost!
# ============================================================

import streamlit as st
import requests

# ---------- Business Personas (System Prompts) ----------
PERSONAS = {
    "Customer Support Agent": {
        "emoji": "🎧",
        "prompt": (
            "You are a professional and friendly Customer Support Agent for 'ShopEasy', "
            "an online e-commerce store selling electronics and gadgets in Pakistan. "
            "Help customers with order tracking, returns, refunds, product questions, "
            "and complaints. Be polite, empathetic, and solution-oriented. "
            "If you don't know the order details, ask for the order ID. "
            "Keep responses concise (3-4 lines max)."
        ),
        "welcome": "Hello! Welcome to ShopEasy Support. How can I help you today?",
        "placeholder": "e.g. Where is my order #12345?",
        "samples": [
            "Where is my order #12345?",
            "I received a broken laptop, I want a refund",
            "Do you have iPhone 15 in stock?",
            "I want to cancel my order",
            "How long does delivery take to Lahore?",
        ],
    },
    "HR Recruiter": {
        "emoji": "👔",
        "prompt": (
            "You are an experienced HR Recruiter for a Pakistani tech startup called 'CodeBase'. "
            "You conduct initial screening interviews. Ask candidates about their experience, "
            "skills, salary expectations, and availability. Be professional yet warm. "
            "Evaluate answers and give brief feedback. Ask one question at a time. "
            "Keep responses concise (3-4 lines max)."
        ),
        "welcome": "Hi there! I'm from CodeBase HR. Let's start your screening — tell me about yourself!",
        "placeholder": "e.g. I have 3 years of Python experience...",
        "samples": [
            "I'm a fresh graduate from FAST with a CS degree",
            "I have 3 years of Python and Django experience",
            "My expected salary is 150k per month",
            "I can start immediately, no notice period",
            "I've built 5 full-stack projects on GitHub",
        ],
    },
    "Sales Pitch Coach": {
        "emoji": "🚀",
        "prompt": (
            "You are a sharp Sales Pitch Coach who helps startup founders practice their "
            "investor pitch. Act like a tough but fair investor from Shark Tank Pakistan. "
            "Ask hard questions about revenue, market size, competition, and traction. "
            "Give brutally honest feedback on their pitch. Rate pitches out of 10. "
            "Keep responses concise (3-4 lines max)."
        ),
        "welcome": "Alright founder, you've got 60 seconds — pitch me your startup!",
        "placeholder": "e.g. We're building an AI tool that...",
        "samples": [
            "We're building an AI tutor for Pakistani students, $5/month",
            "Our food delivery app has 10,000 users in Karachi already",
            "We need $50,000 for 10% equity in our SaaS startup",
            "Our competitor is Bykea but we focus on grocery delivery",
            "We've made 2 lakh revenue in our first 3 months",
        ],
    },
}

# ---------- Ollama API call ----------
def get_ai_response(messages: list, model: str = "llama3.2") -> str:
    """Send chat history to Ollama and return the AI reply."""
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": model, "messages": messages, "stream": False},
            timeout=60,
        )
        response.raise_for_status()
        return response.json()["message"]["content"]
    except requests.ConnectionError:
        return "Could not connect to Ollama. Make sure it is running on localhost:11434."
    except Exception as e:
        return f"Error: {e}"

# ---------- Page Config ----------
st.set_page_config(page_title="AI Business Assistant", page_icon="💼", layout="centered")

# ---------- Sidebar ----------
with st.sidebar:
    st.title("💼 AI Business Assistant")
    st.markdown("---")

    # Persona selector
    selected_persona = st.selectbox(
        "Choose your AI role:",
        list(PERSONAS.keys()),
        format_func=lambda x: f"{PERSONAS[x]['emoji']}  {x}",
    )

    # Model selector
    model_name = st.text_input("Ollama Model", value="llama3.2")

    st.markdown("---")

    # Clear chat button
    if st.button("🗑️  Clear Chat", use_container_width=True):
        st.session_state.pop("chat_history", None)
        st.session_state.pop("active_persona", None)
        st.rerun()

    st.markdown("---")
    st.caption("Powered by Ollama (local LLM)")
    st.caption("Business Problem: 3 AI assistants, 1 app, zero API cost")

# ---------- Detect persona switch ----------
persona_cfg = PERSONAS[selected_persona]

if "active_persona" not in st.session_state or st.session_state.active_persona != selected_persona:
    # Reset chat when persona changes
    st.session_state.active_persona = selected_persona
    st.session_state.chat_history = [
        {"role": "system", "content": persona_cfg["prompt"]},
        {"role": "assistant", "content": persona_cfg["welcome"]},
    ]

# ---------- Main Chat Area ----------
st.header(f"{persona_cfg['emoji']}  {selected_persona}")

# Display chat messages (skip system message)
for msg in st.session_state.chat_history:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- Sample Prompt Buttons (shown at start of conversation) ----------
user_input = None
if len(st.session_state.chat_history) <= 2:
    st.markdown("**Try a sample prompt:**")
    cols = st.columns(len(persona_cfg["samples"]))
    for i, sample in enumerate(persona_cfg["samples"]):
        with cols[i]:
            if st.button(sample, key=f"sample_{i}", use_container_width=True):
                user_input = sample

# ---------- User Input ----------
chat_input = st.chat_input(placeholder=persona_cfg["placeholder"])
if chat_input:
    user_input = chat_input

if user_input:
    # Show user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_reply = get_ai_response(st.session_state.chat_history, model=model_name)
        st.markdown(ai_reply)

    # Save AI reply to history
    st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})


#streamlit run chatbot.py