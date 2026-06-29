import os
from google import genai
from dotenv import load_dotenv

load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_gemini(resume_text, question):

    prompt = f"""
You are a career assistant.

Answer only using information available in the resume.

Resume:
{resume_text}

Question:
{question}

If the answer is not available in the resume, say:
"I could not find this information in the resume."
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text