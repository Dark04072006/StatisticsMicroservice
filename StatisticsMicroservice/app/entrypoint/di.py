from collections.abc import AsyncIterable

from app.core.abstractions.statistics_repository import StatisticsRepository
from app.core.abstractions.transaction_manager import TransactionManager
from app.core.use_cases.delete_all_saved_statistics import DeleteAllSavedStatistics
from app.core.use_cases.read_statistics import ReadStatistics
from app.core.use_cases.save_statistics import SaveStatistics
from app.entrypoint.config import Config
from app.infrastructure.persistence.statistics_repository import (
    PostgresStatisticsRepository,
)
from app.infrastructure.persistence.transaction_manager import (
    PostgresTransactionManager,
)
from dishka import Provider, Scope, provide
from psycopg import AsyncConnection
from psycopg.conninfo import conninfo_to_dict


class PersistenceProvider(Provider):
    def __init__(self, config: Config) -> None:
        super().__init__(scope=Scope.REQUEST)
        self.config = config

    @provide(provides=AsyncConnection)
    async def provide_db_connection(self) -> AsyncIterable[AsyncConnection]:
        conn_info = conninfo_to_dict(self.config.db_uri)
        async with await AsyncConnection.connect(**conn_info) as connection:
            yield connection

    transaction_manager = provide(
        PostgresTransactionManager, provides=TransactionManager
    )
    statistics_repository = provide(
        PostgresStatisticsRepository, provides=StatisticsRepository
    )


class UseCasesProvider(Provider):
    scope = Scope.REQUEST

    save_statistics = provide(SaveStatistics)
    read_statistics = provide(ReadStatistics)
    delete_all_saved_statistics = provide(DeleteAllSavedStatistics)
