import axios from "axios";

const api = axios.create({
    baseURL: "https://resume-ai-assistant-backend.onrender.com",
});

export default api;