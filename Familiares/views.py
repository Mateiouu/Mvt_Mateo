from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Familiar



def familia(self, nombre, dni, nacimiento,):
    familia = Familiar(nombre =  nombre , dni = dni, nacimiento = nacimiento)
    familia.save()

    return HttpResponse(f'''
    <p> El familiar <strong>{familia.nombre}</strong> de Dni <strong>{familia.dni} </strong>, se ha agregado correctamente</p>
    ''') 

def lista_familiar(self):
    lista = Familiar.objects.all()
    return render(self, 'lista-familiares.html',{'lista_familiares': lista})

def inicio(self):
    return render(self, 'inicio.html')

def add(self):
    return render(self, 'upload.html')