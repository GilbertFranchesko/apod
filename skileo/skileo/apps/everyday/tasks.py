import datetime
from celery import shared_task
from apod.nasa import get_picture

from apod.models import PictureDay

@shared_task
def get_apod_picture():
    now = datetime.datetime.now()
    picture = get_picture(now)

    PictureDay.add([picture])

    
