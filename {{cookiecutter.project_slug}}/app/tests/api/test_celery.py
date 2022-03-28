from typing import Dict

from fastapi.testclient import TestClient

from app.core.config import settings


def test_celery_worker_test(client: TestClient) -> None:
    data = {"msg": "test"}
    r = client.post(f"/utils/test-celery/", json=data)
    response = r.json()
    assert response["msg"] == "Message received"
