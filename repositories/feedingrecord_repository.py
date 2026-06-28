import sqlite3
from datetime import date
from datetime import datetime
from models.animal import Animal
from models.feedingrecord import FeedingRecord
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class FeedingRecordRepository:

    def save(self, feedingrecord):

        logger.info(
            f"Salvando Feeding: {feedingrecord.animal_id}, "
            f"{feedingrecord.type_feeding}, "
            f"{feedingrecord.quantity_feeding}, "
            f"{feedingrecord.date_feeding}"
        )

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO feedingrecord (
            animal_id, 
            type_feeding, 
            quantity_feeding, 
            date_feeding
            )
            VALUES (?, ?, ?, ?)""",
                (
                    feedingrecord.animal_id, 
                    feedingrecord.type_feeding,
                    feedingrecord.quantity_feeding,
                    feedingrecord.date_feeding.isoformat()
                 )
        )

        logger.info(f"ID gerado: {cursor.lastrowid}")

        feedingrecord_id = cursor.lastrowid

        conn.commit()
        conn.close()

        return feedingrecord_id

    def get_by_id(self, animal_id: int):
        query = "SELECT animal_id, type_feeding, quantity_feeding, date_feeding FROM feedingrecord WHERE id = ?"

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        logger.info(f"Buscando feeding Record do animal {animal_id}")

        cursor.execute(query, (animal_id,))
        resultado = cursor.fetchone()

        logger.info(f"Resultado do banco: {resultado}")

        cursor.close()
        conn.close()

        if not resultado:
            return None
        
        converted_date = date.fromisoformat(resultado[3]) if resultado[3] else None

        return FeedingRecord(
            animal_id=resultado[0],
            type_feeding = resultado[1],
            date_feeding = converted_date,
            quantity_feeding = resultado[2],
        )

    def update(self, feedingrecord):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
                       '''UPDATE FROM feedingrecord
                          SET animal_id,
                              type_feeding, 
                              quantity_feeding, 
                              date_feeding
                    ) VALUES (?, ?, ?, ?)''', 
                  ( feedingrecord.animal_id, 
                    feedingrecord.type_feeding,
                    feedingrecord.quantity_feeding,
                    feedingrecord.date_feeding)
        )
        logger.info(f"Atualizando feedrecord id = {feedingrecord.id}")

        cursor.execute()

        conn.commit()
        conn.close()

    def delete(self, animal_id):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute()

        conn.commit()
        conn.close()