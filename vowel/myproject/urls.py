from django.contrib import admin
from django.urls import path
from textanalysis.views import analyze_text

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyze/<str:text>/', analyze_text, name='analyze_text'),
]
