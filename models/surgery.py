from db_config import get_connection

def fetch_surgeries():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Surgery")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_surgery(surgery_id, pid, did, date, surgery_type):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Surgery VALUES (%s, %s, %s, %s, %s)",
        (surgery_id, pid, did, date, surgery_type)
    )
    conn.commit()
    conn.close()

def delete_surgery(surgery_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Surgery WHERE Surgery_ID = %s", (surgery_id,))
    conn.commit()
    conn.close()
