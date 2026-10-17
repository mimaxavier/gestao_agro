from database.connection import get_connection
from datetime import date
from datetime import datetime
from models.vaccineapplicationrecord import VaccineApplication
from enums.VaccineName import VaccineName
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class VaccineApplicationRepository:

    
    def save(self, vaccineapplication: VaccineApplication):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO vaccinesapplication (
                    animal_id, vaccine_name, apply_date
                )
                VALUES (?, ?, ?)
                """,
                (
                    vaccineapplication.animal_id,
                    vaccineapplication.vaccine_name.value,
                    vaccineapplication.apply_date.isoformat(),
                ),
            )

            vaccineapplication.id = cursor.lastrowid
            conn.commit()

            logger.info(
                "Vacinação registrada com ID: %s",
                vaccineapplication.id,
            )

        finally:
            conn.close()


    
    def get_by_id(self, id: int):
        query = """
            SELECT animal_id, vaccine_name, apply_date, id
            FROM vaccinesapplication
            WHERE id = ?
        """

        conn = get_connection()

        try:
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            resultado = cursor.fetchone()
        finally:
            conn.close()

        if resultado is None:
            return None

        converted_date = date.fromisoformat(resultado[2])

        return VaccineApplication(
            id=resultado[3],
            animal_id=resultado[0],
            vaccine_name=VaccineName(resultado[1]),
            apply_date=converted_date,
        )

    def find_all(self):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            logger.info("Preparando todos os registros de vacinação!")

            cursor.execute(
                """
                SELECT id, animal_id, vaccine_name, apply_date
                FROM vaccinesapplication
                """
            )

            rows = cursor.fetchall()
            vaccineapplicationrecord = []

            for row in rows:
                applydate_converted = date.fromisoformat(row[3])

                vaccineapplication_record = VaccineApplication(
                    id=row[0],
                    animal_id=row[1],
                    vaccine_name=VaccineName(row[2]),
                    apply_date=applydate_converted,
                )

                vaccineapplicationrecord.append(vaccineapplication_record)

            return vaccineapplicationrecord

        finally:
            conn.close()


    
    def update(self, vaccineapplication: VaccineApplication):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE vaccinesapplication
                SET animal_id = ?,
                    vaccine_name = ?,
                    apply_date = ?
                WHERE id = ?
                """,
                (
                    vaccineapplication.animal_id,
                    vaccineapplication.vaccine_name.value,
                    vaccineapplication.apply_date.isoformat(),
                    vaccineapplication.id,
                ),
            )

            conn.commit()

            logger.info(
                "Registro de vacinação atualizado. ID: %s",
                vaccineapplication.id,
            )

        finally:
            conn.close()

    
    def delete(self, id: int):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM vaccinesapplication
                WHERE id = ?
                """,
                (id,),
            )

            conn.commit()

            logger.info("Exclusão de registro de vacinação solicitada. ID: %s", id)

        finally:
            conn.close()
