# 🤖 Resume AI Assistant

An AI-powered Resume Assistant that allows users to upload a PDF resume and ask natural language questions about its contents. The application extracts text from the uploaded resume, stores it in a MySQL database, and uses Google's Gemini AI to generate context-aware answers based only on the uploaded resume.

## 🚀 Live Demo

**Frontend:** https://resume-ai-assistant-tan.vercel.app/

**Backend API:** https://resume-ai-assistant-backend.onrender.com/

## 📌 Features

* 📄 Upload resume in PDF format
* 🤖 Ask questions about your resume using AI
* 🧠 AI answers only from the uploaded resume
* 💾 Stores resume information in MySQL
* 💬 Saves chat history for every uploaded resume
* 🎨 Responsive React + Tailwind CSS interface
* ☁️ Fully deployed using cloud services

---

## 🏗️ Architecture

```text
React + Tailwind CSS (Vercel)
            │
            ▼
 Flask REST API (Render)
            │
      ┌─────┴────────┐
      ▼              ▼
 Gemini AI      Aiven MySQL
```

---

## 🛠️ Tech Stack

### Frontend

* React
* Vite
* Tailwind CSS
* Axios

### Backend

* Python
* Flask
* Flask-CORS
* PyMuPDF

### AI

* Google Gemini API

### Database

* MySQL
* Aiven Cloud MySQL

### Deployment

* Vercel
* Render

---

## 📂 Project Structure

```text
Resume-AI-Assistant/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── gemini.py
│   ├── resume_parser.py
│   ├── uploads/
│   └── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Vaishnavi10706/Resume-AI-Assistant.git
cd Resume-AI-Assistant
```

---

### Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

Create a `.env` file inside the `backend` folder:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=resume_ai_assistant
DB_SSL=false

GEMINI_API_KEY=your_api_key
```

Run the backend:

```bash
python app.py
```

---

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

## 📌 API Endpoints

### Upload Resume

```
POST /upload
```

Uploads a PDF resume and stores the extracted text.

---

### Ask Question

```
POST /ask
```

Example Request

```json
{
    "question":"Tell me about my projects."
}
```

Example Response

```json
{
    "answer":"You have worked on..."
}
```

---

## 📸 Screenshots

<img width="1576" height="720" alt="Screenshot 2026-07-16 214543" src="https://github.com/user-attachments/assets/bd570dcb-a96f-431f-bbc0-eb092a3d21f6" />


Example:

* Home Page
* Resume Upload
* AI Chat
* Chat History

---

## 🔮 Future Improvements

* User Authentication
* Multiple Resume Support
* Resume Analysis & Suggestions
* AI Resume Score
* Interview Question Generator
* Export Chat as PDF
* Dark Mode
* Voice Assistant
* Docker Support

---

## 👩‍💻 Author

**Vaishnavi**

GitHub: https://github.com/Vaishnavi10706

LinkedIn: *(Add your LinkedIn profile link here)*

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
