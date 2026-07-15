import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def ask_gemini(resume_text, question):
    prompt = f"""
You are an AI Resume Assistant.

Your job is to answer questions only from the uploaded resume.

Instructions:
- Use only the information provided in the resume.
- Do not make assumptions or add information that is not present.
- If the answer is not available, reply exactly:
  "I could not find this information in the resume."
- Keep your answers clear and well organized.
- If the user asks for projects, skills, education, or experience, list them using bullet points whenever appropriate.

Resume:
{resume_text}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text