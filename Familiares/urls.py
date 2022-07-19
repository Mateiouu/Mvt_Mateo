from django.contrib import admin
from django.urls import path, include
from Familiares.views import *

from .views import familia, lista_familiar, inicio
urlpatterns = [
    path('agregar-familia/<nombre>/<dni>/<nacimiento>', familia),
    path('lista-familia/', lista_familiar),
    path('', inicio),
    path('agregar-familiares', add),
    
]
