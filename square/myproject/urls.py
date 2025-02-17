from django.contrib import admin
from django.urls import path
from squares.views import table_of_squares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('squares/<int:num>/', table_of_squares, name='table_of_squares'),
]
