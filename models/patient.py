import mysql.connector
from db_config import get_connection

def fetch_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Patient")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_patient(patient_id, patient_name, dob, age, phone_no, room_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Patient (Patient_ID, Patient_Name, D_O_B, Age, PhoneNo, RoomNo) VALUES (%s, %s, %s, %s, %s, %s)",
        (patient_id, patient_name, dob, age, phone_no, room_no)
    )
    conn.commit()
    conn.close()

def delete_patient(patient_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Patient WHERE Patient_ID = %s", (patient_id,))
    conn.commit()
    conn.close()
