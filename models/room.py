import sqlite3

def get_db_connection():
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_rooms():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Room')
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_room(room_no, room_type, patient_id, room_status):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Room (RoomNo, Room_Type, Patient_ID, Room_Status)
        VALUES (?, ?, ?, ?)
    ''', (room_no, room_type, patient_id, room_status))
    conn.commit()
    conn.close()

def delete_room(room_no):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Room WHERE RoomNo = ?', (room_no,))
    conn.commit()
    conn.close()
