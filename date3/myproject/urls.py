from django.contrib import admin
from django.urls import path
from myapp.views import date3_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('date3/', date3_view, name='date3'),
]
