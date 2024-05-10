from app.core.abstractions.transaction_manager import TransactionManager
from psycopg import AsyncConnection


class PostgresTransactionManager(TransactionManager):
    def __init__(self, connection: AsyncConnection) -> None:
        self.connection: AsyncConnection = connection

    async def commit(self) -> None:
        await self.connection.commit()

    async def rollback(self) -> None:
        await self.connection.rollback()
