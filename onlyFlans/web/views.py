from django.shortcuts import render
from .models import Flan


def indice(request):
    return render(request, 'index.html', {})


def acerca(request):
    return render(request, 'about.html', {})


def bienvenido(request):
    return render(request, 'welcome.html', {})


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})


def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})
