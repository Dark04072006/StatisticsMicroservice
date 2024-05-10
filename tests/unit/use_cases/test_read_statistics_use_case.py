from datetime import datetime
from unittest.mock import AsyncMock

import pytest
from app.core.abstractions.statistics_repository import StatisticsRepository
from app.core.dto.statistics import ReadStatisticsDTO, StatisticsDTO
from app.core.entities.statistics import Statistics
from app.core.exceptions.statistics_validation import StatisticsValidationError
from app.core.use_cases.read_statistics import ReadStatistics


@pytest.fixture
def repository_mock() -> AsyncMock:
    return AsyncMock(spec=StatisticsRepository)


@pytest.fixture
def read_statistics_use_case(repository_mock: StatisticsRepository) -> ReadStatistics:
    return ReadStatistics(repository_mock)


@pytest.mark.asyncio
async def test_read_statistics_with_valid_sort_fields(
    repository_mock: AsyncMock,
    read_statistics_use_case: ReadStatistics,
) -> None:
    from_date = datetime(2024, 5, 1)
    to_date = datetime(2024, 5, 10)
    sort_by = ["date", "views"]
    dto = ReadStatisticsDTO(from_date=from_date, to_date=to_date, sort_by=sort_by)
    mock_results = [
        Statistics(id=1, date=datetime(2024, 5, 1), views=100, clicks=10, cost=50.0),
        Statistics(id=2, date=datetime(2024, 5, 5), views=200, clicks=20, cost=100.0),
        Statistics(id=3, date=datetime(2024, 5, 10), views=150, clicks=15, cost=75.0),
    ]
    repository_mock.read_statistics = AsyncMock(return_value=mock_results)

    result = await read_statistics_use_case(dto)

    repository_mock.read_statistics.assert_called_once_with(from_date, to_date, sort_by)
    assert isinstance(result, list)
    assert len(result) == len(mock_results)
    for idx, stats in enumerate(result):
        assert isinstance(stats, StatisticsDTO)
        assert stats.id == mock_results[idx].id
        assert stats.date == mock_results[idx].date
        assert stats.views == mock_results[idx].views
        assert stats.clicks == mock_results[idx].clicks
        assert stats.cost == mock_results[idx].cost


@pytest.mark.asyncio
async def test_read_statistics_with_invalid_sort_field(
    read_statistics_use_case: ReadStatistics,
) -> None:
    # Arrange
    from_date = datetime(2024, 5, 1)
    to_date = datetime(2024, 5, 10)
    sort_by = ["date", "invalid_field"]
    dto = ReadStatisticsDTO(from_date=from_date, to_date=to_date, sort_by=sort_by)

    # Act and assert
    with pytest.raises(StatisticsValidationError):
        await read_statistics_use_case(dto)
