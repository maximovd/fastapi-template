from typing import Any

from fastapi import APIRouter

from app import schemas
from app.core.celery_app import celery_app
from app.worker import test_celery_task

router = APIRouter()


@router.post("/test-celery/", response_model=schemas.Msg, status_code=201)
def test_celery(msg: schemas.Msg) -> Any:
    """Test Celery worker."""
    test_celery_task.delay(msg.msg)
    return {"msg": "Message received"}
