from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID

from app.core.entities.statistics import Statistics


@dataclass(frozen=True)
class StatisticsInputDTO:
    date: datetime
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[float]


@dataclass(frozen=True)
class StatisticsDTO(StatisticsInputDTO):
    id: UUID
    cpc: float
    cpm: float

    @staticmethod
    def from_entity(entity: Statistics) -> "StatisticsDTO":
        return StatisticsDTO(
            id=entity.id,
            date=entity.date,
            views=entity.views,
            clicks=entity.clicks,
            cost=entity.cost,
            cpc=entity.calculate_average_cost_per_click(),
            cpm=entity.calculate_average_cost_per_1000_impressions(),
        )


@dataclass(frozen=True)
class ReadStatisticsDTO:
    from_date: datetime
    to_date: datetime
    sort_by: Iterable[str]
