import mysql.connector
from db_config import get_connection

def fetch_appointments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Appointment")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_appointment(appointment_id, patient_id, doctor_id, date, time):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Appointment (Appointment_ID, Patient_ID, Doctor_ID, Date, Time) VALUES (%s, %s, %s, %s, %s)",
        (appointment_id, patient_id, doctor_id, date, time)
    )
    conn.commit()
    conn.close()

def delete_appointment(appointment_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Appointment WHERE Appointment_ID = %s", (appointment_id,))
    conn.commit()
    conn.close()

def update_appointment(appointment_id, patient_id, doctor_id, date, time):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Appointment SET Patient_ID = %s, Doctor_ID = %s, Date = %s, Time = %s WHERE Appointment_ID = %s",
        (patient_id, doctor_id, date, time, appointment_id)
    )
    conn.commit()
    conn.close()
