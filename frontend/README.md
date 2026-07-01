🤖 Resume AI Assistant

An AI-powered web application that allows users to upload their resume and ask questions about it. The application uses Google Gemini AI to answer questions based only on the uploaded resume, making it useful for interview preparation and resume review.

---

🚀 Features

📄 Resume Upload

- Upload resume in PDF format
- Extracts text using PyMuPDF
- Stores resume data in MySQL database

🤖 AI Question Answering

- Ask questions about your resume
- AI answers only from the uploaded resume
- Powered by Google Gemini API

💻 Modern Frontend

- Built with React and Vite
- Styled using Tailwind CSS
- Responsive and clean user interface

🔧 Backend API

- Flask REST API
- Resume upload endpoint
- AI question-answering endpoint
- MySQL database integration

---

🛠️ Tech Stack

Frontend

- React 19
- Vite
- Tailwind CSS
- Axios

Backend

- Python
- Flask
- Flask-CORS

Database

- MySQL

AI

- Google Gemini API

Resume Parsing

- PyMuPDF (fitz)

---

📂 Project Structure
```
Resume-AI-Assistant/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── gemini.py
│   ├── resume_parser.py
│   ├── uploads/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx
│   │   │   ├── UploadResume.jsx
│   │   │   └── ChatBox.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   └── index.css
│   │
│   └── package.json
│
└── README.md
```
---

⚙️ Installation

1. Clone the repository
```
git clone https://github.com/Vaishnavi10706/Resume-AI-Assistant.git
```
2. Backend Setup
```
cd backend

python -m venv venv
```
# Windows
```
venv\Scripts\activate

pip install -r requirements.txt
```
Create a ".env" file inside the backend folder.
```
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=resume_ai_assistant

GEMINI_API_KEY=your_api_key
```
Start the Flask server.
```
python app.py
```
---

3. Frontend Setup
```
cd frontend

npm install

npm run dev
```
---

📡 API Endpoints

Upload Resume

POST /upload

Uploads a PDF resume, extracts its text, and stores it in MySQL.

---

Ask AI

POST /ask

Example Request

{
    "question": "Tell me about my projects."
}

Example Response

{
    "answer": "Based on your resume..."
}

---

📌 Current Progress

- ✅ React + Flask project setup
- ✅ Resume PDF upload
- ✅ Resume text extraction
- ✅ MySQL database integration
- ✅ Google Gemini AI integration
- ✅ AI-powered question answering
- ✅ REST API development
- ✅ Tailwind CSS integration
- ✅ Responsive upload interface

---

🚧 Upcoming Features

- AI chat interface with chat bubbles
- Conversation history
- Loading animation
- Drag & drop resume upload
- Dark mode
- Authentication
- Resume management
- Deployment

---

👩‍💻 Author

Vaishnavi

GitHub: https://github.com/Vaishnavi10706
