import requests, os
from django.db import models
from django.core.files import File
from tempfile import NamedTemporaryFile
from urllib.request import urlopen

class PictureDay(models.Model):
    title = models.CharField(max_length=255)
    explanation = models.TextField()
    date = models.DateField()
    image_file = models.ImageField(upload_to="images", null=True)
    video_url = models.URLField(default="None")
    media_type = models.CharField(max_length=255, blank=True)


    # Name: add
    # Static method
    # Description: this method add pictures in database and download her in 
    #    'images' folder.
    # Return: status(boolean)

    @staticmethod
    def add(list_new_pictures):
        for picture in list_new_pictures:
            new_picture_object = PictureDay(
                title = picture['title'],
                explanation = picture['explanation'],
                date = picture['date'],
                media_type = picture['media_type']
            )
            
            if picture['media_type'] == "image":
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(urlopen(picture['url']).read())
                img_temp.flush()
                new_picture_object.image_file.save(f"{picture['date']}.jpg", File(img_temp))

            elif picture['media_type'] == "video":
                new_picture_object.video_url = picture['url']
        
            new_picture_object.save()
        
        return True

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")