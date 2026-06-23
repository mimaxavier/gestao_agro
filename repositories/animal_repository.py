import sqlite3
from datetime import date
from datetime import datetime
from models.animal import Animal
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class AnimalRepository:

    def save(self, animal):

        logger.info(
            f"Salvando animal: {animal.especie}, "
            f"{animal.birth_date}, "
            f"{animal.weight}"
        )

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
                    animal.birth_date.isoformat(), 
                    animal.weight
                     )
        )

        logger.info(f"ID gerado: {cursor.lastrowid}")

        animal_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return animal_id

    def get_by_id(self, animal_id: int):
        query = "SELECT especie, birth_date, weight, id FROM animals WHERE id = ?"

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        logger.info(f"Buscando animal {animal_id}")

        cursor.execute(query, (animal_id,))
        resultado = cursor.fetchone()

        logger.info(f"Resultado do banco: {resultado}")

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

        logger.info(f"Atualizando animal id={animal.id}")

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

        logger.info(f"Animal atualizado com sucesso id={animal.id}")
        logger.info(f"Dados novos: especie={animal.especie}, weight={animal.weight}")

        conn.close()

    def delete(self, animal_id):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        logger.info(f"Deletando animal id={animal_id}")

        cursor.execute(
            """ DELETE FROM animals WHERE id = ? """,
                (animal_id, )

        )

        conn.commit()

        if cursor.rowcount == 0:
            logger.warning(f"Nenhum animal encontrado para deletar id={animal_id}")
        else:
            logger.info(f"Delete executado com sucesso id={animal_id}")

        conn.close()
