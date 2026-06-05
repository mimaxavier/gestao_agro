import sqlite3

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

