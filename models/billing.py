import mysql.connector
from db_config import get_connection

def fetch_billings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Billing")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_billing(billing_id, patient_id, amount, date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Billing (Billing_ID, Patient_ID, Amount, Date) VALUES (%s, %s, %s, %s)",
        (billing_id, patient_id, amount, date)
    )
    conn.commit()
    conn.close()

def delete_billing(billing_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Billing WHERE Billing_ID = %s", (billing_id,))
    conn.commit()
    conn.close()

def update_billing(billing_id, patient_id, amount, date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Billing SET Patient_ID = %s, Amount = %s, Date = %s WHERE Billing_ID = %s",
        (patient_id, amount, date, billing_id)
    )
    conn.commit()
    conn.close()  
