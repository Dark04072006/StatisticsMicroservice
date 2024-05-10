from unittest.mock import AsyncMock

import pytest
from app.core.abstractions.statistics_repository import StatisticsRepository
from app.core.abstractions.transaction_manager import TransactionManager
from app.core.use_cases.delete_all_saved_statistics import DeleteAllSavedStatistics


@pytest.fixture
def repository_mock() -> AsyncMock:
    return AsyncMock(spec=StatisticsRepository)


@pytest.fixture
def transaction_manager_mock() -> AsyncMock:
    return AsyncMock(spec=TransactionManager)


@pytest.fixture
def delete_all_saved_statistics_use_case(
    repository_mock: StatisticsRepository, transaction_manager_mock: TransactionManager
) -> DeleteAllSavedStatistics:
    return DeleteAllSavedStatistics(repository_mock, transaction_manager_mock)


@pytest.mark.asyncio
async def test_delete_all_saved_statistics(
    repository_mock: AsyncMock,
    transaction_manager_mock: AsyncMock,
    delete_all_saved_statistics_use_case: DeleteAllSavedStatistics,
) -> None:
    await delete_all_saved_statistics_use_case()

    repository_mock.delete_all_saved_statistics.assert_called_once()
    transaction_manager_mock.commit.assert_called_once()
