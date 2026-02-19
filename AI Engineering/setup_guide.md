# AI Excuse Generator - Setup Guide

## What is this?

A 10-line Python app that asks AI to generate a funny excuse for late assignments.

**You type:** `Machine Learning`
**AI replies:** _"Sorry professor, my cat sat on my laptop and accidentally deleted my ML assignment. She then looked me in the eye and meowed — I think she's trying to teach me unsupervised learning."_

---

## Setup (One Time Only)

### 1. Check Python is installed

```bash
python --version
```

If not installed: download from https://www.python.org/downloads/

### 2. Check Ollama is installed and running

```bash
ollama --version
```

If not installed: download from https://ollama.com/download

### 3. Download the AI model

```bash
ollama pull llama3.2
```

### 4. Create virtual environment and install library

```bash
cd "c:\Users\Adnan\Desktop\ML\AI 6th"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## Run the Apps

### App 1: Excuse Generator (simple one-shot)

```bash
venv\Scripts\activate
python excuse_generator.py
```

### App 2: Rishta Aunty Chatbot (conversational)

```bash
venv\Scripts\activate
python chatbot.py
```

---

## What is the difference between the two files?

| | excuse_generator.py | chatbot.py |
|---|---|---|
| **API** | `/api/generate` | `/api/chat` |
| **Model** | llama3.2 | llama3.2 |
| **Prompt type** | Only one prompt | System + User prompt |
| **Memory** | No (1 question = 1 answer) | Yes (remembers previous messages) |
| **Style** | One-shot (ask once, get answer) | Conversation (back and forth chat) |

---

## How excuse_generator.py works

```
  You type subject name
        |
        v
  Python builds a prompt (instruction for AI)
        |
        v
  Sends to Ollama /api/generate
        |
        v
  AI generates a funny excuse
        |
        v
  Python prints it on screen
```

## How chatbot.py works

```
  Set system prompt (AI personality)
        |
        v
  Get user message  <------|
        |                   |
        v                   |
  Send full chat history    |
  to Ollama /api/chat       |
        |                   |
        v                   |
  Print AI reply and        |
  save it to history  ------|
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `ConnectionError` | Open terminal, run `ollama serve` |
| `Model not found` | Run `ollama pull llama3.2` |
| `python not found` | Install Python and add to PATH |
