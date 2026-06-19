import sqlite3
from datetime import date
from datetime import datetime
from models.animal import Animal
from typing import Optional

class AnimalRepository:

    def save(self, animal):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
            """ INSERT INTO animals (
                especie,
                birth_date,
                weight
            )
            VALUES (?, ?, ?)""",
                    (
                    animal.especie,
                    animal.birth_date, 
                    animal.weight
                     )
        )

        conn.commit()
        conn.close()

    def get_by_id(self, animal_id: int) -> Optional[Animal]:
        query = "SELECT especie, birth_date, weight, id FROM animals WHERE id = ?"

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(query, (animal_id,))
        resultado = cursor.fetchone
        conn.close()

        if not resultado:
            return None
        
        birth_date = date.fromisoformat(resultado[1]) if resultado[2] else None

        return Animal(
            especie = resultado[0],
            birth_date = birth_date,
            weight = resultado[2],
            id = resultado[0]
        )


        conn.close()

        return resultado

    def update(self, animal):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
            """ UPDATE animals
                    SET especie = ?, birth_date = ?, 
                    weight = ?
                WHERE id = ? """,
                (animal.especie,
                 animal.birth_date,
                 animal.weight,
                 animal.id
                 )
            )

        conn.commit()
        conn.close()

    def delete(self, animal_id):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
            """ DELETE FROM animals WHERE id = ? """,
                (animal_id, )

        )

        conn.commit()
        conn.close()
