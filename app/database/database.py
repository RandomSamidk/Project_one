import mysql.connector

DATABASE_CONFIG={
    'host': 'localhost',
    'user': 'root',
    'password': 'user123',
    'database': 'Hifx',
}

_connection = None

def get_connection():
    global _connection
    if _connection is None or not _connection.is_connected():
        _connection = mysql.connector.connect(**DATABASE_CONFIG)
    return _connection

def get_cursor(dictionary_cursor=False):
    conn = get_connection()
    if dictionary_cursor:
        return conn.cursor(dictionary=True)
    else:
        return conn.cursor()



