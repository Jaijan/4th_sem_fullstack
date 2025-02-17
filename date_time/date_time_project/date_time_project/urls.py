from django.contrib import admin
from django.urls import path
from datetime_app.views import index, get_time

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('get_time/', get_time, name='get_time'),
]
