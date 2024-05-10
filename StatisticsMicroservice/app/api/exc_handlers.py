from typing import cast

from app.core.exceptions.statistics_validation import StatisticsValidationError
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.types import ExceptionHandler


async def statistics_validation_error_handler(
    _: Request,
    exc: StatisticsValidationError,
) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content={
            "status": "error",
            "message": exc.message,
        },
    )


def init_exc_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        StatisticsValidationError,
        cast(ExceptionHandler, statistics_validation_error_handler),
    )
