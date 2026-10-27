import sqlite3


def get_connection(db_path="database/farm.db"):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn