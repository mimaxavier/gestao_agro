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
            f"{feedingrecord.id}"
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

        feedingrecord.id = cursor.lastrowid

        logger.info(f"ID gerado: {cursor.lastrowid}")

        conn.commit()
        conn.close()

        return feedingrecord

    def get_by_id(self, id: int):
        query = "SELECT id, animal_id, type_feeding, quantity_feeding, date_feeding FROM feedingrecord WHERE id = ?"

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        logger.info(f"Buscando feeding Record de ID: {id}")

        cursor.execute(query, (id,))
        resultado = cursor.fetchone()

        logger.info(f"Resultado do banco: {resultado}")

        cursor.close()
        conn.close()

        if not resultado:
            return None
        
        converted_date = date.fromisoformat(resultado[4]) if resultado[4] else None

        return FeedingRecord(
            id = resultado[0],
            animal_id=resultado[1],
            type_feeding = resultado[2],
            quantity_feeding = resultado[3],
            date_feeding = converted_date,
        )

    def update(self, feedingrecord: FeedingRecord):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
                '''UPDATE feedingrecord
                SET animal_id = ?,
                    type_feeding = ?, 
                    quantity_feeding = ?, 
                    date_feeding = ?
                WHERE id = ?
                ''', 
                (
                    feedingrecord.animal_id, feedingrecord.type_feeding, feedingrecord.quantity_feeding, feedingrecord.date_feeding, feedingrecord.id
                )
        )
        logger.info(f"Atualizando feedrecord id = {feedingrecord.id}")

        conn.commit()
        conn.close()

    def delete(self, id:int):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        logger.info(f"Deletar feedrecord id = {id}")

        cursor.execute(
                """DELETE FROM feedingrecord
                WHERE id = ?""",
                (id,)
                
        )

        logger.info(f" id = {id} excluído com sucesso!")

        conn.commit()
        conn.close()