from app.api.exc_handlers import init_exc_handlers
from app.api.routers.statistics import router
from app.entrypoint.config import Config
from app.entrypoint.di import PersistenceProvider, UseCasesProvider
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI


def app_factory() -> FastAPI:
    app = FastAPI()

    app.include_router(router)

    config = Config.load_from_env()

    container = make_async_container(
        PersistenceProvider(config),
        UseCasesProvider(),
    )
    init_exc_handlers(app)
    setup_dishka(container, app)

    return app
