from django.shortcuts import render
from .models import *

def index(request):
    s = "<h1> Mahallalar </h1> \n"
    m = Mahalla.objects.all()
    context = {
        "m": m,
        "title": "MAHALLA NOMI"
    }

    return render(request, 'index.html', context=context)

def viloyat(request):
    s = "<h1> Viloyatlar </h1> \n"
    v = Viloyat.objects.all()
    context = {
        "v": v,
        "title": "VILOYATLAR TOGRISIDA"
    }

    return render(request, 'vil.html', context=context)

def tuman(request):
    s = "<h1> Tumanlar </h1> \n"
    t = Tuman.objects.all()
    context = {
        "t": t,
        "title": "TUMAN NOMLARI"
    }

    return render(request, 'tuman.html', context=context)