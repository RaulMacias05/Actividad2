from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index.html"),
    path("contacto.html/",views.contacto, name="contacto.html"),
    path("estadio.html/",views.estadio, name="estadio.html"),
    path("jugadores.html/",views.jugadores, name="jugadores.html"),
    path("titulos.html/",views.titulos, name="titulos.html")
]