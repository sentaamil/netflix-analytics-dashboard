from db_config.connection import get_connection

try:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("✅ Connection successful! Tables in 'netflix_db':")
    for table in tables:
        print(table[0])
    conn.close()
except Exception as e:
    print("❌ Connection failed!")
    print(e)
