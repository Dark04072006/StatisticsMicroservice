from datetime import datetime
from unittest.mock import AsyncMock, patch

import pytest
from app.core.abstractions.statistics_repository import StatisticsRepository
from app.core.abstractions.transaction_manager import TransactionManager
from app.core.dto.statistics import StatisticsDTO, StatisticsInputDTO
from app.core.entities.statistics import Statistics
from app.core.use_cases.save_statistics import SaveStatistics


@pytest.fixture
def repository_mock() -> AsyncMock:
    return AsyncMock(spec=StatisticsRepository)


@pytest.fixture
def transaction_manager_mock() -> AsyncMock:
    return AsyncMock(spec=TransactionManager)


@pytest.fixture
def save_statistics_use_case(
    repository_mock: StatisticsRepository,
    transaction_manager_mock: TransactionManager,
) -> SaveStatistics:
    return SaveStatistics(repository_mock, transaction_manager_mock)


@pytest.mark.asyncio
async def test_save_statistics(
    repository_mock: StatisticsRepository,
    save_statistics_use_case: SaveStatistics,
    transaction_manager_mock: TransactionManager,
) -> None:
    input_dto = StatisticsInputDTO(
        date=datetime(2024, 5, 10), views=1000, clicks=50, cost=500.0
    )
    expected_entity = Statistics.create(
        input_dto.date,
        input_dto.views,
        input_dto.clicks,
        input_dto.cost,
    )
    expected_dto = StatisticsDTO.from_entity(expected_entity)

    with patch.object(
        Statistics,
        "create",
        return_value=expected_entity,
    ):
        result_dto = await save_statistics_use_case(input_dto)

    repository_mock.save_statistics.assert_called_once_with(expected_entity)
    transaction_manager_mock.commit.assert_called_once()

    assert result_dto == expected_dto
