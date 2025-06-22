from db_config import get_connection

def fetch_pharmacy():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Pharmacy")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_pharmacy(medicine_id, medicine_name, price, stock):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Pharmacy (Medicine_ID, Medicine_Name, Price, Stock) VALUES (%s, %s, %s, %s)",
        (medicine_id, medicine_name, price, stock)
    )
    conn.commit()
    conn.close()

def delete_pharmacy(medicine_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pharmacy WHERE Medicine_ID = %s", (medicine_id,))
    conn.commit()
    conn.close()
