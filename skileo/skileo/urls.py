from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from apod.views import main_view, select_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name="apod_main_view"),
    path('<str:date>/', select_view, name="apod_select_view")
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()