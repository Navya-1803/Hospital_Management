from db_config import get_connection

def fetch_insurances():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Insurance")
    data = cursor.fetchall()
    conn.close()
    return data

def insert_insurance(pid, provider, coverage_amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Insurance (Patient_ID, Provider, Coverage_Amount) VALUES (%s, %s, %s)",
        (pid, provider, coverage_amount)
    )
    conn.commit()
    conn.close()

def delete_insurance(policy_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Insurance WHERE Policy_ID = %s", (policy_id,))
    conn.commit()
    conn.close()
