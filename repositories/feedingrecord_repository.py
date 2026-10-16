from database.connection import get_connection
from datetime import date
from datetime import datetime
from models.animal import Animal
from models.feedingrecord import FeedingRecord
from enums.FeedType import FeedType
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class FeedingRecordRepository:


    def save(self, feedingrecord: FeedingRecord):
        logger.info(
            "Salvando registro de alimentação: animal_id=%s, tipo=%s",
            feedingrecord.animal_id,
            feedingrecord.feeding_type.value,
        )

        conn = get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO feedingrecord (
                    animal_id,
                    feeding_type,
                    feeding_quantity,
                    feeding_date
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    feedingrecord.animal_id,
                    feedingrecord.feeding_type.value,
                    feedingrecord.feeding_quantity,
                    feedingrecord.feeding_date.isoformat(),
                ),
            )

            feedingrecord.id = cursor.lastrowid

            conn.commit()

            logger.info(
                "Registro de alimentação salvo com ID: %s",
                feedingrecord.id,
            )

            return feedingrecord

        finally:
            conn.close()


    def get_by_id(self, id: int):
        query = """
            SELECT id, animal_id, feeding_type, feeding_quantity, feeding_date
            FROM feedingrecord
            WHERE id = ?
        """

        conn = get_connection()

        try:
            cursor = conn.cursor()

            logger.info(f"Buscando feeding Record de ID: {id}")

            cursor.execute(query, (id,))
            resultado = cursor.fetchone()

            logger.info(f"Resultado do banco: {resultado}")

        finally:
            conn.close()

        if resultado is None:
            return None

        converted_date = datetime.fromisoformat(resultado[4])

        return FeedingRecord(
            id=resultado[0],
            animal_id=resultado[1],
            feeding_type=FeedType(resultado[2]),
            feeding_quantity=resultado[3],
            feeding_date=converted_date,
        )

    def find_all(self):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            logger.info(
                "Preparando todos os registros da tabela de alimentação!"
            )

            cursor.execute("SELECT * FROM feedingrecord")
            rows = cursor.fetchall()

            feedingrecords = []

            for row in rows:
                logger.info("Linha do banco: %s", row)

                feedingdate_converted = datetime.fromisoformat(row[4])

                feeding_record = FeedingRecord(
                    id=row[0],
                    animal_id=row[1],
                    feeding_type=FeedType(row[2]),
                    feeding_quantity=row[3],
                    feeding_date=feedingdate_converted,
                )

                feedingrecords.append(feeding_record)

            return feedingrecords

        finally:
            conn.close()

    
    def update(self, feedingrecord: FeedingRecord):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            query = """
                UPDATE feedingrecord
                SET animal_id = ?,
                    feeding_type = ?,
                    feeding_quantity = ?,
                    feeding_date = ?
                WHERE id = ?
            """

            cursor.execute(
                query,
                (
                    feedingrecord.animal_id,
                    feedingrecord.feeding_type.value,
                    feedingrecord.feeding_quantity,
                    feedingrecord.feeding_date.isoformat(),
                    feedingrecord.id,
                ),
            )

            if cursor.rowcount == 0:
                logger.warning(
                    "Nenhum registro de alimentação encontrado para atualizar. "
                    "ID: %s",
                    feedingrecord.id,
                )
            else:
                conn.commit()
                logger.info(
                    "Registro de alimentação atualizado. ID: %s",
                    feedingrecord.id,
                )

        finally:
            conn.close()


    
    def delete(self, id: int):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            logger.info("Excluindo registro de alimentação. ID: %s", id)

            cursor.execute(
                """
                DELETE FROM feedingrecord
                WHERE id = ?
                """,
                (id,),
            )

            if cursor.rowcount == 0:
                logger.warning(
                    "Nenhum registro de alimentação encontrado para excluir. "
                    "ID: %s",
                    id,
                )
            else:
                conn.commit()
                logger.info(
                    "Registro de alimentação excluído. ID: %s",
                    id,
                )

        finally:
            conn.close()
