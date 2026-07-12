function ChatMessage({ sender, text }) {
    const isUser = sender === "user";
    return (
        <div
            className={`flex mb-4 ${
                isUser ? "justify-end" : "justify-start"
            }`}>
            <div
                className={`max-w-xl px-4 py-3 rounded-lg ${
                    isUser
                        ? "bg-blue-500 text-white"
                        : "bg-gray-200 text-black"
                }`}>
                <p className="text-sm font-semibold mb-1">
                    {isUser ? "You" : "AI Assistant"}
                </p>
                <p>{text}</p>
            </div>
        </div>
    );
}
export default ChatMessage;