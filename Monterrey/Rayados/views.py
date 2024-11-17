from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "Rayados/index.html", {})

def contacto(request):
    return render(request, "Rayados/contacto.html", {})

def estadio(request):
    return render(request, "Rayados/estadio.html", {})

def jugadores(request):
    return render(request, "Rayados/jugadores.html", {})

def titulos(request):
    return render(request, "Rayados/titulos.html", {})