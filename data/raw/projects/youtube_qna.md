# 🎥 YouTube Q&A Chatbot

An AI-powered YouTube Q&A chatbot that lets users load a YouTube video's transcript and ask questions about its content. The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant transcript sections before generating answers with an LLM.

## 🚀 Live Demo

**Streamlit App:** Add your deployed Streamlit URL here
Demo link = https://youtube-qna-chatbotgit.streamlit.app/
> **Note:** YouTube may block transcript requests from cloud-hosted IP addresses. If transcript retrieval fails on Streamlit Cloud, run the application locally.

---

## ✨ Features

* 🎥 Load transcripts directly from YouTube videos
* ✂️ Recursive text chunking for better retrieval
* 🧠 Hugging Face embeddings using `BAAI/bge-small-en-v1.5`
* 🔎 Semantic similarity search
* 💬 Conversational Q&A over video content
* 🧾 Chat history maintained during the session
* 🤖 LLM-powered responses
* 🌐 Streamlit web interface
* 🔐 API keys managed securely using environment variables and Streamlit Secrets

---

## 🏗️ Architecture

```text
YouTube Video URL
        │
        ▼
YouTube Transcript
        │
        ▼
Text Chunking
        │
        ▼
Hugging Face Embeddings
        │
        ▼
Vector Store
        │
        ▼
Similarity Retrieval
        │
        ▼
Relevant Context
        │
        ▼
LLM
        │
        ▼
Answer
        │
        ▼
Streamlit Chat Interface
```

---

## 🛠️ Tech Stack

| Technology             | Purpose                       |
| ---------------------- | ----------------------------- |
| Python                 | Core development              |
| Streamlit              | Web UI                        |
| LangChain              | RAG pipeline                  |
| YouTube Transcript API | Transcript extraction         |
| Hugging Face           | Text embeddings               |
| BGE-small-en-v1.5      | Embedding model               |
| Vector Store           | Semantic retrieval            |
| Gemini / OpenAI        | LLM-based response generation |

---

## 📂 Project Structure

```text
YouTube-QnA-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

> `.env` should never be committed to GitHub.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/PrashantKumar9889/youtube-qna-chatbot.git
```

### 2. Navigate to the project

```bash
cd youtube-qna-chatbot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY="your_google_api_key"
```

If using OpenAI:

```env
OPENAI_API_KEY="your_openai_api_key"
```

Never upload `.env` to GitHub.

Make sure `.gitignore` contains:

```text
.env
.venv/
__pycache__/
```

---

## ▶️ Run Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

Enter a YouTube URL, load the video transcript, and start asking questions.

---

## ☁️ Streamlit Deployment

The application can be deployed using **Streamlit Community Cloud**.

1. Push the project to GitHub.
2. Connect the repository to Streamlit Community Cloud.
3. Select `app.py` as the main file.
4. Add your API key under Streamlit **Secrets**.

Example:

```toml
GOOGLE_API_KEY = "your_google_api_key"
```

---

## ⚠️ YouTube Transcript Limitation

YouTube may block transcript requests originating from cloud-provider IP addresses.

As a result, transcript retrieval may work locally but fail after deployment on Streamlit Cloud.

This is a limitation of the transcript retrieval layer rather than the RAG pipeline.

---

## 🧠 RAG Workflow

The chatbot follows a Retrieval-Augmented Generation workflow:

### 1. Transcript Extraction

The YouTube video's transcript is retrieved using `youtube-transcript-api`.

### 2. Chunking

The transcript is divided into smaller chunks using:

```python
RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
```

### 3. Embeddings

Each chunk is converted into a vector representation using:

```text
BAAI/bge-small-en-v1.5
```

### 4. Retrieval

When the user asks a question, the application searches the vector store for the most relevant transcript chunks.

### 5. Generation

The retrieved context is provided to the LLM, which generates an answer based on the video content.

---

## 💬 Example

**User:**

```text
What is the main idea of this video?
```

**Chatbot:**

```text
The main idea of the video is...
```

The chatbot answers using information retrieved from the video's transcript.

---

## 🔒 Security

API keys are never hardcoded into the application.

For local development:

```text
.env
```

For Streamlit Cloud:

```text
Streamlit Secrets
```

The `.env` file is excluded through `.gitignore`.

---

## 🚧 Future Improvements

* Support videos without available transcripts
* Improve multilingual transcript support
* Add persistent vector databases
* Add source/citation references for answers
* Improve conversational memory
* Add transcript download functionality
* Add support for multiple YouTube videos
* Add authentication
* Improve cloud deployment reliability

---

## 👨‍💻 Author

**Prashant Kumar**

AI / Data Engineering | RAG | LLM Applications | LangChain | Python

GitHub:
https://github.com/PrashantKumar9889

---

## ⭐ If you find this project useful

Give the repository a ⭐ on GitHub.

