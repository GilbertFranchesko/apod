import os

from django.conf import settings
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skileo.settings')

app = Celery("skileo")


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'everyday.tasks.get_apod_picture',
        'schedule': crontab(hour=0, minute=0), # Every day
    },
}
app.conf.timezone = 'UTC'

app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

