import mysql.connector
from db_config import get_connection

def fetch_blood_banks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Blood_Bank")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_blood_bank(blood_id, patient_id, blood_type, availability, donor_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Blood_Bank (Blood_ID, Patient_ID, Blood_Type, Availability, Donor_name) VALUES (%s, %s, %s, %s, %s)",
        (blood_id, patient_id, blood_type, availability, donor_name)
    )
    conn.commit()
    conn.close()

def delete_blood_bank(blood_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Blood_Bank WHERE Blood_ID = %s", (blood_id,))
    conn.commit()
    conn.close()
