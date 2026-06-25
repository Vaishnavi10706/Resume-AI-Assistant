import { useState } from "react";
import axios from "axios";

function UploadResume(){

    const [file,setFile] = useState(null);
    const [message,setMessage] = useState("");

    const handleUpload = async()=>{
        if(!file){
            setMessage("Please select a resume");
            return;
        }
        const formData = new FormData();
        formData.append("resume",file);
        try{
            const response = await axios.post(
                "http://127.0.0.1:5000/upload",
                formData
            );
            setMessage(response.data.message);
        }catch(error){
            console.log(error);
            setMessage(
                "Upload failed"
            );
        }
    }
    return(
        <div>
            <h2>Upload Resume</h2>
            <input
                type="file"
                accept=".pdf"
                onChange={(e)=>setFile(e.target.files[0])}/>
            <br/>
            <br/>
            <button onClick={handleUpload}>Upload</button>
            <p>{message}</p>
        </div>
    )
}
export default UploadResume;