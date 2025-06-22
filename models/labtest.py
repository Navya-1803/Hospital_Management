import mysql.connector
from db_config import get_connection

def fetch_lab_tests():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM LabTest")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_lab_test(test_name, patient_id, doctor_id, result):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO LabTest (TestName, Patient_ID, Doctor_ID, Result) VALUES (%s, %s, %s, %s)",
        (test_name, patient_id, doctor_id, result)
    )
    conn.commit()
    conn.close()

def delete_lab_test(test_name, patient_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM LabTest WHERE TestName = %s AND Patient_ID = %s", (test_name, patient_id))
    conn.commit()
    conn.close()
