# test_db.py

import sqlite3

conn = sqlite3.connect("database/farm.db")

print("Banco conectado!")

conn.close()