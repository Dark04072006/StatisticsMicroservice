from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from app.core.exceptions.statistics_validation import StatisticsValidationError


@dataclass
class Statistics:
    id: UUID
    date: datetime
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[float]

    def __post_init__(self) -> None:
        self._validate_date_type()
        self._validate_views()
        self._validate_clicks()
        self._validate_cost()

    def _validate_date_type(self) -> None:
        if not isinstance(self.date, datetime):
            raise TypeError("date must be an instance of datetime object")

    def _validate_views(self) -> None:
        if self.views is not None and not isinstance(self.views, int):
            raise TypeError("views must be an integer")
        if self.views and self.views < 0:
            raise StatisticsValidationError("views must be greater than or equal to 0")

    def _validate_clicks(self) -> None:
        if self.clicks is not None and not isinstance(self.clicks, int):
            raise TypeError("clicks must be an integer")
        if self.clicks and self.clicks < 0:
            raise StatisticsValidationError("clicks must be greater than or equal to 0")

    def _validate_cost(self) -> None:
        if self.cost is not None and not isinstance(self.cost, float):
            raise TypeError("cost must be a float")
        if self.cost and self.cost < 0.00:
            raise StatisticsValidationError("cost must be greater than or equal to 0")

    @staticmethod
    def create(
        date: datetime,
        views: Optional[int] = None,
        clicks: Optional[int] = None,
        cost: Optional[float] = None,
    ) -> "Statistics":
        return Statistics(uuid4(), date, views, clicks, cost)

    def calculate_average_cost_per_click(self) -> float:
        if not self.cost or not self.clicks:
            return 0.00
        return round(self.cost / self.clicks, 2)

    def calculate_average_cost_per_1000_impressions(self) -> float:
        if not self.cost or not self.views:
            return 0.00
        return round((self.cost / self.views) * 1000, 2)
