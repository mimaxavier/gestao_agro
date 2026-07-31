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
            f"Salvando MilkProductionRecord:  {milkproductionrecord.animal_id}, "
            f"{milkproductionrecord.quantity_production}, "
            f"{milkproductionrecord.production_date}, "
            f"{milkproductionrecord.id}"
        )

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO milkproductionrecord (
            animal_id, 
            quantity_production, 
            production_date
            )
            VALUES (?, ?, ?)""",
                (
                    milkproductionrecord.animal_id, 
                    milkproductionrecord.quantity_production,
                    milkproductionrecord.production_date.isoformat(),
                ),
        )

        milkproductionrecord.id = cursor.lastrowid

        logger.info(f"ID gerado: {cursor.lastrowid}")
        

        conn.commit()
        conn.close()

        return milkproductionrecord

    def get_by_id(self, id: int):
        query = "SELECT id, animal_id, quantity_production, production_date FROM milkproductionrecord WHERE id = ?"

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(query, (id,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if not resultado:
            return None
        
        converted_date = datetime.fromisoformat(resultado[3]) if resultado[3] else None

        return MilkProductionRecord(
            id = resultado[0],
            animal_id=resultado[1],
            quantity_production = resultado[2],
            production_date = converted_date
        )

    def find_all(self):
            conn = sqlite3.connect("database/farm.db")
    
            cursor = conn.cursor()
    
            logger.info(f"Preparando todos os registros da tabela de produção!")
    
            cursor.execute(
                """SELECT * FROM milkproductionrecord"""
            )
    
            rows = cursor.fetchall()
    
            milkproductionrecord = []
    
            for row in rows:
                logger.info("Linha do banco: %s", row)
    
                converted_birthdate = datetime.fromisoformat(row[3] if row[3] else None)
    
                logger.info("Data convertida fica %s",converted_birthdate)
    
                milkproduction = MilkProductionRecord(
    
                    id = row[0],
                    animal_id= row[1],
                    quantity_production= row[2],
                    production_date= converted_birthdate
    
                )
    
                milkproductionrecord.append(milkproduction)
    
            conn.close()
    
    
            return milkproductionrecord

    def update(self, milkproductionrecord: MilkProductionRecord):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
             '''UPDATE milkproductionrecord
                SET animal_id = ?,
                    quantity_production = ?, 
                    production_date = ?
                WHERE id = ?
                ''', 
                (
                    milkproductionrecord.animal_id, 
                    milkproductionrecord.quantity_production,
                    milkproductionrecord.production_date,
                    milkproductionrecord.id
                )
        )
        logger.info(f"Atualizando milkrecord id = {milkproductionrecord.id}")

        conn.commit()
        conn.close()

    def delete(self, id:int):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        logger.info(f"Deletando MilkProductionId {id}")

        cursor.execute(
            """DELETE FROM milkproductionrecord
                WHERE id = ?""",
                (id,)
        )

        logger.info(f" id = {id} excluído com sucesso!")

        conn.commit()
        conn.close()