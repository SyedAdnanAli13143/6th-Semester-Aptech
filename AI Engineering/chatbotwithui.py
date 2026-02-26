# Step 1: Import libraries
import requests
import gradio as gr

# ============================================
# CHATBOT (Rishta Aunty)
# ============================================

# Step 2: System prompt - sets AI's personality (user never sees this)
system_prompt = "You are a dramatic Rishta Aunty from Pakistan. You judge everything - marks, salary, height, skin color. Always reply in English. Be funny and over-dramatic. Ask nosy questions. Keep answers short 2-3 lines max."

# Step 3: Chat function - sends messages to Ollama and gets reply
def chat_with_aunty(user_message, history):
    # Build chat history in Ollama's format
    chat_history = [{"role": "system", "content": system_prompt}]

    # Add previous messages from Gradio history (messages format)
    for msg in history:
        chat_history.append({"role": msg["role"], "content": msg["content"]})

    # Add current user message
    chat_history.append({"role": "user", "content": user_message})

    # Send to Ollama
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "llama3.2",
        "messages": chat_history,
        "stream": False
    })

    ai_reply = response.json()["message"]["content"]
    return ai_reply

# ============================================
# EXCUSE GENERATOR
# ============================================

# Step 4: Excuse function - generates a funny excuse for late assignment
def generate_excuse(subject):
    if not subject.strip():
        return "Please enter a subject name!"

    prompt = f"Write a short funny excuse for submitting {subject} assignment late. Make it 2 lines only."

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })

    return response.json()["response"]

# ============================================
# GRADIO UI
# ============================================

# Step 5: Build the Gradio interface with tabs
with gr.Blocks(title="AI Tools - Rishta Aunty & Excuse Generator") as app:
    gr.Markdown("# 🤖 AI Tools (Powered by Ollama + LLaMA 3.2)")

    # Tab 1: Rishta Aunty Chatbot
    with gr.Tab("Rishta Aunty Chatbot"):
        gr.Markdown("### Chat with the most dramatic Rishta Aunty from Pakistan!")
        chatbot = gr.ChatInterface(
            fn=chat_with_aunty,
            chatbot=gr.Chatbot(height=400),
            textbox=gr.Textbox(placeholder="Say something to Aunty...", container=False),
        )

    # Tab 2: Excuse Generator
    with gr.Tab("Excuse Generator"):
        gr.Markdown("### Generate a funny excuse for your late assignment!")
        with gr.Row():
            subject_input = gr.Textbox(label="Subject Name", placeholder="e.g. Machine Learning")
            excuse_output = gr.Textbox(label="AI Generated Excuse", lines=4)
        generate_btn = gr.Button("Generate Excuse", variant="primary")
        generate_btn.click(fn=generate_excuse, inputs=subject_input, outputs=excuse_output)

# Step 6: Launch the app
app.launch()
