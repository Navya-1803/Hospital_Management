import mysql.connector
from db_config import get_connection

def fetch_departments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Department")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_department(dept_id, dept_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Department (Dept_ID, Dept_Name) VALUES (%s, %s)",
        (dept_id, dept_name)
    )
    conn.commit()
    conn.close()

def delete_department(dept_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Department WHERE Dept_ID = %s", (dept_id,))
    conn.commit()
    conn.close()
