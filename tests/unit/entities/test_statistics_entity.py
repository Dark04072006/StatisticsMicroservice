from datetime import datetime

import pytest
from app.core.entities.statistics import Statistics
from app.core.exceptions.statistics_validation import StatisticsValidationError


def test_statistics_creation():
    date = datetime(2024, 5, 10)
    stats = Statistics.create(date, views=1000, clicks=50, cost=500.0)

    assert stats.id is not None
    assert stats.date == date
    assert stats.views == 1000
    assert stats.clicks == 50
    assert stats.cost == 500.0


def test_statistics_invalid_date():
    with pytest.raises(TypeError):
        Statistics.create("2024-05-10", views=1000, clicks=50, cost=500.0)


def test_statistics_invalid_views():
    with pytest.raises(StatisticsValidationError):
        Statistics.create(datetime(2024, 5, 10), views=-100, clicks=50, cost=500.0)


def test_statistics_invalid_clicks():
    with pytest.raises(StatisticsValidationError):
        Statistics.create(datetime(2024, 5, 10), views=1000, clicks=-50, cost=500.0)


def test_statistics_invalid_cost():
    with pytest.raises(StatisticsValidationError):
        Statistics.create(datetime(2024, 5, 10), views=1000, clicks=50, cost=-500.0)


def test_average_cost_per_click():
    stats = Statistics.create(datetime(2024, 5, 10), views=1000, clicks=50, cost=500.0)
    assert stats.calculate_average_cost_per_click() == 10.00


def test_average_cost_per_click_with_zero_clicks():
    stats = Statistics.create(datetime(2024, 5, 10), views=1000, clicks=0, cost=0.0)
    assert stats.calculate_average_cost_per_click() == 0.00


def test_average_cost_per_1000_impressions():
    stats = Statistics.create(datetime(2024, 5, 10), views=1000, clicks=50, cost=500.0)
    assert stats.calculate_average_cost_per_1000_impressions() == 500.00


def test_average_cost_per_1000_impressions_with_zero_views():
    stats = Statistics.create(datetime(2024, 5, 10), views=0, clicks=50, cost=500.0)
    assert stats.calculate_average_cost_per_1000_impressions() == 0.00
