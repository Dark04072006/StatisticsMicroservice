from app.core.abstractions.statistics_repository import StatisticsRepository
from app.core.abstractions.transaction_manager import TransactionManager


class DeleteAllSavedStatistics:
    def __init__(
        self,
        repository: StatisticsRepository,
        transaction_manager: TransactionManager,
    ) -> None:
        self.repository = repository
        self.transaction_manager = transaction_manager

    async def __call__(self) -> None:
        await self.repository.delete_all_saved_statistics()
        await self.transaction_manager.commit()
