from datetime import datetime
from typing import Annotated, List

from app.core.dto.statistics import ReadStatisticsDTO, StatisticsDTO, StatisticsInputDTO
from app.core.use_cases.delete_all_saved_statistics import DeleteAllSavedStatistics
from app.core.use_cases.read_statistics import ReadStatistics
from app.core.use_cases.save_statistics import SaveStatistics
from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Query

router = APIRouter(prefix="/statistics", tags=["statistics"])


@router.post("/", response_model=StatisticsDTO, status_code=201)
@inject
async def save_statistics(
    dto: StatisticsInputDTO,
    save_statistic: FromDishka[SaveStatistics],
) -> StatisticsDTO:
    return await save_statistic(dto)


@router.get("/", response_model=List[StatisticsDTO])
@inject
async def read_statistics(
    read_statistics: FromDishka[ReadStatistics],
    from_date: Annotated[
        datetime,
        Query(
            alias="from",
            description="period start date (inclusive)",
        ),
    ],
    to_date: Annotated[
        datetime,
        Query(
            alias="to",
            description="period end date (inclusive)",
        ),
    ],
    sort_by: Annotated[
        List[str],
        Query(
            default_factory=list,
            description=(
                "fields to sort statistics. "
                "Available: ['date', 'views', 'clicks', 'cost']"
            ),
        ),
    ],
) -> List[StatisticsDTO]:
    dto = ReadStatisticsDTO(from_date, to_date, sort_by)

    return await read_statistics(dto)


@router.delete("/", status_code=204)
@inject
async def delete_all_saved_statistics(
    delete_all_saved_statistics: FromDishka[DeleteAllSavedStatistics],
) -> None:
    await delete_all_saved_statistics()
