import sqlite3
from datetime import date
from datetime import datetime
from models.animal import Animal
from typing import Optional

class VaccineApplication:

    def save(self, animal):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute()

        conn.commit()
        conn.close()

    def get_by_id(self, animal_id: int):
        query = "SELECT especie, birth_date, weight, id FROM animals WHERE id = ?"

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(query, (animal_id,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if not resultado:
            return None
        
        converted_date = date.fromisoformat(resultado[1]) if resultado[1] else None

        return Animal(
            id=resultado[3],
            especie = resultado[0],
            birth_date = converted_date,
            weight = resultado[2],
        )

    def update(self, animal):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute()

        conn.commit()
        conn.close()

    def delete(self, animal_id):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute()

        conn.commit()
        conn.close()