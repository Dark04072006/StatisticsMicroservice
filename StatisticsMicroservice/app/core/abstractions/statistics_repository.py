from abc import ABC, abstractmethod
from collections.abc import Iterable
from datetime import datetime
from typing import Optional

from app.core.entities.statistics import Statistics


class StatisticsRepository(ABC):
    @abstractmethod
    async def save_statistics(self, statistic: Statistics) -> None: ...

    @abstractmethod
    async def read_statistics(
        self,
        from_date: datetime,
        to_date: datetime,
        sort_by: Optional[Iterable[str]] = None,
    ) -> Iterable[Statistics]: ...

    @abstractmethod
    async def delete_all_saved_statistics(self) -> None: ...
