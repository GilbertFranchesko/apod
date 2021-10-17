import requests

from django.conf import settings


# Name: get count pictures
# Description: function for create request to NASA API.
# Params: count(int)
# Return: json
def get_picture(date):
    
    formatting_date = date.strftime("%Y-%m-%d")
    data = {
        "api_key": settings.NASA_TOKEN,
        "date": date
    }

    request = requests.get(settings.NASA_APOD_URL, data)

    return request.json()

# Name: get count pictures
# Description: function for create request to NASA API.
# Params: count(int)
# Return: json
def get_pictures(start_date, end_date):

    formatting_start_date = start_date.strftime("%Y-%m-%d")
    formatting_end_date = end_date.strftime("%Y-%m-%d")

    data = {
        "api_key": settings.NASA_TOKEN,
        "start_date": formatting_start_date,
        "end_date": formatting_end_date
    }

    request = requests.get(settings.NASA_APOD_URL, data)
    print(request.url)
    return request.json()