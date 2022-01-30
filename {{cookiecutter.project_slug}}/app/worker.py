from app.core.celery_app import celery_app
from app.config import settings


@celery_app.task(acks_late=True)
def test_celery(msg: str) -> str:
    return f"test task return {msg}"
