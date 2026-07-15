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

def get_latest_resume():
    connection = get_connection()
    cursor = connection.cursor()
    query = """
    SELECT resume_text
    FROM resumes
    ORDER BY id DESC
    LIMIT 1
    """
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        return result[0]
    return None

def save_chat(resume_id, question, answer):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO chats (resume_id, question, answer)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (resume_id, question, answer)
    )

    connection.commit()

    cursor.close()
    connection.close()

def get_latest_resume_id():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT id
    FROM resumes
    ORDER BY id DESC
    LIMIT 1
    """

    cursor.execute(query)

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        return result[0]

    return None

def get_chat_history(resume_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT question, answer
    FROM chats
    WHERE resume_id = %s
    ORDER BY created_at ASC
    """

    cursor.execute(query, (resume_id,))

    chats = cursor.fetchall()

    cursor.close()
    connection.close()

    return chats