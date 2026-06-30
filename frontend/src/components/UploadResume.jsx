import { useState } from "react";
import api from "../services/api";

function UploadResume() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [uploading, setUploading] = useState(false);

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a resume.");
      return;
    }
    setUploading(true);
    const formData = new FormData();
    formData.append("resume", file);
    try {
      const response = await api.post("/upload", formData);
      setMessage(response.data.message);
    } catch (error) {
      console.error(error);
      setMessage("Upload failed.");
    }
    setUploading(false);
  };
  return (
    <div className="border rounded-xl p-6 bg-slate-50">
      <h2 className="text-2xl font-semibold mb-5">
        📄 Upload Resume
      </h2>
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4 block w-full"
      />
      {file && (
        <p className="text-sm text-gray-600 mb-4">
          Selected File:
          <span className="font-medium">
            {" "}
            {file.name}
          </span>
        </p>
      )}
      <button
        onClick={handleUpload}
        disabled={uploading}
        className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white px-6 py-2 rounded-lg transition"
      >
        {uploading ? "Uploading..." : "Upload Resume"}
      </button>
      {message && (
        <div className="mt-4 p-3 rounded-lg bg-green-100 text-green-800">
          {message}
        </div>
      )}
    </div>
  );
}
export default UploadResume;