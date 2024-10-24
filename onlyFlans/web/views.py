from django.shortcuts import render

def indice(request):
    return render(request, 'index.html', {})

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    return render(request, 'welcome.html', {})
