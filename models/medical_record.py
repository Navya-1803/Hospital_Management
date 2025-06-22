from db_config import get_connection

def fetch_medical_records():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Medical_Record")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_medical_record(record_id, pid, did, date, diagnosis, treatment):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Medical_Record VALUES (%s, %s, %s, %s, %s, %s)",
        (record_id, pid, did, date, diagnosis, treatment)
    )
    conn.commit()
    conn.close()

def delete_medical_record(record_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Medical_Record WHERE Record_ID = %s", (record_id,))
    conn.commit()
    conn.close()
