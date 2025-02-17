from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'datetime_app/index.html')

def get_time(request):
    now = datetime.now()
    time_str = now.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    date_str = now.strftime("%A, %d %B %Y")
    
    return JsonResponse({"time": time_str, "date": date_str})
