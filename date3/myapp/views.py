from django.shortcuts import render
from datetime import datetime

def date3_view(request):
    now = datetime.now()
    hours = now.hour % 12 or 12  
    initial_hours = str(hours).zfill(2)
    initial_minutes = str(now.minute).zfill(2)
    initial_seconds = str(now.second).zfill(2)
    initial_ampm = "PM" if now.hour >= 12 else "AM"
    
    return render(request, 'myapp/date3.html', {
        'initial_hours': initial_hours,
        'initial_minutes': initial_minutes,
        'initial_seconds': initial_seconds,
        'initial_ampm': initial_ampm,
    })
