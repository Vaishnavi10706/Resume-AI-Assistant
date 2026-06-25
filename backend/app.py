from flask import Flask, request, jsonify
from flask_cors import CORS
import os

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

    return jsonify({
        "message": "Resume uploaded successfully",
        "filename": file.filename
    })

if __name__ == "__main__":
    app.run(debug=True)