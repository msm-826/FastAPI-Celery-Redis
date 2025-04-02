import time
from datetime import datetime, timedelta
from random import randint

from celery import Celery
from celery.signals import celeryd_after_setup, worker_init
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

celery_app = Celery(
    __name__,
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    broker_connection_retry_on_startup=True
)


@celeryd_after_setup.connect
def setup_worker(sender=None, instance=None, **kwargs):
    logger.info("---------------------------------------")
    logger.info(f"Worker {instance.hostname} initialized")
    logger.info("---------------------------------------")


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

celery_app.conf.timezone = 'Asia/Kolkata'
