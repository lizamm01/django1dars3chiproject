from django.shortcuts import render
from django.http import JsonResponse

def news_article(request):
    return JsonResponse({"headline": "Texnologiya yangiliklari", "views": 10500})

def planet_info(request):
    return JsonResponse({"name": "Mars", "type": "Quruq", "distance_from_sun": "227 mln km"})

def company_detail(request):
    return JsonResponse({"name": "Google", "industry": "IT", "founded": 1998})
