from collections.abc import Iterable
from datetime import datetime
from typing import Optional

from app.core.abstractions.statistics_repository import StatisticsRepository
from app.core.entities.statistics import Statistics
from psycopg import AsyncConnection
from psycopg.rows import class_row


class PostgresStatisticsRepository(StatisticsRepository):
    def __init__(self, connection: AsyncConnection) -> None:
        self.connection: AsyncConnection = connection

    async def save_statistics(self, statistic: Statistics) -> None:
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
                INSERT INTO statistics VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    statistic.id,
                    statistic.date,
                    statistic.views,
                    statistic.clicks,
                    statistic.cost,
                ),
            )

    async def read_statistics(
        self,
        from_date: datetime,
        to_date: datetime,
        sort_by: Optional[Iterable[str]] = None,
    ) -> Iterable[Statistics]:
        async with self.connection.cursor(row_factory=class_row(Statistics)) as cursor:
            sort_clause = ""
            if sort_by:
                sort_clause = f"ORDER BY {', '.join(sort_by)}"

            await cursor.execute(
                f"""
                SELECT * FROM statistics
                WHERE date >= %s AND date <= %s
                {sort_clause}
                """,
                (from_date, to_date),
            )

            return await cursor.fetchall()

    async def delete_all_saved_statistics(self) -> None:
        async with self.connection.cursor() as cursor:
            await cursor.execute(
                """
                DELETE FROM statistics
                """
            )
