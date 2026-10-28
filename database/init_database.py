import sqlite3

def init_database(db_path="database/farm.db"):
    conn = sqlite3.connect(db_path)
    try:
        with open("database/schema.sql") as f:
            conn.executescript(f.read())
    finally:
        conn.close()