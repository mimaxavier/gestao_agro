import sqlite3
from datetime import date
from datetime import datetime
from models.vaccineapplicationrecord import VaccineApplication
from enums.VaccineName import VaccineName
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class VaccineApplicationRepository:

    def save(self, vaccineapplication):

        logger.info(
            f"Salvando VaccineApplication: {vaccineapplication.animal_id}, "
            f"{vaccineapplication.vaccine_name}, "
            f"{vaccineapplication.apply_date}, "
            f"{vaccineapplication.id}"
        )

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
            """INSERT INTO vaccinesapplication (
            animal_id,
            vaccine_name,
            apply_date
            )
            VALUES (?, ?, ?)""",
            (
                vaccineapplication.animal_id,
                vaccineapplication.vaccine_name,
                vaccineapplication.apply_date.isoformat(),
            )
        )

        vaccineapplication.id = cursor.lastrowid

        logger.info(f"ID gerado: {cursor.lastrowid}")

        conn.commit()
        conn.close()

    def get_by_id(self, id: int):
        query = "SELECT animal_id, vaccine_name, apply_date, id FROM vaccinesapplication WHERE id = ?"

        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(query, (id,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        if not resultado:
            return None
        
        converted_date = date.fromisoformat(resultado[2]) if resultado[2] else None

        return VaccineApplication(
            id=resultado[3],
            animal_id = resultado[0],
            apply_date = converted_date,
            vaccine_name = VaccineName(resultado[1]),
        )

    def find_all(self):
        conn = sqlite3.connect("database/farm.db")
            
        cursor = conn.cursor()
            
        logger.info(f"Preparando todos os registros da tabela de vacinação!")
            
        cursor.execute(
                        """SELECT * FROM vaccinesapplication"""
                    )
            
        rows = cursor.fetchall()
            
        vaccineapplicationrecord = []
            
        for row in rows:
            logger.info("Linha do banco: %s", row)
            
        applydate_converted = datetime.fromisoformat(row[4] if row[4] else None)
            
        logger.info("Data convertida fica %s",applydate_converted)
            
        vaccineapplication_record = VaccineApplication(
                             
            id = row[0],
            animal_id= row[1],
            vaccine_name = VaccineName(row[2]),
            feeding_quantity = row[3],
            feeding_date= applydate_converted
            
                        )
            
        vaccineapplicationrecord.append(vaccineapplication_record)
            
        conn.close()
            
            
        return vaccineapplicationrecord

    def update(self, vaccineapplication: VaccineApplication):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        cursor.execute(
        '''UPDATE vaccinesapplication
            SET animal_id = ?,
                vaccine_name = ?,
                apply_date = ?
            WHERE id = ?
            ''',
            (
                vaccineapplication.animal_id,
                vaccineapplication.vaccine_name,
                vaccineapplication.apply_date,
                vaccineapplication.id
            )
        )
        logger.info(f"Atualizando vaccineapplication id = {vaccineapplication.id}")

        conn.commit()
        conn.close()

    def delete(self, id: int):
        conn = sqlite3.connect("database/farm.db")

        cursor = conn.cursor()

        logger.info(f"Deletando VaccineApplication de ID = {id}")

        cursor.execute(
            """DELETE FROM vaccinesapplication
                WHERE id = ?""",
                (id,)
        )

        logger.info(f" id = {id} excluído com sucesso!")

        conn.commit()
        conn.close()