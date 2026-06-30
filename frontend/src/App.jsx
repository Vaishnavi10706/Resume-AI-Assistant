import Header from "./components/Header";
import UploadResume from "./components/UploadResume";
import ChatBox from "./components/ChatBox";

function App() {
    return (
        <div className="min-h-screen bg-slate-100 py-10 px-4">
            <div className="max-w-4xl mx-auto">
                <Header />
                <div className="bg-white rounded-2xl shadow-xl p-8">
                    <UploadResume />
                    <hr className="my-8" />
                    <ChatBox />
                </div>
            </div>
        </div>
    );
}

export default App;