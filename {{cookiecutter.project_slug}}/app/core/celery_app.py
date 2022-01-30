from celery import Celery

from app.core.config import settings

celery_app = Celery(settings.CELERY_APP_NAME, broker=settings.CELERY_BROKER)

celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue"}
