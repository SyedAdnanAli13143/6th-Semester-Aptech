# =============================================================================
# Virtual Advisor - Tax Document Q&A Chatbot
# =============================================================================
# A Streamlit chatbot that uses RAG (Retrieval-Augmented Generation) to answer
# questions about a tax PDF document. It runs entirely locally using Ollama
# with the LLaMA 3.2 model — no API keys or cloud services needed.
#
# Flow:
#   1. On startup, the PDF is read and split into text chunks.
#   2. Chunks are embedded using HuggingFace and stored in a FAISS vector store.
#   3. When the user asks a question, the most relevant chunks are retrieved.
#   4. The retrieved context + question are sent to LLaMA 3.2 via Ollama.
#   5. The AI response is displayed in the chat interface.
# =============================================================================

# Step 1: Import required libraries
import streamlit as st          # Web UI framework
import requests                 # HTTP client for Ollama API
import os                       # File path handling
from PyPDF2 import PdfReader    # PDF text extraction
from langchain_text_splitters import RecursiveCharacterTextSplitter  # Text chunking
from langchain_community.vectorstores import FAISS                  # Vector database
from langchain_huggingface import HuggingFaceEmbeddings             # Text embeddings

# =============================================================================
# Step 2: PDF Processing Functions
# =============================================================================

def extract_pdf_text(pdf_path):
    """
    Read a PDF file and extract all text from every page.
    Returns the combined text as a single string.
    """
    text = ""
    for page in PdfReader(pdf_path).pages:
        text += page.extract_text()
    return text


def build_vectorstore(text):
    """
    Convert raw text into a searchable FAISS vector store.

    Process:
      1. Split the text into overlapping chunks (2500 chars each, 350 overlap)
         so that no important info is lost at chunk boundaries.
      2. Generate embeddings for each chunk using a HuggingFace model.
      3. Store the embeddings in a FAISS index for fast similarity search.
    """
    # Split text into manageable chunks with overlap to preserve context
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=2500,      # Max characters per chunk
        chunk_overlap=350     # Overlap between consecutive chunks
    ).split_text(text)

    # Load the embedding model (runs locally, no API key needed)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L12-v2",
        model_kwargs={"trust_remote_code": True},
    )

    # Build and return the FAISS vector store from the text chunks
    return FAISS.from_texts(chunks, embeddings)

# =============================================================================
# Step 3: Ollama LLM Integration
# =============================================================================

def get_ai_response(messages, model="llama3.2"):
    """
    Send a list of chat messages to the Ollama API and return the AI's reply.

    Args:
        messages: List of dicts with 'role' and 'content' keys
                  (e.g., [{"role": "system", "content": "..."}, ...])
        model:    The Ollama model to use (default: llama3.2)

    Returns:
        The AI-generated response text, or an error message if something fails.
    """
    try:
        # POST request to Ollama's local chat API
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": model, "messages": messages, "stream": False},
            timeout=120,  # 2-minute timeout for slower machines
        )
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()["message"]["content"]
    except requests.ConnectionError:
        # Ollama server is not running
        return "Ollama is not running! Start it first on localhost:11434."
    except Exception as e:
        return f"Error: {e}"

# =============================================================================
# Step 4: App Configuration
# =============================================================================

# System prompt defines the AI's personality and behavior
SYSTEM_PROMPT = (
    "You are a helpful virtual tax advisor. Answer the user's question based on the "
    "provided context from the tax document. If the answer is not in the context, "
    "say you don't know. Keep answers concise and clear."
)

# PDF file to load (must be in the same directory as this script)
PDF_FILE = "CT-Returns-EN-11-11-2024.pdf"

# =============================================================================
# Step 5: Streamlit Page Setup
# =============================================================================

# Configure the browser tab title, icon, and layout
st.set_page_config(page_title="Virtual Advisor", page_icon="📄", layout="wide")

# Sidebar with app title and clear chat button
with st.sidebar:
    st.title("📄 Virtual Advisor")
    st.markdown("---")

    # Clear chat button — removes history and forces a page reload
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.pop("chat_history", None)
        st.rerun()

    st.markdown("---")
    st.caption("Powered by Ollama + LLaMA 3.2 (local)")

# =============================================================================
# Step 6: Load and Index the PDF Document (runs once on first visit)
# =============================================================================

if "vectorstore" not in st.session_state:
    # Resolve the PDF path relative to this script's location
    base_dir = os.path.dirname(__file__)
    pdf_path = os.path.join(base_dir, PDF_FILE)

    # Stop the app if the PDF file is missing
    if not os.path.exists(pdf_path):
        st.error(f"PDF not found: {pdf_path}")
        st.stop()

    # Extract text from PDF, chunk it, and build the vector store
    with st.spinner("Loading document..."):
        raw_text = extract_pdf_text(pdf_path)
        st.session_state.vectorstore = build_vectorstore(raw_text)

# =============================================================================
# Step 7: Initialize Chat History
# =============================================================================

# On first load, seed the chat with the system prompt and a welcome message
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Hello! I'm your Virtual Tax Advisor. Ask me anything about your tax document."},
    ]

# =============================================================================
# Step 8: Display Chat Messages
# =============================================================================

st.header("📄 Virtual Advisor")

# Render all messages from history (skip the hidden system prompt)
for msg in st.session_state.chat_history:
    if msg["role"] == "system":
        continue
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =============================================================================
# Step 9: Handle User Input and Generate AI Response
# =============================================================================

# Show the chat input box at the bottom of the page
if user_input := st.chat_input("Ask any question about your tax document..."):

    # Add user message to history and display it immediately
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Retrieve the top 3 most relevant chunks from the vector store
    retriever = st.session_state.vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    )
    context = retriever.invoke(user_input)

    # Build the augmented prompt: context from PDF + user's question
    augmented_prompt = (
        f"Context from document:\n{context}\n\n"
        f"User question: {user_input}"
    )

    # Prepare the message list for the LLM (system prompt + augmented user query)
    llm_messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": augmented_prompt},
    ]

    # Call Ollama and display the response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_reply = get_ai_response(llm_messages)
        st.markdown(ai_reply)

    # Save the assistant's reply to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})
