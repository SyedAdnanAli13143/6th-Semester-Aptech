# Step 1: Import libraries
import streamlit as st
import requests

# Step 2: System prompt (sets AI's personality — user never sees this)
system_prompt = (
    "You are a dramatic Rishta Aunty from Pakistan. You judge everything - "
    "marks, salary, height, skin color. Always reply in English. "
    "Be funny and over-dramatic. Ask nosy questions. Keep answers short 2-3 lines max."
)

# Step 3: Sample prompts — quick-click buttons for the user to try
SAMPLE_PROMPTS = [
    "I just got a job at 80k salary",
    "I'm 25 and still not married",
    "My son got 900 marks in matric",
    "I want to marry for love, not rishta",
    "We live in a 2-bedroom flat",
]

# Step 4: Ollama API call function
def get_ai_response(messages, model="llama3.2"):
    """Send chat history to Ollama and return AI reply."""
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": model, "messages": messages, "stream": False},
            timeout=60,
        )
        response.raise_for_status()
        return response.json()["message"]["content"]
    except requests.ConnectionError:
        return "Ollama is not running! Start it first on localhost:11434."
    except Exception as e:
        return f"Error: {e}"

# Step 5: Page config
st.set_page_config(page_title="Rishta Aunty Bot", page_icon="👵", layout="centered")

# Step 6: Sidebar
with st.sidebar:
    st.title("👵 Rishta Aunty Bot")
    st.markdown("---")
    model_name = st.text_input("Ollama Model", value="llama3.2")
    st.markdown("---")

    if st.button("🗑️  Clear Chat", use_container_width=True):
        st.session_state.pop("chat_history", None)
        st.rerun()

    st.markdown("---")
    st.caption("Powered by Ollama (local LLM)")

# Step 7: Initialize chat history with system prompt + welcome message
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": "Assalam-o-Alaikum beta! Aunty has heard you're looking for rishta. Tell me EVERYTHING — salary, height, family background. Jaldi bolo!"},
    ]

# Step 8: Header
st.header("👵 Rishta Aunty Bot")

# Step 9: Display chat messages (skip system message)
for msg in st.session_state.chat_history:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Step 10: Sample prompt buttons (shown only at start of conversation)
user_message = None
if len(st.session_state.chat_history) <= 2:
    st.markdown("**Try a sample prompt:**")
    cols = st.columns(len(SAMPLE_PROMPTS))
    for i, prompt in enumerate(SAMPLE_PROMPTS):
        with cols[i]:
            if st.button(prompt, key=f"sample_{i}", use_container_width=True):
                user_message = prompt

# Step 11: Chat input box
chat_input = st.chat_input(placeholder="e.g. My beta earns 2 lakh per month...")
if chat_input:
    user_message = chat_input

# Step 12: Process user message (from button or text input)
if user_message:
    # Add user message to history and display
    st.session_state.chat_history.append({"role": "user", "content": user_message})
    with st.chat_message("user"):
        st.markdown(user_message)

    # Get AI response and display
    with st.chat_message("assistant"):
        with st.spinner("Aunty is judging..."):
            ai_reply = get_ai_response(st.session_state.chat_history, model=model_name)
        st.markdown(ai_reply)

    # Save to history
    st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})
