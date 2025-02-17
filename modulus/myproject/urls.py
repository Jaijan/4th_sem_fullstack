from django.contrib import admin
from django.urls import path
from modapp.views import mod_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mod/<int:dividend>/<int:divisor>/', mod_view, name='mod_view'),
]
