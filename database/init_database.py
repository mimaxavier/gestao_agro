import sqlite3

conn = sqlite3.connect("database/farm.db")

with open("database/schema.sql") as f:
    conn.executescript(f.read())

conn.close()