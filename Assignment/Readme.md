# Assignment: Convert RAG Chatbot from Streamlit to FastAPI + React

## Hey Students!

You've already learned about **Generative AI**, **RAG (Retrieval-Augmented Generation)**, **FastAPI**, and **React** along with tools like Streamlit and Gradio. Now it's time to put it all together in one real project.

You've seen the **Q&A Virtual Advisor** app built with Streamlit — it reads a PDF document, breaks it into chunks, stores them as vectors, and answers questions based only on that document using a local LLM (LLaMA 3.2 via Ollama).

**Your job?** Take that working Streamlit app and rebuild it as a proper full-stack application with **FastAPI** as the backend and **React** as the frontend.

---

## What You Already Have (The Existing App)

The original Streamlit app lives here:
**[GitHub - Q & A with reference doc](https://github.com/SyedAdnanAli13143/6th-Semester-Aptech/tree/main/AI%20Engineering/RAG/Q%20%26%20A%20with%20reference%20doc)**

It's a single `app.py` file that does everything:

- Reads a PDF file (`CT-Returns-EN-11-11-2024.pdf`) using **PyPDF2**
- Splits the text into smaller chunks using **LangChain's RecursiveCharacterTextSplitter**
- Converts those chunks into vector embeddings using **HuggingFace's all-MiniLM-L12-v2** model
- Stores and searches those vectors using **FAISS** (Facebook AI Similarity Search)
- Sends the relevant chunks + user question to **Ollama's LLaMA 3.2** model to generate an answer
- Shows everything in a **Streamlit** chat interface

The problem with this? Everything is mixed together — the AI logic, the data processing, and the UI are all in one file. In the real world, we separate concerns. That's what you'll do here.

---

## What You Need to Build

### Backend (FastAPI)

Create a FastAPI server that handles all the heavy lifting:

1. **PDF Upload Endpoint** — Let users upload a PDF file through the API (not hardcoded)
2. **Processing Logic** — When a PDF is uploaded, extract text, chunk it, and create the FAISS vector store (same logic as the Streamlit app, just moved to the backend)
3. **Question-Answer Endpoint** — Accept a user's question, search the vector store for relevant chunks, send them to Ollama/LLaMA, and return the answer
4. **Chat History Endpoint** — Store and return conversation history so the frontend can display it
5. **CORS Setup** — Enable CORS so your React frontend can talk to the backend

Your FastAPI backend should have at least these routes:

| Method | Route | What it does |
|--------|-------|-------------|
| POST | `/upload` | Upload a PDF document |
| POST | `/ask` | Ask a question about the uploaded document |
| GET | `/history` | Get the chat conversation history |
| DELETE | `/history` | Clear the conversation history |

### Frontend (React)

Build a clean React frontend that:

1. **File Upload Section** — A button/area to upload a PDF file to the backend
2. **Chat Interface** — A chat window where the user types questions and sees answers (like ChatGPT's interface)
3. **Loading States** — Show a spinner or "Thinking..." message while waiting for the AI response
4. **Chat History** — Display the full conversation (questions and answers)
5. **Clear Chat Button** — Let users start a fresh conversation
6. **Upload Status** — Show whether a document is currently loaded and ready for questions

You can use any React UI library you like — Material UI, Tailwind CSS, Ant Design, plain CSS — your choice.

---

## Step-by-Step Guide (How to Approach This)

Don't try to build everything at once. Follow these steps:

### Step 1: Understand the Existing Code

- Clone the original repo and run the Streamlit app locally
- Read through `app.py` line by line
- Make sure Ollama is installed and the LLaMA 3.2 model is pulled (`ollama pull llama3.2`)
- Ask the app a few questions to see how it works

### Step 2: Set Up Your Project Structure

Create a folder structure like this:

```
your-project/
├── backend/
│   ├── main.py              # FastAPI app entry point
│   ├── rag_engine.py         # All the RAG logic (chunking, embeddings, search, LLM calls)
│   ├── requirements.txt      # Python dependencies
│   └── uploads/              # Folder to store uploaded PDFs
├── frontend/
│   ├── src/
│   │   ├── App.jsx           # Main React component
│   │   ├── components/
│   │   │   ├── ChatWindow.jsx
│   │   │   ├── FileUpload.jsx
│   │   │   └── MessageBubble.jsx
│   │   └── ...
│   ├── package.json
│   └── ...
└── README.md
```

### Step 3: Build the Backend First

1. Move the RAG logic (PDF reading, chunking, embeddings, FAISS, Ollama calls) into `rag_engine.py`
2. Create FastAPI routes in `main.py` that use the functions from `rag_engine.py`
3. Test your API using **Swagger UI** (FastAPI gives you this for free at `http://localhost:8000/docs`)
4. Make sure `/upload` and `/ask` work correctly before touching the frontend

### Step 4: Build the React Frontend

1. Create a new React app (`npx create-react-app frontend` or use Vite: `npm create vite@latest frontend`)
2. Build the file upload component first
3. Build the chat interface
4. Connect everything to your FastAPI backend using `fetch` or `axios`

### Step 5: Test the Full Flow

1. Start the backend: `uvicorn main:app --reload`
2. Start the frontend: `npm start` or `npm run dev`
3. Upload a PDF → Ask questions → Get answers
4. Make sure error cases are handled (no PDF uploaded yet, empty question, etc.)

---

## Requirements & Dependencies

### Backend (Python)

```
fastapi
uvicorn
python-multipart
PyPDF2
langchain
langchain-community
langchain-huggingface
faiss-cpu
sentence-transformers
requests
```

### Frontend (Node.js)

```
react
axios (or use built-in fetch)
Any UI library of your choice (optional)
```

### You Also Need

- **Ollama** installed on your machine — [Download Ollama](https://ollama.com)
- Run `ollama pull llama3.2` to download the LLaMA 3.2 model
- **Python 3.9+**
- **Node.js 18+**

---

## Submission Guidelines

1. Push your complete project to a **GitHub repository**
2. Your repo must have a clear README with setup instructions (how to run your project)
3. Include screenshots of your working app
4. Make sure the app actually runs — I will clone and test it

---

## Grading Criteria

| Criteria | Marks |
|----------|-------|
| FastAPI backend works correctly (upload + ask endpoints) | 30 |
| React frontend is functional and clean | 25 |
| RAG pipeline works properly (correct answers from document) | 20 |
| Code organization and project structure | 10 |
| Error handling and user experience | 10 |
| README and documentation | 5 |
| **Total** | **100** |

---

## Tips from Your Instructor

- **Don't panic.** You already know all the pieces — this assignment is about connecting them together.
- **Backend first, frontend second.** Always make sure your API works before building the UI.
- **Use Swagger UI** (`/docs`) — it's your best friend for testing the backend without a frontend.
- **Google is your friend.** If you're stuck on "how to upload a file in FastAPI" or "how to make a POST request in React", search it. That's what real developers do.
- **Keep it simple.** A working simple app beats a broken fancy one. Get the basics right first, then add polish.
- **Ask questions.** If something is unclear, ask before you waste hours going in the wrong direction.

---

---

# Key Concepts & Definitions You Should Know

Before you start building, make sure you understand these foundational concepts. These are not just textbook definitions — I'm explaining them the way you'll actually encounter them in your work.

---

## Artificial Intelligence (AI)

Artificial Intelligence is the broad field of making machines do things that would normally require human intelligence — things like understanding language, recognizing images, making decisions, and learning from experience. It's the umbrella term. Everything else below falls under AI in some way.

Think of it this way: if a machine can look at a problem, figure out what to do, and take action without someone explicitly programming every single step — that's AI in action.

AI has been around as a concept since the 1950s, but it's only in the last decade that we've had enough data and computing power to make it truly useful.

---

## Machine Learning (ML)

Machine Learning is a subset of AI. Instead of writing rules by hand ("if temperature > 100, then alert"), you give the machine a bunch of data and let it figure out the patterns on its own.

For example, you show it 10,000 emails labeled as "spam" or "not spam," and the ML algorithm learns what makes an email spammy — without you ever writing a single rule about the word "FREE" or "CLICK HERE."

There are three main types:
- **Supervised Learning** — You give it labeled data (input + correct answer). Example: predicting house prices.
- **Unsupervised Learning** — You give it data without labels and it finds patterns. Example: customer segmentation.
- **Reinforcement Learning** — The model learns by trial and error, getting rewards for good actions. Example: training a robot to walk.

---

## Deep Learning (DL)

Deep Learning is a subset of Machine Learning that uses **neural networks with many layers** (that's what "deep" refers to — the depth of the network). While traditional ML might use algorithms like decision trees or linear regression, Deep Learning uses layers upon layers of connected nodes (neurons) that gradually learn more complex features.

Why does it matter? Deep Learning is what made breakthroughs possible in image recognition, speech recognition, language translation, and generative AI. Traditional ML struggles with raw images or text, but Deep Learning eats that stuff for breakfast.

The catch? Deep Learning needs **a lot of data** and **a lot of computing power**. That's why it only became practical when GPUs became affordable and datasets became massive.

---

## Neural Networks

A Neural Network is the fundamental architecture behind Deep Learning. It's inspired by (but not identical to) how the human brain works — a network of connected nodes (neurons) organized in layers.

Here's the simple version:
- **Input Layer** — Takes in the data (pixels of an image, words of a sentence, numbers in a spreadsheet)
- **Hidden Layers** — These are where the magic happens. Each layer extracts increasingly complex features from the data. In an image, the first layer might detect edges, the next detects shapes, the next detects objects.
- **Output Layer** — Gives you the final result (this image is a cat, this email is spam, this sentence is positive)

Each connection between neurons has a **weight** — a number that gets adjusted during training. The process of adjusting these weights so the network gives correct answers is called **training** or **learning**.

Common types of neural networks:
- **CNN (Convolutional Neural Network)** — Great for images and visual data
- **RNN (Recurrent Neural Network)** — Designed for sequential data like text and time series
- **Transformer** — The architecture behind GPT, LLaMA, and most modern language models. It uses "attention" to process all parts of the input at once instead of one at a time.

---

## Natural Language Processing (NLP)

NLP is the branch of AI that deals with **human language** — teaching machines to read, understand, and generate text (and sometimes speech).

Every time you use Google Translate, talk to Siri, or get autocomplete suggestions while typing — that's NLP at work.

Key tasks in NLP include:
- **Text Classification** — Is this review positive or negative?
- **Named Entity Recognition (NER)** — Find all the person names, company names, and dates in this document
- **Machine Translation** — Convert English to Urdu
- **Text Summarization** — Give me a 3-sentence summary of this long article
- **Question Answering** — Given a paragraph, answer this specific question
- **Text Generation** — Write the next paragraph, complete this sentence

Modern NLP is dominated by **Transformer-based models** (like GPT, BERT, and LLaMA). Before transformers, NLP was painful — we had to manually engineer features and deal with limited context. Now, these large language models can understand and generate text at near-human levels.

Your RAG assignment is fundamentally an NLP task — the model is reading a document and answering questions about it in natural language.

---

## Generative AI

Generative AI refers to AI models that can **create new content** — text, images, code, music, video. Unlike traditional AI that classifies or predicts, generative AI actually produces something new.

Examples you already know:
- **ChatGPT / Claude** — Generate text, answer questions, write code
- **DALL-E / Midjourney** — Generate images from text descriptions
- **GitHub Copilot** — Generate code as you type
- **Suno** — Generate music

Most modern generative AI is built on **Large Language Models (LLMs)** for text and **Diffusion Models** for images. The "large" in LLM refers to the massive number of parameters (weights) in the model — GPT-4 has hundreds of billions of parameters, all trained on enormous amounts of internet text.

The LLM you're using in your assignment — **LLaMA 3.2** — is an open-source generative AI model by Meta. It generates answers to your questions by predicting the most likely next words based on the context you give it.

---

## RAG (Retrieval-Augmented Generation)

This is the core concept of your assignment, so pay extra attention.

**The Problem:** LLMs like ChatGPT or LLaMA are trained on general internet data. They don't know about your company's internal documents, your personal files, or any data that wasn't in their training set. If you ask them about your specific tax document, they'll either make stuff up (hallucinate) or say "I don't know."

**The Solution:** RAG. Instead of retraining the entire model (which is expensive and slow), you **retrieve** relevant information from your own documents and **feed it to the model** along with the question. The model then generates an answer based on that specific context.

Here's how RAG works step by step (this is exactly what your app does):

1. **Load** — Read the PDF document
2. **Chunk** — Split the document into smaller pieces (because LLMs have limited context windows)
3. **Embed** — Convert each chunk into a vector (a list of numbers) using an embedding model. Similar text gets similar vectors.
4. **Store** — Save these vectors in a vector database (FAISS in your case)
5. **Retrieve** — When a user asks a question, convert the question into a vector too, then find the chunks whose vectors are most similar to the question's vector
6. **Generate** — Send those relevant chunks + the user's question to the LLM and let it generate a well-formed answer

Why is RAG so popular right now? Because it gives you the best of both worlds — the language ability of a powerful LLM combined with the accuracy of your own specific data. No hallucination (or at least much less), no expensive retraining.

---

## Computer Vision

Computer Vision is the field of AI that teaches machines to **see and understand images and videos**. Just like NLP is about text, Computer Vision is about visual data.

Tasks in Computer Vision include:
- **Image Classification** — Is this a photo of a cat or a dog?
- **Object Detection** — Where are the cars, pedestrians, and traffic signs in this image? (Used in self-driving cars)
- **Image Segmentation** — Outline every single object in the image pixel by pixel
- **Face Recognition** — Who is this person?
- **OCR (Optical Character Recognition)** — Read the text in this image

Computer Vision heavily relies on **CNNs (Convolutional Neural Networks)** and more recently **Vision Transformers (ViT)**. While it's not directly used in your RAG assignment, it's a major pillar of AI that you should understand.

---

## Agentic AI

Agentic AI is the newest and most exciting frontier. While regular chatbots just answer questions, **AI Agents can actually take actions** — they can browse the web, write and run code, call APIs, read files, make decisions, and chain multiple steps together to complete complex tasks.

Think of the difference like this:
- **Regular AI:** "Here's a recipe for pasta." (just gives information)
- **Agentic AI:** "I'll order the ingredients, set a timer, and walk you through each step as you cook." (takes action)

Key characteristics of Agentic AI:
- **Autonomy** — Can work independently toward a goal without constant human input
- **Tool Use** — Can use external tools (search engines, calculators, APIs, code interpreters)
- **Planning** — Can break down complex tasks into steps
- **Memory** — Can remember context from earlier in the conversation or even previous conversations
- **Reasoning** — Can think through problems step by step

Real-world examples: AI coding assistants that can edit your files, AI research agents that can browse the web and compile reports, customer service bots that can actually process refunds (not just tell you how).

The framework behind most AI agents? **LLMs + Tools + Memory + Planning Logic.** The LLM is the brain, the tools are the hands, memory is the notebook, and planning logic is the strategy.

---

## Embeddings & Vector Databases

Since your assignment uses these heavily, let's make sure you get them:

**Embeddings** are numerical representations of data (text, images, etc.) as vectors — lists of numbers like `[0.12, -0.34, 0.56, ...]`. The key property is that **similar things get similar vectors**. The sentence "How do I file taxes?" and "What's the process for tax filing?" would have vectors that are close to each other in vector space, even though the words are different.

**Vector Databases** (like FAISS, Pinecone, ChromaDB, Weaviate) are databases designed to store these vectors and quickly find the most similar ones. When you ask "What are the tax deadlines?", the system converts your question to a vector and searches the database for document chunks with the closest vectors. This is called **similarity search**.

In your app, you're using:
- **all-MiniLM-L12-v2** (HuggingFace) as the embedding model
- **FAISS** as the vector database

---

## LLM (Large Language Model)

A Large Language Model is a specific type of neural network (usually a Transformer) trained on massive amounts of text data. It learns the patterns, grammar, facts, and reasoning abilities encoded in that text.

How it works at the simplest level: you give it some text (a prompt), and it predicts the most likely next words, one token at a time. That's it. But because it's been trained on so much data with so many parameters, this simple mechanism produces remarkably intelligent-seeming output.

Popular LLMs:
- **GPT-4 / GPT-4o** (OpenAI) — Closed source, API access
- **Claude** (Anthropic) — Closed source, API access
- **LLaMA 3.2** (Meta) — Open source, can run locally via Ollama (this is what you're using)
- **Gemini** (Google) — Closed source, API access
- **Mistral** (Mistral AI) — Open source

---

## Prompt Engineering

Prompt Engineering is the skill of writing effective instructions (prompts) for AI models to get the best possible output. It's not just about asking a question — it's about asking the right way.

In your RAG app, the prompt sent to LLaMA looks something like:
> "Based on the following context from the document: [relevant chunks here]. Answer this question: [user's question]. Only answer based on the provided context."

That instruction to "only answer based on the provided context" is prompt engineering — it prevents the model from making stuff up.

---

## Hallucination

When an AI model confidently generates information that is **completely made up or incorrect**, that's called a hallucination. The model isn't lying on purpose — it's just predicting probable-sounding text that happens to be wrong.

RAG was specifically designed to reduce hallucination by grounding the model's responses in actual source documents.

---

## How Everything Connects in Your Assignment

Here's the big picture of how all these concepts come together in what you're building:

```
User asks a question (NLP - understanding human language)
        ↓
Question gets converted to a vector (Embeddings)
        ↓
Similar document chunks are found (Vector Database - FAISS)
        ↓
Chunks + Question sent to LLaMA (LLM - Large Language Model)
        ↓
LLaMA generates an answer (Generative AI)
        ↓
Answer displayed to user (React Frontend ← FastAPI Backend)
```

This entire pipeline is **RAG** — and you're building it as a proper full-stack application. You already understand each piece. Now go connect them.

Good luck!
