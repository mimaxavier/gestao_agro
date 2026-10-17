from database.connection import get_connection
from datetime import datetime
from models.milkproductionrecord import MilkProductionRecord
import logging

logger = logging.getLogger(__name__)

class MilkProductionRecordRepository:

    def save(self, milkproductionrecord):

        logger.info(
            f"Salvando MilkProductionRecord: {milkproductionrecord.animal_id}, "
            f"{milkproductionrecord.quantity_production}, "
            f"{milkproductionrecord.production_date}, "
            f"{milkproductionrecord.id}"
        )

        conn = get_connection()

        try:
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

            return milkproductionrecord

        finally:
            conn.close()

    
    def get_by_id(self, id: int):
        query = """
            SELECT id, animal_id, quantity_production, production_date
            FROM milkproductionrecord
            WHERE id = ?
        """

        conn = get_connection()

        try:
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            resultado = cursor.fetchone()

            if not resultado:
                return None

            converted_date = (
                datetime.fromisoformat(resultado[3])
                if resultado[3]
                else None
            )

            return MilkProductionRecord(
                id=resultado[0],
                animal_id=resultado[1],
                quantity_production=resultado[2],
                production_date=converted_date
            )

        finally:
            conn.close()


    
    def find_all(self):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            logger.info("Preparando todos os registros da tabela de produção!")

            cursor.execute("""
                SELECT id, animal_id, quantity_production, production_date
                FROM milkproductionrecord
            """)

            rows = cursor.fetchall()
            milkproductionrecords = []

            for row in rows:
                converted_date = (
                    datetime.fromisoformat(row[3])
                    if row[3]
                    else None
                )

                milkproduction = MilkProductionRecord(
                    id=row[0],
                    animal_id=row[1],
                    quantity_production=row[2],
                    production_date=converted_date
                )

                milkproductionrecords.append(milkproduction)

            return milkproductionrecords

        finally:
            conn.close()


    
    def update(self, milkproductionrecord: MilkProductionRecord):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                UPDATE milkproductionrecord
                SET animal_id = ?,
                    quantity_production = ?,
                    production_date = ?
                WHERE id = ?
                """,
                (
                    milkproductionrecord.animal_id,
                    milkproductionrecord.quantity_production,
                    milkproductionrecord.production_date.isoformat(),
                    milkproductionrecord.id
                )
            )

            logger.info(
                "Atualizando milkrecord id = %s",
                milkproductionrecord.id
            )

            conn.commit()

        finally:
            conn.close()

    
    def delete(self, id: int):
        conn = get_connection()

        try:
            cursor = conn.cursor()

            logger.info("Deletando MilkProductionRecord id=%s", id)

            cursor.execute(
                """
                DELETE FROM milkproductionrecord
                WHERE id = ?
                """,
                (id,)
            )

            conn.commit()

            logger.info("Exclusão do registro id=%s concluída", id)

        finally:
            conn.close()
