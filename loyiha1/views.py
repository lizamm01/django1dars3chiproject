from django.shortcuts import render
from django.http import JsonResponse

def university_info(request):
    return JsonResponse({"name": "TATU", "faculty": "IT", "students": 5000})

def shop_item(request):
    return JsonResponse({"item": "Kofta", "price": 150, "in_stock": True})

def restaurant_menu(request):
    return JsonResponse({"dish": "Osh", "price": 30000, "available": True})

