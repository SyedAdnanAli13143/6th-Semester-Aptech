# Step 1: Import library (to send requests to AI model)
import requests

# Step 2: Ask student for their subject name
subject = input("Enter your subject name: ")

# Step 3: Write a prompt (instruction for AI - this is called Prompt Engineering)
prompt = f"Write a short funny excuse for submitting {subject} assignment late. Make it 2 lines only."

# Step 4: Send prompt to Ollama AI running on our computer (localhost)
response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama3.2",   # AI model name (already downloaded in Ollama)
    "prompt": prompt,       # our instruction to AI
    "stream": False         # wait for full answer at once
})

# Step 5: Print the AI generated excuse
print("\nAI Generated Excuse:")
print(response.json()["response"])
