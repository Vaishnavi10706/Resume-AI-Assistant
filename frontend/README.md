📄 Resume AI Assistant

An AI-powered Resume Assistant that allows users to upload their resumes and interact with an intelligent chatbot to receive personalized responses based on the uploaded resume.

This project is being built using React, Flask, MySQL, and the Gemini API.

---

🚀 Tech Stack

Frontend

- React
- Vite
- Axios

Backend

- Python
- Flask
- Flask-CORS

Database

- MySQL (coming soon)

AI

- Google Gemini API (coming soon)

PDF Processing

- PyMuPDF

---

✨ Features

✅ Completed

- Flask backend setup
- React + Vite frontend setup
- REST API for resume upload
- PDF upload from React frontend
- CORS configuration
- File storage in the backend "uploads/" directory
- API testing setup using VS Code REST Client

🚧 In Progress

- Extract text from uploaded PDF
- Store extracted resume data in MySQL
- Integrate Gemini API for AI-powered responses
- Chat interface
- Resume-based question answering

📌 Planned Features

- User authentication (Login/Register)
- Chat history
- Resume analysis dashboard
- Suggested interview questions
- Skill extraction
- Project extraction
- Experience summary
- Responsive UI
- Dark mode

---

📂 Project Structure
```
resume-ai-assistant/
│
├── backend/
│   ├── app.py
│   ├── database.py
│   ├── gemini.py
│   ├── resume_parser.py
│   ├── uploads/
│   └── test.http
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── UploadResume.jsx
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   └── package.json
│
├── .gitignore
└── README.md
```
---

⚙️ Getting Started

Clone the Repository
```
git clone https://github.com/Vaishnavi10706/Resume-AI-Assistant.git
```
Backend Setup
```
cd backend

python -m venv venv
```
# Windows
```
venv\Scripts\activate

pip install -r requirements.txt

python app.py
```
The backend will start at:

http://127.0.0.1:5000

Frontend Setup
```
cd frontend

npm install

npm run dev
```
The frontend will start at:

http://localhost:5173

---

📌 Current Workflow
```
User
   │
   ▼
Select Resume (PDF)
   │
   ▼   
React Frontend
   │
   ▼
Flask Backend
   │
   ▼
Store PDF in uploads
```
---

🛣️ Roadmap

- [x] Backend setup
- [x] Frontend setup
- [x] Resume upload API
- [x] Resume upload UI
- [ ] PDF text extraction
- [ ] MySQL integration
- [ ] Gemini API integration
- [ ] AI chatbot
- [ ] Resume analysis
- [ ] Authentication
- [ ] Chat history

---

👩‍💻 Author

Vaishnavi

GitHub: https://github.com/Vaishnavi10706
