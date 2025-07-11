from django.shortcuts import render
from django.http import JsonResponse

def flight_info(request):
    return JsonResponse({"from": "Tashkent", "to": "Istanbul", "duration": "5 soat"})

def hospital_detail(request):
    return JsonResponse({"name": "Shifokor", "departments": 12, "open": True})

def app_detail(request):
    return JsonResponse({"name": "Telegram", "users": "800 mln", "platform": "Cross-platform"})
