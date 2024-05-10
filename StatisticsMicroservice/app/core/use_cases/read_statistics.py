from typing import List

from app.core.abstractions.statistics_repository import StatisticsRepository
from app.core.dto.statistics import ReadStatisticsDTO, StatisticsDTO
from app.core.exceptions.statistics_validation import StatisticsValidationError


class ReadStatistics:
    def __init__(self, repository: StatisticsRepository) -> None:
        self.repository = repository

    async def __call__(self, dto: ReadStatisticsDTO) -> List[StatisticsDTO]:
        for field in dto.sort_by:
            if field not in ["date", "views", "clicks", "cost"]:
                raise StatisticsValidationError(
                    f"Invalid sort field: {field}. "
                    "Available fields: ['date', 'views', 'clicks', 'cost']"
                )

        results = await self.repository.read_statistics(
            dto.from_date,
            dto.to_date,
            dto.sort_by,
        )

        return [StatisticsDTO.from_entity(result) for result in results]
