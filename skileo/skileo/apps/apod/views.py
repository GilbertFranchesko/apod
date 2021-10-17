from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .models import PictureDay
from .nasa import get_picture, get_pictures

# Name view: MainView
# Description: checks if the application is first launched.
# Route: / 
def main_view(request):

    list_of_pictures = PictureDay.objects.all()
    
    # Application first launched
    if len(list_of_pictures) is 0:
        
        now_date = datetime.datetime.now()
        mod_date = now_date - datetime.timedelta(days=14)
        
        pictures = get_pictures(mod_date, now_date)
        
        new_pictures = list()
        for picture in pictures:
            new_pictures.append(
                {
                    "title": picture['title'],
                    "explanation": picture['explanation'],
                    "date": picture['date'],
                    "media_type": picture['media_type'],
                    "url": picture['url'],
                }
            )

        PictureDay.add(new_pictures)
    

    now_date = datetime.datetime.now()
    next_date = (now_date + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    previous_date = (now_date - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    now_date = now_date.strftime("%Y-%m-%d")

    today_picture = PictureDay.objects.get(date=now_date)
    return render(request, "main.tpl", {"picture": today_picture, "next_day": next_date, "previous_date": previous_date})

def select_view(request, date):

    now = datetime.datetime.now()
    tomorrow = datetime.datetime(now.year, now.month, now.day + 1).strftime("%Y-%m-%d")
    if date == tomorrow:
        return HttpResponse("not found")

    else: 
        format_date = datetime.datetime.strptime(date, "%Y-%m-%d")

        next_date = (format_date + datetime.timedelta(days=1))
        format_next_date = next_date.strftime("%Y-%m-%d")

        previous_date = (format_date - datetime.timedelta(days=1))
        previous_date_format = previous_date.strftime("%Y-%m-%d")


        selected_picture = PictureDay.objects.get(date=format_date)
        return render(request, "main.tpl", {"picture": selected_picture, "next_day": format_next_date, "previous_date": previous_date_format})
