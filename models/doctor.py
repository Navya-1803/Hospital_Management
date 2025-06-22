import sqlite3

def get_db_connection():
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_doctors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Doctor')
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_doctor(doctor_id, doctor_name, specialization, dept_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Doctor (Doctor_ID, Doctor_Name, Specialization, Dept_ID)
        VALUES (?, ?, ?, ?)
    ''', (doctor_id, doctor_name, specialization, dept_id))
    conn.commit()
    conn.close()

def delete_doctor(doctor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Doctor WHERE Doctor_ID = ?', (doctor_id,))
    conn.commit()
    conn.close()
