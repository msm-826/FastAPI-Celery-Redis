import time
from datetime import datetime, timedelta
from random import randint

from celery import Celery

from app.main import app

celery_app = Celery(
    __name__,
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0'
)


@celery_app.task(name="scheduled_function")
def scheduled_function():
    time.sleep(randint(5, 10))
    print(f"scheduled function executed at {datetime.now()}")
    return True


celery_app.conf.beat_schedule = {
    'run-every-minute': {
        'task': 'scheduled_function',
        # 'schedule': crontab(minute='*/1'),
        'schedule': timedelta(seconds=8)
    }
}

celery_app.conf.timezone = 'UTC'
