from db_config import get_connection

def fetch_emergencies():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Emergency")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_emergency(cid, pid, date, details, phone_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Emergency VALUES (%s, %s, %s, %s, %s)",
        (cid, pid, date, details, phone_no)
    )
    conn.commit()
    conn.close()

def delete_emergency(cid):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Emergency WHERE Case_ID = %s", (cid,))
    conn.commit()
    conn.close()
