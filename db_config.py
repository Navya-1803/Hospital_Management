import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="yourUsername",
        password="yourPassword",
        database="nameOfDatabase"
    )
