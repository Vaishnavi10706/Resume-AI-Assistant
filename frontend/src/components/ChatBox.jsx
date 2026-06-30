import { useState } from "react";
import api from "../services/api";

function ChatBox() {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");
    const [loading, setLoading] = useState(false);
    const askQuestion = async () => {
        if (!question.trim()) {
            return;
        }
        setLoading(true);
        try {
            const response = await api.post("/ask", {
                question: question
            });
            setAnswer(response.data.answer);
        } catch (error) {
            console.error(error);
            setAnswer("Something went wrong.");
        }
        setLoading(false);
    };
    return (
        <div>
            <h2>Ask About Your Resume</h2>
            <input
                type="text"
                placeholder="Ask a question..."
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
            />
            <button onClick={askQuestion}>Send</button>
            <br />
            <br />
            {loading && <p>Thinking...</p>}
            {answer && (
                <div>
                    <h3>AI Response</h3>
                    <p>{answer}</p>
                </div>
            )}
        </div>
    );
}
export default ChatBox;