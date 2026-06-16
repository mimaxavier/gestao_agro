import sqlite3
from models.animal import Animal

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

    def get_by_id():
        pass

    def update():
        pass

