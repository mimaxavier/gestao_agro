import sqlite3
from datetime import date
from datetime import datetime
from models.animal import Animal
from models.milkproductionrecord import MilkProductionRecord
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class MilkProductionRecordRepository:

    def save(self, milkproductionrecord):

        logger.info(
            f"Salvando Feeding: {milkproductionrecord.animal_id}, "
            f"{milkproductionrecord.quantity_production}, "
            f"{milkproductionrecord.date_production}, "
            f"{milkproductionrecord.id}"
        )

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
                 """INSERT INTO milkproductionrecord (
            animal_id, 
            quantity_production, 
            date_production, 
            id
            )
            VALUES (?, ?, ?, ?)""",
                (
                    milkproductionrecord.animal_id, 
                    milkproductionrecord.quantity_feeding,
                    milkproductionrecord.date_production,
                    milkproductionrecord.date_production.isoformat()
                 )
        )

        milkproductionrecord.id = cursor.latrowid

        logger.info(f"ID gerado: {cursor.lastrowid}")
        

        conn.commit()
        conn.close()

        return milkproductionrecord

    def get_by_id(self, id: int):
        query = "SELECT id, animal_id, quantity_production, date_production FROM milkproductionrecord WHERE id = ?"

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(query, (id,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if not resultado:
            return None
        
        converted_date = date.fromisoformat(resultado[3]) if resultado[3] else None

        return MilkProductionRecord(
            id = resultado[0],
            animal_id=resultado[1],
            quantity_production = resultado[2],
            date_production = converted_date,
        )

    def update(self, milkproductionrecord: MilkProductionRecord):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
             '''UPDATE milkproductionrecord
                SET animal_id = ?,
                    quantity_production = ?, 
                    date_production = ?,
                WHERE id = ?
                ''', 
                (
                    milkproductionrecord.animal_id, 
                    milkproductionrecord.quantity_feeding,
                    milkproductionrecord.date_production,
                    milkproductionrecord.id
                )
        )
        logger.info(f"Atualizando feedrecord id = {milkproductionrecord.id}")

        conn.commit()
        conn.close()

    def delete(self, id:int):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        logger.info(f"Deletando MilkProductionId {id}")

        cursor.execute(
            """DELETE FROM feedingrecord
                WHERE id = ?""",
                (id,)
        )

        logger.info(f" id = {id} excluído com sucesso!")

        conn.commit()
        conn.close()