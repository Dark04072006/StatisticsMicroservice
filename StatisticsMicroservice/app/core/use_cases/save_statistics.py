from app.core.abstractions.statistics_repository import StatisticsRepository
from app.core.abstractions.transaction_manager import TransactionManager
from app.core.dto.statistics import StatisticsDTO, StatisticsInputDTO
from app.core.entities.statistics import Statistics


class SaveStatistics:
    def __init__(
        self,
        repository: StatisticsRepository,
        transaction_manager: TransactionManager,
    ) -> None:
        self.repository = repository
        self.transaction_manager = transaction_manager

    async def __call__(self, dto: StatisticsInputDTO) -> StatisticsDTO:
        statistic = Statistics.create(dto.date, dto.views, dto.clicks, dto.cost)

        await self.repository.save_statistics(statistic)

        await self.transaction_manager.commit()

        return StatisticsDTO.from_entity(statistic)
