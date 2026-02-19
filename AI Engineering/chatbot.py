# Step 1: Import library (to send requests to AI model)
import requests

# Step 2: Write system prompt (this sets AI's personality, user never sees this)
# System prompt = tells AI WHO it is and HOW to behave
system_prompt = "You are a dramatic Rishta Aunty from Pakistan. You judge everything - marks, salary, height, skin color. Always reply in English. Be funny and over-dramatic. Ask nosy questions. Keep answers short 2-3 lines max."

# Step 3: Create chat history (so AI remembers previous messages)
# Each message has a role: "system", "user", or "assistant"
chat_history = [
    {"role": "system", "content": system_prompt}  # system prompt goes first
]

print("Rishta Aunty Bot (type 'exit' to quit)\n")

# Step 4: Run a loop so user can chat back and forth (conversation)
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Step 5: Add user's message to chat history
    chat_history.append({"role": "user", "content": user_input})

    # Step 6: Send full chat history to Ollama (this gives AI context)
    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "llama3.2",         # AI model name
        "messages": chat_history,    # send full conversation
        "stream": False              # get complete answer at once
    })

    # Step 7: Extract AI's reply and print it
    ai_reply = response.json()["message"]["content"]
    print(f"Aunty: {ai_reply}\n")

    # Step 8: Save AI's reply to history (so next answer has full context)
    chat_history.append({"role": "assistant", "content": ai_reply})
