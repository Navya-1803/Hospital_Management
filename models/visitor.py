from db_config import get_connection

def fetch_visitors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Visitor")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_visitor(visitor_id, name, relationship, pid, phone_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Visitor VALUES (%s, %s, %s, %s, %s)",
        (visitor_id, name, relationship, pid, phone_no)
    )
    conn.commit()
    conn.close()

def delete_visitor(visitor_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Visitor WHERE Visitor_ID = %s", (visitor_id,))
    conn.commit()
    conn.close()
