import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    
def save_resume(filename, resume_text):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
    INSERT INTO resumes (filename, resume_text)
    VALUES (%s, %s)
    """
    cursor.execute(query, (filename, resume_text))
    connection.commit()
    inserted_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return inserted_id