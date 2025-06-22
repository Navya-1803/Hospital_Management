import sqlite3

def get_db_connection():
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_staff():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Staff')
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_staff(staff_id, staff_name, staff_role, dept_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Staff (Staff_ID, Staff_Name, Staff_Role, Dept_ID)
        VALUES (?, ?, ?, ?)
    ''', (staff_id, staff_name, staff_role, dept_id))
    conn.commit()
    conn.close()

def delete_staff(staff_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Staff WHERE Staff_ID = ?', (staff_id,))
    conn.commit()
    conn.close()
