import { useState } from "react";
import api from "../services/api";
import ChatMessage from "./ChatMessage";

function ChatBox() {
    const [question, setQuestion] = useState("");
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);
    const askQuestion = async () => {
        if (question.trim() === "") {
            return;
        }
        const userMessage = {
            sender: "user",
            text: question
        };
        setMessages((prev) => [...prev, userMessage]);
        setLoading(true);
        try {
            const response = await api.post("/ask", {
                question: question
            });
            const aiMessage = {
                sender: "ai",
                text: response.data.answer
            };
            setMessages((prev) => [...prev, aiMessage]);
        } catch (error) {
            console.log(error);
            setMessages((prev) => [
                ...prev,
                {
                    sender: "ai",
                    text: "Something went wrong."
                }
            ]);
        }
        setQuestion("");
        setLoading(false);
    };
    return (
        <div>
            <h2 className="text-2xl font-semibold mb-4">💬 Chat</h2>
            <div className="border rounded-lg h-96 overflow-y-auto p-4 bg-gray-50">
                {messages.length === 0 && (
                    <p className="text-gray-500">Ask anything about your resume.</p>
                )}
                {messages.map((message, index) => (
                    <ChatMessage
                        key={index}
                        sender={message.sender}
                        text={message.text}/>
                ))}
                {loading && (
                    <p className="text-gray-500">AI is thinking...</p>
                )}
            </div>
            <div className="flex gap-3 mt-4">
                <input
                    type="text"
                    placeholder="Ask a question..."
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    className="flex-1 border rounded-lg px-4 py-2"
                />
                <button
                    onClick={askQuestion}
                    className="bg-blue-600 text-white px-5 rounded-lg hover:bg-blue-700">
                    Send
                </button>
            </div>
        </div>
    );
}
export default ChatBox;