from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from resume_parser import extract_text
from database import (
    save_resume,
    get_latest_resume,
    get_latest_resume_id,
    save_chat,
    get_chat_history
)
from gemini import ask_gemini

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Resume AI Assistant Backend Running"

@app.route("/upload", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    file = request.files["resume"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )
    file.save(file_path)
    resume_text = extract_text(file_path)
    resume_id = save_resume(
        file.filename,
        resume_text
    )
    print(f"Resume saved successfully with ID: {resume_id}")
    return jsonify({
        "message": "Resume uploaded successfully",
        "filename": file.filename
    })

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({
            "error": "Question is required."
        }), 400
    resume_text = get_latest_resume()
    resume_id = get_latest_resume_id()
    if not resume_text:
        return jsonify({
            "error": "No resume found."
        }), 404
    answer = ask_gemini(
        resume_text,
        question
    )
    save_chat(
        resume_id,
        question,
        answer
    )
    return jsonify({
        "answer": answer
    })

@app.route("/chats", methods=["GET"])
def get_chats():
    resume_id = get_latest_resume_id()
    if not resume_id:
        return jsonify([])
    chats = get_chat_history(resume_id)
    messages = []
    for question, answer in chats:
        messages.append({
            "sender": "user",
            "text": question
        })
        messages.append({
            "sender": "ai",
            "text": answer
        })
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)