# 🚀 Prashant Kumar — AI Engineer Portfolio

A full-stack AI engineering portfolio built with **Streamlit and FastAPI**, designed to showcase my projects, technical skills, experience, and AI engineering work.

The portfolio itself demonstrates a practical frontend–backend architecture with REST APIs and cloud deployment.

## 🌐 Live Portfolio

**Portfolio:**
https://prashant-ai-portfoliogit-rej24k6hvpeqx4yqmlzuqm.streamlit.app/

**FastAPI Backend:**
https://prashant-ai-portfolio.onrender.com/

**API Documentation:**
https://prashant-ai-portfolio.onrender.com/docs

---

## ✨ Features

* 🏠 Personal portfolio homepage
* 👤 Profile and professional information
* 💻 Projects showcase
* 🧠 Technical skills
* 💼 Experience section
* 🤖 AI Chat section
* 📬 Contact section
* 🔌 REST API backend
* ☁️ Cloud deployment
* 📱 Responsive Streamlit interface
* 📊 Data-driven portfolio content using JSON
* 🔄 Streamlit frontend connected to FastAPI backend

---

## 🏗️ Architecture

```text
                    🌐 User
                       │
                       ▼
              ┌─────────────────┐
              │    Streamlit    │
              │    Frontend     │
              └────────┬────────┘
                       │
                       │ HTTPS / REST API
                       ▼
              ┌─────────────────┐
              │     FastAPI     │
              │     Backend     │
              └────────┬────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      /profile     /projects     /skills
          │            │            │
          ▼            ▼            ▼
    profile.json  projects.json  skills.json
```

The frontend communicates with the deployed FastAPI backend through HTTP requests.

---

## 🛠️ Tech Stack

### Frontend

* Python
* Streamlit
* HTML/CSS
* Streamlit Components

### Backend

* FastAPI
* Uvicorn
* REST APIs
* Pydantic

### Data

* JSON
* Python data handling

### Development

* Git
* GitHub
* Virtual Environment
* VS Code / PyCharm

### Deployment

* Streamlit Community Cloud
* Render

---

## 📁 Project Structure

```text
Portfolio Website/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── api_client.py
│   │
│   └── routes/
│       ├── __init__.py
│       ├── profile.py
│       ├── projects.py
│       └── skills.py
│
├── data/
│   ├── profile.json
│   ├── projects.json
│   └── skills.json
│
├── pages/
│   ├── home.py
│   ├── 1_Projects.py
│   ├── skills.py
│   ├── experience.py
│   ├── chatbot.py
│   └── contact.py
│
└── assets/
    └── profile.jpg
```

---

## 🔌 API Endpoints

The FastAPI backend currently exposes the following endpoints:

| Method | Endpoint        | Description                  |
| ------ | --------------- | ---------------------------- |
| GET    | `/api/health`   | API health check             |
| GET    | `/api/profile`  | Personal profile information |
| GET    | `/api/projects` | Portfolio projects           |
| GET    | `/api/skills`   | Technical skills             |

Interactive API documentation is available through FastAPI Swagger:

`/docs`

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/PrashantKumar9889/prashant-ai-portfolio.git
cd prashant-ai-portfolio
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start FastAPI

Open a terminal:

```bash
uvicorn backend.main:app --reload
```

FastAPI will run at:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### 5. Start Streamlit

Open another terminal:

```bash
streamlit run app.py
```

Streamlit will normally run at:

```text
http://localhost:8501
```

---

## 🔄 Frontend–Backend Communication

The Streamlit application communicates with FastAPI through:

```python
API_BASE_URL = "https://prashant-ai-portfolio.onrender.com/api"
```

For example:

```python
response = requests.get(
    f"{API_BASE_URL}/projects",
    timeout=10
)

response.raise_for_status()

projects = response.json()
```

This keeps portfolio data separate from the frontend presentation layer.

---

## ☁️ Deployment

### Streamlit

The frontend is deployed using **Streamlit Community Cloud**.

### FastAPI

The backend is deployed using **Render**.

Production architecture:

```text
Streamlit Cloud
      │
      │ HTTPS
      ▼
Render
      │
      ▼
FastAPI
      │
      ▼
JSON Data
```

---

## 🔐 Security

Sensitive configuration and credentials should not be committed to GitHub.

The project ignores:

```text
.env
.streamlit/secrets.toml
venv/
__pycache__/
*.pyc
```

API keys and other secrets should be stored using environment variables or Streamlit secrets rather than hard-coded in source code.

---

## 🚀 Roadmap

The portfolio is actively being developed.

### Completed

* [x] Streamlit portfolio
* [x] Multi-page navigation
* [x] Profile section
* [x] Projects section
* [x] Skills section
* [x] FastAPI backend
* [x] REST API endpoints
* [x] Streamlit → FastAPI integration
* [x] GitHub repository
* [x] FastAPI cloud deployment
* [x] Streamlit cloud deployment
* [x] Production API connection

### Planned

* [ ] Personal AI chatbot
* [ ] RAG-based portfolio knowledge base
* [ ] Resume Q&A
* [ ] Project-specific AI explanations
* [ ] GitHub integration
* [ ] AI engineering playground
* [ ] LLM-powered project recommendations
* [ ] Better project architecture visualizations
* [ ] Analytics
* [ ] UI/UX improvements
* [ ] Automated deployment pipeline

---

## 🤖 Future AI Chatbot Architecture

The planned personal AI chatbot will allow recruiters and visitors to ask questions about my background, skills, projects, and experience.

```text
              Portfolio Knowledge
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
     Resume       Projects       Skills
       │             │             │
       └─────────────┼─────────────┘
                     ▼
                  Chunking
                     │
                     ▼
                 Embeddings
                     │
                     ▼
                Vector Store
                     │
                     ▼
                 Retrieval
                     │
                     ▼
                    LLM
                     │
                     ▼
             Grounded Response
```

The goal is to make the portfolio itself a demonstration of practical **RAG and AI engineering**.

---

## 🎯 Purpose

This project serves two purposes:

1. **Professional Portfolio** — showcase my AI engineering projects, skills, and experience.
2. **AI Engineering Demonstration** — demonstrate how a modern application can combine a frontend, REST API backend, data layer, and AI capabilities.

---

## 👨‍💻 About Me

**Prashant Kumar**

AI Engineer focused on:

* Generative AI
* RAG systems
* LLM applications
* Python
* FastAPI
* AI agents
* Data and ML systems

I build practical AI-powered applications and continuously work on applying modern AI engineering techniques to real-world problems.

---

## 📫 Connect

* GitHub: https://github.com/PrashantKumar9889
* LinkedIn: https://www.linkedin.com/in/prashant-kumar-64101b304/
* Portfolio: https://prashant-ai-portfoliogit-rej24k6hvpeqx4yqmlzuqm.streamlit.app/

---

## 📄 License

This project is primarily a personal portfolio project.

The code is publicly available for learning and reference. Please do not reproduce the portfolio content, personal information, or project descriptions as your own.
