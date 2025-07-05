import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3307,           # <-- Your custom port
        user="root",
        password="root",
        database="netflix_db"
    )
