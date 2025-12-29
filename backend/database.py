import sqlite3

DB_NAME = "decisions.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS decisions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            date TEXT NOT NULL,
            taken_path TEXT NOT NULL,
            reflection TEXT,
            mood INTEGER
        )
    """)
    conn.commit()
    conn.close()