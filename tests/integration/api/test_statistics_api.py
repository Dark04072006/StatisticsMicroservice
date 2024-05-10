import asyncio
from collections.abc import AsyncGenerator

import pytest
import pytest_asyncio
from app.entrypoint.api import app_factory
from httpx import ASGITransport, AsyncClient


@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    app = app_factory()
    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport, base_url="http://test-server"
    ) as client:
        yield client


@pytest.mark.asyncio
async def test_save_statistics(client: AsyncClient) -> None:
    json = {"date": "2024-05-10", "views": 1000, "clicks": 50, "cost": 500.0}

    response = await client.post("/statistics/", json=json)

    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["date"].startswith(json["date"])
    assert response.json()["views"] == json["views"]
    assert response.json()["clicks"] == json["clicks"]
    assert response.json()["cost"] == json["cost"]


@pytest.mark.asyncio
async def test_read_statistics(client: AsyncClient) -> None:
    params = {
        "from": "2024-05-10",
        "to": "2024-05-15",
        "sort_by": ["date", "views", "clicks", "cost"],
    }
    response = await client.get("/statistics/", params=params)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_delete_all_saved_statistics(client: AsyncClient) -> None:
    json_first = {"date": "2024-05-10", "views": 1000, "clicks": 50, "cost": 500.0}
    json_second = {"date": "2024-05-11", "views": 1500, "clicks": 70, "cost": 700.0}

    tasks = [
        client.post("/statistics/", json=json_first),
        client.post("/statistics/", json=json_second),
    ]
    await asyncio.gather(*tasks)

    response = await client.delete("/statistics/")

    assert response.status_code == 204

    params = {
        "from": "2024-05-10",
        "to": "2024-05-11",
        "sort_by": ["date", "views", "clicks", "cost"],
    }
    response = await client.get("/statistics/", params=params)

    assert response.status_code == 200
    assert len(response.json()) == 0
